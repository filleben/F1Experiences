from django import forms
from .models import Contact

#Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'contact_email', 'contact_phone', 'subject', 'message',)
