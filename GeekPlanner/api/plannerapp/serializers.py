"""
Module for plannerapp serializers.
"""
from rest_framework import serializers

from .models import (
    Project,
    Card,
    Category,
)


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer of Project model."""
    class Meta:
        model = Project
        fields = ('title', 'description', 'thumbnail', 'is_public')


class CategorySerializer(serializers.ModelSerializer):
    """Serializer of Category model."""
    class Meta:
        model = Category
        fields = ('name',)


class CardSerializer(serializers.ModelSerializer):
    """Serializer of Card model."""
    class Meta:
        model = Card
        fields = ('title', 'description', 'priority',)
