from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ("code", "email", "first_name", "last_name", "objetivo")
