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


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer of Project model."""
    id = serializers.ReadOnlyField()
    thumbnail = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'thumbnail', 'is_public',)


class CardSerializer(serializers.ModelSerializer):
    """Serializer of Card model."""
    id = serializers.ReadOnlyField()

    class Meta:
        model = Card
        fields = ('id', 'title', 'description', 'priority',)


class CategorySerializer(serializers.ModelSerializer):
    """Serializer of Category model."""
    id = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = ('id', 'name',)


class ParticipationSerializes(serializers.ModelSerializer):
    """Serialize of Participation model."""
    class Meta:
        model = Participation
        fields = ('project', 'user', 'is_owner',)
