"""
Model for authapp serializers.
"""
from django.db import transaction, models
from django.core.exceptions import ValidationError

from rest_framework import serializers

from .models import (
    User,
    UserProfile,
)


class UserLoginSerializer(serializers.ModelSerializer):
    """Serializer for registration form."""
    token = models.CharField()

    class Meta:
        model = User
        fields = ('username', 'password', 'token')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        """
        Validates user credentials from the login form.
        :param attrs: form data.
        :return: validated data.
        """
        username = attrs.get('username', None)
        if username is None:
            raise ValidationError('Username field should be filled!')

        password = attrs.get('password', None)
        if password is None:
            raise ValidationError('Password field should be filled!')

        user = User.objects.filter(
            models.Q(username=username) &
            models.Q(password=password)
        )
        if not user.exists():
            raise ValidationError('Such username/password does not exist!')
        if not user.check_password(password):
            raise ValidationError('Incorrect password!')

        return attrs


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer of UserProfile model."""
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """Serializer of User model."""
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """
        Creates user account.
        :param validated_data: data passed through validation.
        :return: instance of User model.
        """
        validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        # UserProfile creation will be triggered by save()
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Updates user account information.
        :param instance: user instance.
        :param validated_data: data passed through validation.
        :return: updated User instance.
        """
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        profile.avatar = profile_data.get('avatar', profile.avatar)
        profile.gender = profile_data.get('gender', profile.gender)

        with transaction.atomic():
            instance.save()
            profile.save()

        return instance
