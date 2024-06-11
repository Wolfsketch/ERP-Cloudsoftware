"""
views.py: Dit maakt het mogelijk om de logica van de applicatie te definiëren. Het bevat de views die de gebruiker ziet en de acties die de gebruiker kan uitvoeren. Dit is de plek waar de gegevens worden opgehaald, verwerkt en weergegeven.

STAP 3 MAAK EEN VIEW AAN (VOOR HET VERWERKEN VAN DE GEBRUIKERSINVOER)
"""
from django.shortcuts import render, redirect, get_object_or_404
from .forms import KlantForm, BestellingForm, BestellingProductFormSet, ProductForm, SimpleTestForm
from .models import Klant, Bestelling, BestellingProduct, Product
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
import logging

# Stel de logger in
logger = logging.getLogger(__name__)

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def bestellingen(request):
    bestellingen_lijst = Bestelling.objects.all()
    debug_info = []
    for bestelling in bestellingen_lijst:
        debug_info.append(f"Bestelling ID: {bestelling.id}, Klant: {bestelling.klant.voornaam} {bestelling.klant.achternaam}, Totaal: {bestelling.totaal}")
    
    return render(request, 'bestellingen.html', {'bestellingen': bestellingen_lijst, 'debug_info': debug_info})

@login_required
def klanten(request):
    klanten = Klant.objects.all()
    return render(request, 'klanten.html', {'klanten': klanten})


@login_required
def bestelling_detail(request, pk):
    bestelling = get_object_or_404(Bestelling, pk=pk)
    return render(request, 'bestelling_detail.html', {'bestelling': bestelling})

@login_required
def bestelling_bewerk(request, pk):
    bestelling = get_object_or_404(Bestelling, pk=pk)
    if request.method == 'POST':
        form = BestellingForm(request.POST, instance=bestelling)
        if form.is_valid():
            form.save()
            return redirect('bestelling_detail', pk=bestelling.pk)
    else:
        form = BestellingForm(instance=bestelling)
    return render(request, 'bestelling_bewerken.html', {'form': form, 'bestelling': bestelling})


@login_required
def bestelling_verwijder(request, pk):
    bestelling = get_object_or_404(Bestelling, pk=pk)
    if request.method == 'POST':
        bestelling.delete()
        return redirect('bestellingen')
    return render(request, 'bestelling_verwijderen.html', {'bestelling': bestelling})


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
    if request.method == 'POST':
        klant_form = KlantForm(request.POST)
        bestelling_form = BestellingForm(request.POST)
        formset = BestellingProductFormSet(request.POST)

        if klant_form.is_valid() and bestelling_form.is_valid() and formset.is_valid():
            klant = klant_form.save()
            bestelling = bestelling_form.save(commit=False)
            bestelling.klant = klant
            bestelling.save()

            for form in formset:
                if form.cleaned_data:
                    bestelling_product = form.save(commit=False)
                    bestelling_product.bestelling = bestelling
                    bestelling_product.save()

            return redirect('bestellingen')
        else:
            logger.debug('Klant form errors: %s', klant_form.errors)
            logger.debug('Bestelling form errors: %s', bestelling_form.errors)
            logger.debug('Formset errors: %s', formset.errors)
    else:
        klant_form = KlantForm()
        bestelling_form = BestellingForm()
        formset = BestellingProductFormSet(queryset=BestellingProduct.objects.none())

    return render(request, 'bestelling_create_manual.html', {
        'klant_form': klant_form,
        'bestelling_form': bestelling_form,
        'formset': formset
    })



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
    

def simple_test_view(request):
    if request.method == 'POST':
        form = SimpleTestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('simple_test_success')
    else:
        form = SimpleTestForm()
    return render(request, 'simple_test_form.html', {'form': form})

def simple_test_success(request):
    return render(request, 'simple_test_success.html')