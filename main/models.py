from django.db import models


class Page(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    reverse_url = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self) -> str:
        return self.name
    
    def get_url(self):
        return self.reverse_url + self.slug


class Settings(models.Model):
    name = models.CharField(max_length=100, unique=True)
    pages = models.ManyToManyField(Page)
    page_title = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return self.name
