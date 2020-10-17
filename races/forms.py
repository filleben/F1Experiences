from django import forms
from .models import Race, Ticket

class RaceForm(forms.ModelForm):

    class Meta:
        model = Race
        fields = '__all__'

class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        race = Race.objects.all()
        friendly_names = [(r.id, r.get_friendly_name()) for r in race]

        self.fields['race'].choices = friendly_names