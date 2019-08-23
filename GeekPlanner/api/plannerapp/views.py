"""
Module for plannerapp views.
"""
from django.db.models import Q

from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .serializers import (
    ProjectSerializer,
    CardSerializer,
    CategorySerializer,
)
from .models import (
    Project,
    Card,
    Category,
    Participation,
)
from .pagination import ProjectPageNumberPagination
from .permissions import (
    ProjectPermissions,
    ProjectDataPermissions,
)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated, ProjectPermissions])
def set_project_participation(request, pk):
    """
    Changes state of user participation in a project upon
    clicking the Join/Leave buttons.
    :param request: request object.
    :param pk: project PK.
    :return: Response with HTTP 200 status code.
    """
    participation = Participation.objects.get_or_create(
        project=pk,
        user=request.user,
    )
    participation.is_active = request.data['participate']
    participation.save()
    return Response(status=status.HTTP_200_OK)


def get_default_categories():
    """
    Gets list of predefined categories.
    :return: list of predefined Category objects.
    """
    return [
        Category.objects.get_or_create(name=name)[0]
        for name in ['TO-DO', 'Do Today', 'In Progress', 'Done']
    ]


class ProjectListAPIView(generics.ListAPIView):
    """
    View which controls a collection of Project instances.
    Provides method(s): GET.
    """
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ProjectPageNumberPagination

    def get_queryset(self):
        """
        Project will be fetched only if:
        * Project has is_active=True value. (and)
        * Project was created by the current user (or)
        * Project was created by anybody, but it has public status (is_public=True).
        :return: filtered queryset with projects.
        """
        return Project.objects.filter(
            Q(is_active=True) & (
                Q(is_public=True) | (
                    Q(participation__is_active=True) &
                    Q(participation__user=self.request.user)
                )
            )
        ).select_related('is_owner').order_by('date_created')


class ProjectCreateAPIView(generics.CreateAPIView):
    """
    View which controls creation of Project.
    Provides method(s): POST.
    """
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Creates Project and adds Participation data.
        :param request: Request instance.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        :return: Response object.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        Participation.objects.create(
            project_id=serializer.data['id'],
            user_id=request.user.id,
            is_owner=True,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProjectRetrieveAPIView(generics.RetrieveAPIView):
    """
    View which allows user to see project content.
    Provides method(s): GET.
    """
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Project can be retrieved only if:
        * Project have not been deleted yet. (and)
        * User joined the project.
        :return: filtered queryset with projects.
        """
        return Project.objects.filter(
            Q(is_active=True) &
            Q(participation__user=self.request.user)
        )

    def get(self, request, *args, **kwargs):
        """
        Retrieves project content: cards and categories.
        :param request: Request instance.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        :return: Response with dict of cards and categories.
        """
        project = self.get_object()
        categories = get_default_categories()

        categories_cards = {}
        for category in categories:
            cards = Card.objects.filter(
                Q(project=project.pk) &
                Q(is_active=True) &
                Q(category=category)
            )
            categories_cards[category.name] = CardSerializer(cards, many=True).data

        return Response({
            'information': ProjectSerializer(project).data,
            'categories': CategorySerializer(categories, many=True).data,
            'cards': categories_cards
        })


class ProjectUpdateAPIView(generics.UpdateAPIView):
    """
    View which allows project participant to update project.
    Provides method(s): UPDATE.
    """
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Project can be updated only if:
        * It have not been deleted yet.
        * Current user joined the project.
        :return: filtered queryset with projects.
        """
        return Project.objects.filter(
            Q(is_active=True) &
            Q(participation__is_active=True) &
            Q(participation__user=self.request.user)
        )

    def update(self, request, *args, **kwargs):
        pass


class ProjectDestroyAPIView(generics.DestroyAPIView):
    """
    View which allows project owner to delete it.
    Provides method(s): DELETE.
    """
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Project can be deleted only if:
        * It have not been deleted yet.
        * Current user is the owner of this project.
        :return: filtered queryset with projects.
        """
        return Project.objects.filter(
            Q(is_active=True) &
            Q(participation__is_active=True) &
            Q(participation__user=self.request.user) &
            Q(participation__is_owner=True)
        )

    def delete(self, request, *args, **kwargs):
        """
        Sets project as "inactive" to be able to recover project via admin panel.
        :param request: Request instance.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        :return: Response with HTTP 204 status code.
        """
        project = self.get_object()
        project.is_active = False
        project.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CardCreateAPIView(generics.CreateAPIView):
    """
    View which controls process of creation of single Card instance.
    Provides method(s): POST.
    """
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated, ProjectDataPermissions]


class CardRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    View which controls a single instance of Card and allows to
    delete, modify, create and show its details.
    Provides method(s): GET, PUT, PATCH, DELETE.
    """
    queryset = Card.objects.filter(is_active=True).order_by('pk')
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated, ProjectDataPermissions]

    def delete(self, request, *args, **kwargs):
        """
        Sets card as "inactive" to be able to recover card via admin panel.
        :param request: Request instance.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        :return: Response with HTTP 204 status code.
        """
        card = self.get_object()
        card.is_active = False
        card.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
