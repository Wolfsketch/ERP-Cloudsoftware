from django import forms
from .models import Bestelling, BestellingProduct, Product

class BestellingForm(forms.ModelForm):
    class Meta:
        model = Bestelling
        fields = ['klant_naam', 'klant_bedrijf', 'email', 'telefoon', 'facturatieadres', 'afleveradres', 'besteldatum', 'voorschot', 'totaal', 'betaling', 'status']
        widgets = {
            'klant_naam': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Naam'}),
            'klant_bedrijf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bedrijfnaam'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telefoon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefoon'}),
            'facturatieadres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Facturatieadres'}),
            'afleveradres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Afleveradres'}),
            'besteldatum': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'voorschot': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0.00 €'}),
            'totaal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0.00 €'}),
            'betaling': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Betaling'}),
            'status': forms.Select(choices=Bestelling.STATUS_CHOICES, attrs={'class': 'form-control'}),
        }
    initial = {
        'voorschot': '',
        'totaal': ''
    }
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
            'product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Begin met typen om een product te zoeken...'}),
            'omschrijving': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Omschrijving'}),
            'hoeveelheid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Hoeveelheid'}),
            'eenheidsprijs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Eenheidsprijs'}),
            'belastingen': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Belastingen'}),
        }

BestellingProductFormSet = forms.inlineformset_factory(
    Bestelling,
    BestellingProduct,
    form=BestellingProductForm,
    extra=1,
    can_delete=True,
    widgets={
        'product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Begin met typen om een product te zoeken...'}),
        'omschrijving': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Omschrijving'}),
        'hoeveelheid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Hoeveelheid'}),
        'eenheidsprijs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Eenheidsprijs'}),
        'belastingen': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Belastingen'}),
    }
)
