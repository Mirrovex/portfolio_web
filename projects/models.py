from django.db import models
import os
from django.templatetags.static import static


class Tag(models.Model):

    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='tag_icons/', blank=True)
    icon_url = models.URLField(max_length=200, blank=True)
    style = models.TextField(blank=True, null=True)
    show_projects = models.BooleanField(default=True)
    show_about = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
    
    def __str__(self) -> str:
        return self.name
    
    def get_image_url(self):
        if self.icon and os.path.exists(self.icon.path):
            try:
                self.icon.read()
                return self.icon.url
            except:
                print("error reading icon")
        if self.icon_url:
            return self.icon_url
        else:
            return False


class Project(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    github = models.URLField(max_length=200, blank=True)
    website = models.URLField(max_length=200, blank=True)
    show = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
    
    def get_image_url(self):
        first_image = self.images.first()
        if first_image:
            return first_image.get_image_url()
        else:
            return static('icons/no-image.png')


class ProjectImage(models.Model):
    
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="projects_images/", blank=True)
    image_url = models.URLField(max_length=200, blank=True)

    def __str__(self) -> str:
        return f"{self.project.title} Image"
    
    def get_image_url(self):
        if self.image and os.path.exists(self.image.path):
            try:
                self.image.read()
                return self.image.url
            except:
                print("error reading image")
        if self.image_url:
            return self.image_url
        else:
            return static('icons/no-image.png')
