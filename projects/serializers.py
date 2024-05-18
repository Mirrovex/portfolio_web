from .models import Project
from rest_framework import serializers
from django.urls import reverse


class ProjectsSerializer(serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField()
    project_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['title', 'description', 'image_url', 'project_url', 'tags']

    def get_image_url(self, obj):
        return obj.get_image_url()
    
    def get_project_url(self, obj):
        return reverse('projects:project', args=[obj.id])
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['tags'] = [tag.name for tag in instance.tags.all()]
        return representation