"""
Module for plannerapp views.
"""
from django.db.models import Q

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
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
)
from .pagination import ProjectLimitOffsetPagination


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
    queryset = Project.objects.filter(is_active=True).order_by('date_created')
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ProjectLimitOffsetPagination

    def get_serializer_context(self):
        """
        Overrides context with page title.
        :return: updated context with page title.
        """
        context = super(ProjectListAPIView, self).get_serializer_context()
        context.update({'title': 'Projects'})
        return context


class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    View which controls a single instance of Project and allows to
    delete, modify, create and show its details.
    Provides method(s): GET, PUT, PATCH, DELETE.
    """
    queryset = Project.objects.filter(is_active=True).order_by('date_created')
    serializer_class = ProjectSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Retrieves project content: cards and categories.
        :param request: Request instance.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        :return: Response with dict of cards and categories.
        """
        project = self.get_object()
        project_serializer = ProjectSerializer(project)

        categories = self.get_project_categories(project.pk)
        categories_cards = {}
        for category in categories:
            cards = Card.objects.filter(
                Q(project=project.pk) &
                Q(is_active=True) &
                Q(category=category)
            )
            serialized_category = CategorySerializer(category)
            serialized_cards = CardSerializer(cards, many=True)
            categories_cards[serialized_category.data] = serialized_cards.data

        return Response(data={
            'project': project_serializer.data,
            'categories_cards': categories_cards
        })

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

    def get_project_categories(self, project_pk):
        # TODO
        return [
            *get_default_categories(),
            # Category.objects.filter(projects=project_pk),
        ]


class CardCreateAPIView(generics.CreateAPIView):
    """
    View which controls process of creation of single Card instance.
    Provides method(s): POST.
    """
    serializer_class = CardSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]


class CardRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    View which controls a single instance of Card and allows to
    delete, modify, create and show its details.
    Provides method(s): GET, PUT, PATCH, DELETE.
    """
    queryset = Card.objects.filter(is_active=True).order_by('pk')
    serializer_class = CardSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

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

