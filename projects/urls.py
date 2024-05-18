from django.urls import path

from .views import *


app_name = 'projects'

urlpatterns = [
    path('', projects, name='projects'),
    path('<int:id>/', project, name='project'),
    path('list/', ProjectsView.as_view(), name='projects_list'),
]
