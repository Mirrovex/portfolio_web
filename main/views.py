from django.shortcuts import render

from .models import Settings


def home(request):
    settings = Settings.objects.first()
    return render(request, "home.html", {'active_tab': 'home', 'settings': settings})


def about(request):
    settings = Settings.objects.first()
    return render(request, "about.html", {'active_tab': 'about', 'settings': settings})


def contact(request):
    settings = Settings.objects.first()
    return render(request, "contact.html", {'active_tab': 'contact', 'settings': settings})