from django.urls import path

from .views import *


app_name = 'ratings'

urlpatterns = [
    path('', ratings, name='ratings'),
]

