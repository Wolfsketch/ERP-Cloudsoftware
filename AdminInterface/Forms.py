from django import forms
from .models import Bestelling, BestellingProduct, Klant, Product, SimpleTest
from django.forms.models import inlineformset_factory

class KlantForm(forms.ModelForm):
    class Meta:
        model = Klant
        fields = ['voornaam', 'achternaam', 'bedrijf', 'facturatieadres', 'adres', 'telefoonnummer', 'email']
        widgets = {
            'voornaam': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Voornaam', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
            'achternaam': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Achternaam', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
            'bedrijf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bedrijf', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
            'facturatieadres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Facturatieadres', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
            'adres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Afleveradres', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
            'telefoonnummer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefoonnummer', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
        }

class BestellingForm(forms.ModelForm):
    class Meta:
        model = Bestelling
        fields = ['besteldatum', 'voorschot', 'totaal', 'betaling', 'status', 'adres']
        widgets = {
            'besteldatum': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
            'voorschot': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00 €', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
            'totaal': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00 €', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
            'betaling': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Betaling', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
            'status': forms.Select(attrs={'class': 'form-control', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
            'adres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Afleveradres', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
        }

class BestellingProductForm(forms.ModelForm):
    class Meta:
        model = BestellingProduct
        fields = ['product', 'omschrijving', 'hoeveelheid', 'eenheidsprijs', 'belastingen']
        widgets = {
            'product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Begin met typen om een product te zoeken...', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
            'omschrijving': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Omschrijving', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
            'hoeveelheid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Hoeveelheid', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
            'eenheidsprijs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Eenheidsprijs', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
            'belastingen': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Belastingen', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
        }

BestellingProductFormSet = inlineformset_factory(
    Bestelling,
    BestellingProduct,
    form=BestellingProductForm,
    extra=1,
    can_delete=True,
)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['naam', 'ean', 'omschrijving', 'prijs', 'categorie', 'image', 'korting', 'korting_prijs']
        widgets = {
            'naam': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Naam'}),
            'ean': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'EAN'}),
            'omschrijving': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Omschrijving'}),
            'prijs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prijs'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'korting': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'korting_prijs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Korting Prijs'}),
        }

class SimpleTestForm(forms.ModelForm):
    class Meta:
        model = SimpleTest
        fields = ['name', 'description']