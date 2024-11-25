from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Client, Project
from .Serializers import ClientSerializer, ProjectSerializer
from django.contrib.auth.models import User

# CRUD for Clients
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

# CRUD for Projects
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# Retrieve projects assigned to logged-in user
class UserProjectsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        projects = request.user.projects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)