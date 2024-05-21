from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(
        required=True, 
        max_length=100, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "Imię", "class": "form-control"}), 
        label="",
        error_messages={
            'required': 'Proszę podać imię',
            'max_length': 'Imię nie może mieć więcej niż 100 znaków'
        }
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class": "form-control"}), 
        label="",
        error_messages={
            'required': 'Proszę podać email',
            'invalid': 'Niepoprawny adres email'
        }
    )
    subject = forms.CharField(
        required=True, 
        max_length=100, 
        widget=forms.widgets.TextInput(attrs={"placeholder": "Temat", "class": "form-control"}), 
        label="",
        error_messages={
            'required': 'Proszę podać temat',
            'max_length': 'Temat nie może mieć więcej niż 100 znaków'
        }
    )
    message = forms.CharField(
        required=True, 
        widget=forms.widgets.Textarea(attrs={
            "placeholder": "Wiadomość",
            "class": "form-control",
            "rows": 5,
            "cols": 40,
            "style": "resize: none;"
            }), 
        label="",
        error_messages={
            'required': 'Proszę napisać wiadomość'
        }
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                field.widget.attrs['class'] += ' is-invalid'