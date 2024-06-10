"""
forms.py: Dit maakt het mogelijk om formulieren te genereren op basis van de modellen. Het zorgt ervoor dat de invoer van de gebruiker wordt gevalideerd en opgeslagen in de juiste modelvelden.

STAP 2 MAAK EEN FORMULIER AAN (VOOR HET WEERGEVEN VAN DE PAGINA)
"""


from django import forms
from .models import Bestelling, BestellingProduct, Product

class CombinedBestellingForm(forms.Form):
    klant_voornaam = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Voornaam', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}))
    klant_achternaam = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Achternaam', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}))
    klant_bedrijf = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bedrijf', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}))
    klant_facturatieadres = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Facturatieadres', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}))
    klant_adres = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Afleveradres', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}))
    klant_telefoonnummer = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefoonnummer', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}))
    klant_email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}))

    besteldatum = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}))
    voorschot = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00 €', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}))
    totaal = forms.DecimalField(max_digits=10, decimal_places=2, required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00 €', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}))
    betaling = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Betaling', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}))
    status = forms.ChoiceField(choices=Bestelling.STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}))

    class Meta:
        model = Bestelling
        fields = [
            'klant_voornaam', 'klant_achternaam', 'klant_bedrijf', 'klant_facturatieadres', 'klant_adres', 'klant_telefoonnummer', 'klant_email',
            'besteldatum', 'voorschot', 'totaal', 'betaling', 'status'
        ]

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

BestellingProductFormSet = forms.inlineformset_factory(
    Bestelling,
    BestellingProduct,
    form=BestellingProductForm,
    extra=1,
    can_delete=True,
    widgets={
        'product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Begin met typen om een product te zoeken...', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
        'omschrijving': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Omschrijving', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
        'hoeveelheid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Hoeveelheid', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
        'eenheidsprijs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Eenheidsprijs', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
        'belastingen': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Belastingen', 'style': 'border-width: 0 0 1px 0; border-radius: 0;'}),
    }
)