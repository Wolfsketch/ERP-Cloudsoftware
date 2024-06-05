from django import forms
from .models import Bestelling, BestellingProduct, Product

class BestellingProductForm(forms.ModelForm):
    class Meta:
        model = BestellingProduct
        fields = ['product', 'omschrijving', 'hoeveelheid', 'eenheidsprijs', 'belastingen']
        widgets = {
            'product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Begin met typen om een product te zoeken...'}),
            'omschrijving': forms.TextInput(attrs={'class': 'form-control'}),
            'hoeveelheid': forms.NumberInput(attrs={'class': 'form-control'}),
            'eenheidsprijs': forms.NumberInput(attrs={'class': 'form-control'}),
            'belastingen': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class BestellingForm(forms.ModelForm):
    class Meta:
        model = Bestelling
        fields = ['klant_naam', 'klant_bedrijf', 'email', 'telefoon', 'facturatieadres', 'afleveradres', 'besteldatum', 'voorschot', 'totaal', 'betaling', 'status']
        widgets = {
            'klant_naam': forms.TextInput(attrs={'class': 'form-control'}),
            'klant_bedrijf': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefoon': forms.TextInput(attrs={'class': 'form-control'}),
            'facturatieadres': forms.TextInput(attrs={'class': 'form-control'}),
            'afleveradres': forms.TextInput(attrs={'class': 'form-control'}),
            'besteldatum': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'voorschot': forms.NumberInput(attrs={'class': 'form-control'}),
            'totaal': forms.NumberInput(attrs={'class': 'form-control'}),
            'betaling': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(choices=Bestelling.STATUS_CHOICES, attrs={'class': 'form-control'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['naam', 'ean', 'omschrijving', 'prijs', 'categorie', 'image', 'korting', 'korting_prijs']

BestellingProductFormSet = forms.inlineformset_factory(
    Bestelling, Bestelling.producten.through,
    form=BestellingProductForm,
    extra=1,
    widgets={
        'product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Begin met typen om een product te zoeken...'}),
        'omschrijving': forms.TextInput(attrs={'class': 'form-control'}),
        'hoeveelheid': forms.NumberInput(attrs={'class': 'form-control'}),
        'eenheidsprijs': forms.NumberInput(attrs={'class': 'form-control'}),
        'belastingen': forms.NumberInput(attrs={'class': 'form-control'}),
    }
)
