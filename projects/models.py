from django.db import models
import os
from django.templatetags.static import static


class Tag(models.Model):

    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='tag_icons/', blank=True)
    style = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    
    def get_image_url(self):
        if self.icon and os.path.exists(self.icon.path):
            return self.icon.url
        else:
            return static('icons/no-image.png')


class Project(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    github = models.URLField(max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    
    def get_image_url(self):
        first_image = self.images.first()
        if first_image and first_image.image and os.path.exists(first_image.image.path):
            return first_image.image.url
        else:
            return static('icons/no-image.png')


class ProjectImage(models.Model):
    
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="projects_images/")

    def __str__(self) -> str:
        return f"{self.project.title} Image"
