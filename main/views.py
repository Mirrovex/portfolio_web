from django.shortcuts import render


def home(request):
    return render(request, "home.html", {'active_tab': 'home'})


def about(request):
    return render(request, "about.html", {'active_tab': 'about'})


def contact(request):
    return render(request, "contact.html", {'active_tab': 'contact'})