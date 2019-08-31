"""
Module for plannerapp serializers.
"""
from rest_framework import serializers

from .models import (
    Project,
    Card,
    Category,
    Participation,
)


class ParticipationSerializer(serializers.ModelSerializer):
    """Serialize of Participation model."""
    class Meta:
        model = Participation
        fields = ('project', 'user', 'is_owner',)


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer of Project model."""
    id = serializers.ReadOnlyField()
    thumbnail = serializers.ImageField(
        required=False,
        allow_null=True
    )
    is_owner = serializers.ReadOnlyField(
        source='project_participation_set__is_owner',
        allow_null=True
    )

    class Meta:
        model = Project
        fields = ('id', 'title', 'date_created', 'description',
                  'thumbnail', 'is_public', 'is_owner')


class CardSerializer(serializers.ModelSerializer):
    """Serializer of Card model."""
    id = serializers.ReadOnlyField()

    class Meta:
        model = Card
        fields = ('id', 'title', 'description', 'priority',
                  'project', 'category')


class CategorySerializer(serializers.ModelSerializer):
    """Serializer of Category model."""
    id = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = ('id', 'name',)
