from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage

from projects.models import Tag
from .models import Settings
from .forms import ContactForm


def home(request):
    settings = Settings.objects.first()
    return render(request, "home.html", {'active_tab': 'home', 'settings': settings})


def about(request):
    settings = Settings.objects.first()
    tags = Tag.objects.all()
    return render(request, "about.html", {'active_tab': 'about', 'settings': settings, 'tags': tags})


def contact(request):
    settings = Settings.objects.first()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                email_message = EmailMessage(
                    f"{subject}",
                    f"{name} | {email}\n\n{message}",
                    "mirrovex@wp.pl",  # send from
                    ["mirrovex@wp.pl"],  # send to
                    reply_to=[email]
                )
                email_message.send(fail_silently=False)


                messages.success(request, "Wysłano wiadomość")
                return redirect("contact")
            except Exception as e:
                print(e)
        messages.error(request, "Twój formularz ma błędy")
        return render(request, "contact.html", {'active_tab': 'contact', 'settings': settings, 'form': form})
    else:
        form = ContactForm()
        return render(request, "contact.html", {'active_tab': 'contact', 'settings': settings, 'form': form})