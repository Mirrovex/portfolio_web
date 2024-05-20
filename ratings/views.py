from django.shortcuts import render

from main.models import Settings

def ratings(request):
    pages = Settings.objects.first().pages.all()
    return render(request, 'ratings.html', {'active_tab': 'ratings', 'pages': pages})