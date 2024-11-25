from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='created_clients')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='projects')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='created_projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name