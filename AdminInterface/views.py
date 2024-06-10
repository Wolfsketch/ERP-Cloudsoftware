from django.shortcuts import render, get_object_or_404, redirect
from .models import Bestelling, Product, BestellingProduct, Klant
from .Forms import ProductForm, BestellingProductForm, CombinedBestellingForm, BestellingProductFormSet
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.db.models import Q
from django.db.models import Q
from django.http import JsonResponse
import logging

# Stel de logger in
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def bestellingen(request):
    bestellingen_lijst = Bestelling.objects.all()
    debug_info = []
    for bestelling in bestellingen_lijst:
        debug_info.append(f"Bestelling ID: {bestelling.id}, Klant: {bestelling.klant.Voornaam} {bestelling.klant.Achternaam}, Totaal: {bestelling.totaal}")
    
    return render(request, 'bestellingen.html', {'bestellingen': bestellingen_lijst, 'debug_info': debug_info})

@login_required
def klanten(request):
    return render(request, 'klanten.html')

@login_required
def bestelling_detail(request, pk):
    bestelling = get_object_or_404(Bestelling, pk=pk)
    return render(request, 'bestelling_detail.html', {'bestelling': bestelling})

@login_required
def bestelling_bewerk(request, pk):
    bestelling = get_object_or_404(Bestelling, pk=pk)
    if request.method == 'POST':
        combined_form = CombinedBestellingForm(request.POST, instance=bestelling)
        if combined_form.is_valid():
            combined_form.save()
            return redirect('bestelling_detail', pk=bestelling.pk)
    else:
        combined_form = CombinedBestellingForm(instance=bestelling)
    return render(request, 'bestelling_bewerk.html', {'combined_form': combined_form})

@login_required
def bestelling_verwijder(request, pk):
    bestelling = get_object_or_404(Bestelling, pk=pk)
    if request.method == 'POST':
        bestelling.delete()
        return redirect('bestellingen')
    return render(request, 'bestelling_verwijder.html', {'bestelling': bestelling})

@login_required
def bestelling_mail(request, pk):
    bestelling = get_object_or_404(Bestelling, pk=pk)
    # Voeg hier je mail-verzendcode toe
    return render(request, 'bestelling_mail.html', {'bestelling': bestelling})

@login_required
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

@login_required
def bestelling_create_manual(request):
    BestellingProductFormSet = modelformset_factory(BestellingProduct, form=BestellingProductForm, extra=1, can_delete=True)
    
    if request.method == 'POST':
        combined_form = CombinedBestellingForm(request.POST)
        formset = BestellingProductFormSet(request.POST, queryset=BestellingProduct.objects.none())

        print(f"POST data: {request.POST}")
        
        if combined_form.is_valid() and formset.is_valid():
            # Klant opslaan
            klant_data = {
                'Voornaam': combined_form.cleaned_data['klant_voornaam'],
                'Achternaam': combined_form.cleaned_data['klant_achternaam'],
                'Bedrijf': combined_form.cleaned_data['klant_bedrijf'],
                'Facturatieadres': combined_form.cleaned_data['klant_facturatieadres'],
                'Adres': combined_form.cleaned_data['klant_adres'],
                'Telefoonnummer': combined_form.cleaned_data['klant_telefoonnummer'],
                'Email': combined_form.cleaned_data['klant_email'],
            }
            print(f"Klant data: {klant_data}")
            klant, created = Klant.objects.get_or_create(**klant_data)

            # Bereken het totaalbedrag
            totaal_bedrag = 0
            for form in formset:
                if form.cleaned_data:
                    hoeveelheid = form.cleaned_data.get('hoeveelheid', 0)
                    eenheidsprijs = form.cleaned_data.get('eenheidsprijs', 0)
                    totaal_bedrag += hoeveelheid * eenheidsprijs

            # Bestelling opslaan
            bestelling_data = {
                'klant': klant,
                'besteldatum': combined_form.cleaned_data['besteldatum'],
                'voorschot': combined_form.cleaned_data['voorschot'],
                'totaal': totaal_bedrag,
                'betaling': combined_form.cleaned_data['betaling'],
                'status': combined_form.cleaned_data['status'],
            }
            print(f"Bestelling data: {bestelling_data}")
            bestelling = Bestelling.objects.create(**bestelling_data)

            # BestellingProduct opslaan
            for form in formset:
                if form.cleaned_data:
                    bestelling_product = form.save(commit=False)
                    bestelling_product.bestelling = bestelling
                    bestelling_product.save()

            return redirect('bestellingen')
        else:
            print(f"Combined form errors: {combined_form.errors}")
            print(f"Formset errors: {formset.errors}")
    else:
        combined_form = CombinedBestellingForm()
        formset = BestellingProductFormSet(queryset=BestellingProduct.objects.none())

    return render(request, 'bestelling_create_manual.html', {'combined_form': combined_form, 'formset': formset})





