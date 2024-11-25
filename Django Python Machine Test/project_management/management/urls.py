from django.urls import path
from .views import (
    ClientListCreateView, ClientRetrieveUpdateDestroyView,
    ProjectListCreateView, UserProjectsView
)

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-detail'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('user-projects/', UserProjectsView.as_view(), name='user-projects'),
]