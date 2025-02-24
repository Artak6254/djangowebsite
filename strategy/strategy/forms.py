from django import forms
from .models import ContactForm

class ContactUser(forms.ModelForm):
    class Meta:
        model = ContactForm  
        fields = ['username', 'user_email', 'user_message'] 