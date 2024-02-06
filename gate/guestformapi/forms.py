from django import forms
from .models import GuestForm

class GuestFormForm(forms.ModelForm):
    class Meta:
        model = GuestForm
        fields = ["name", "entering", "roll_id", "contact", "address", "purpose", "notes"]
