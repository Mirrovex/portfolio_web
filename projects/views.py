from django.shortcuts import render, get_object_or_404
from rest_framework import generics

from .models import Project, Tag
from main.models import Settings
from .serializers import ProjectsSerializer
from .pagination import ProjectPagination


def projects(request):
    pages = Settings.objects.first().pages.all()
    projects = Project.objects.filter(show=True)
    tags = Tag.objects.all()

    return render(request, "projects.html", {'active_tab': 'projects', 'pages': pages, 'projects': projects, 'tags': tags})


def project(request, id):
    pages = Settings.objects.first().pages.all()
    project = get_object_or_404(Project, id=id)
    return render(request, "project.html", {'active_tab': 'projects', 'pages': pages, 'project': project})


class ProjectsView(generics.ListAPIView):

    serializer_class = ProjectsSerializer
    pagination_class = ProjectPagination

    def get_queryset(self):
        tag = self.request.query_params.get('tag', None)
        name = self.request.query_params.get('name', None)
        queryset = Project.objects.filter(show=True)
        if tag:
            queryset = queryset.filter(tags__name__icontains=tag)
        if name:
            queryset = queryset.filter(title__icontains=name)
        return queryset

