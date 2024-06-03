# forms.py

from django import forms
from .models import Bestelling

class BestellingForm(forms.ModelForm):
    class Meta:
        model = Bestelling
        fields = ['Product', 'Klant', 'Hoeveelheid', 'Adres', 'Telefoonnummer', 'Betaling', 'Totaal', 'Voorschot', 'Besteldatum', 'Status']
