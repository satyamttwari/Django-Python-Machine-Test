from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
    users = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']