from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact Form
    """
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'contact_email', 'contact_phone',
                  'subject', 'message',)
