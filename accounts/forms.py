from django import forms
from .models import UserProfile

#User Profile Form
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        labels = {
            'default_phone_number': 'Phone Number',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County/State',
            'default_country': 'Country',
        }