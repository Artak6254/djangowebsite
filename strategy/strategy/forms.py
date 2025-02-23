from django import forms
from .models import ContactForm


class ContactUser(forms.ModelForm):
    model = ContactForm
    field = ['name', 'email', 'message']