@login_required
def bestelling_create_manual(request):
    BestellingProductFormSet = modelformset_factory(BestellingProduct, form=BestellingProductForm, extra=1, can_delete=True)
    
    if request.method == 'POST':
        combined_form = CombinedBestellingForm(request.POST)
        formset = BestellingProductFormSet(request.POST, queryset=BestellingProduct.objects.none())
        
        if combined_form.is_valid() and formset.is_valid():
            # Debug: Print combined_form cleaned data
            print("Combined form is valid. Cleaned data:", combined_form.cleaned_data)
            
            # Klant opslaan
            klant_data = {
                'Voornaam': combined_form.cleaned_data['klant_voornaam'],
                'Achternaam': combined_form.cleaned_data['klant_achternaam'],
                'Bedrijf': combined_form.cleaned_data['klant_bedrijf'],
                'Facturatieadres': combined_form.cleaned_data['klant_facturatieadres'],
                'Adres': combined_form.cleaned_data['klant_adres'],
                'Telefoonnummer': combined_form.cleaned_data['klant_telefoonnummer'],
                'Email': combined_form.cleaned_data['klant_email'],
            }
            klant, created = Klant.objects.get_or_create(**klant_data)
            print("Klant opgeslagen:", klant)
            
            # Bereken het totaalbedrag
            totaal_bedrag = 0
            for form in formset:
                if form.cleaned_data:
                    hoeveelheid = form.cleaned_data.get('hoeveelheid', 0)
                    eenheidsprijs = form.cleaned_data.get('eenheidsprijs', 0)
                    totaal_bedrag += hoeveelheid * eenheidsprijs
            print("Totaal bedrag berekend:", totaal_bedrag)
            
            # Bestelling opslaan
            bestelling_data = {
                'klant': klant,
                'besteldatum': combined_form.cleaned_data['besteldatum'],
                'voorschot': combined_form.cleaned_data['voorschot'],
                'totaal': totaal_bedrag,
                'betaling': combined_form.cleaned_data['betaling'],
                'status': combined_form.cleaned_data['status'],
            }
            bestelling = Bestelling.objects.create(**bestelling_data)
            print("Bestelling opgeslagen:", bestelling)
            
            # BestellingProduct opslaan
            for form in formset:
                if form.cleaned_data:
                    bestelling_product = form.save(commit=False)
                    bestelling_product.bestelling = bestelling
                    bestelling_product.save()
                    print("BestellingProduct opgeslagen:", bestelling_product)

            return redirect('bestellingen')
        else:
            # Debug: Print form errors if any form is invalid
            print("Combined form errors:", combined_form.errors)
            print("Formset errors:", formset.errors)
    else:
        combined_form = CombinedBestellingForm()
        formset = BestellingProductFormSet(queryset=BestellingProduct.objects.none())

    return render(request, 'bestelling_create_manual.html', {'combined_form': combined_form, 'formset': formset})



@login_required
def product_list(request):
    producten = Product.objects.all()
    return render(request, 'producten.html', {'producten': producten})

@login_required
def product_autocomplete(request):
    if 'term' in request.GET:
        qs = Product.objects.filter(
            Q(naam__icontains=request.GET.get('term')) |
            Q(ean__icontains=request.GET.get('term'))
        )
        products = list()
        for product in qs:
            products.append({
                'id': product.id,
                'label': f"{product.naam} ({product.ean})",
                'value': product.naam,
            })
        return JsonResponse(products, safe=False)
    return JsonResponse([], safe=False)
    