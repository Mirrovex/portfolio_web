from django.shortcuts import render

from main.models import Settings

def ratings(request):
    settings = Settings.objects.first()
    return render(request, 'ratings.html', {'active_tab': 'ratings', 'settings': settings})