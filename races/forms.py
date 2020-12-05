from django import forms
from .widgets import CustomClearableFileInput
from .models import Race, Ticket

#Race Form
class RaceForm(forms.ModelForm):
    """
    Image and flag field set to custom file input
    """
    class Meta:
        model = Race
        fields = '__all__'

    image = forms.ImageField(label='Circuit Map:', required=False, widget=CustomClearableFileInput)
    flag = forms.ImageField(label='Flag:', required=False, widget=CustomClearableFileInput)

#Ticket Form
class TicketForm(forms.ModelForm):
    """
    Uses the friendly name field from races model as a drop down menu
    """
    class Meta:
        model = Ticket
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        race = Race.objects.all()
        friendly_names = [(r.id, r.get_friendly_name()) for r in race]

        self.fields['race'].choices = friendly_names