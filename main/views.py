from django.shortcuts import render

from .models import Settings


def home(request):
    pages = Settings.objects.first().pages.all()
    return render(request, "home.html", {'active_tab': 'home', 'pages': pages})


def about(request):
    pages = Settings.objects.first().pages.all()
    return render(request, "about.html", {'active_tab': 'about', 'pages': pages})


def contact(request):
    pages = Settings.objects.first().pages.all()
    return render(request, "contact.html", {'active_tab': 'contact', 'pages': pages})