from projects.models import Project
from rest_framework import viewsets, permissions
from projects.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer