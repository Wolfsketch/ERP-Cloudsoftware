from django.shortcuts import render, get_object_or_404, redirect
from .models import Bestelling, Product, BestellingProduct
from .Forms import BestellingForm, BestellingProductForm
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import JsonResponse
from .Forms import ProductForm, BestellingForm, BestellingProductForm, BestellingProductFormSet
from django.db.models import Q
from .models import Product


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def bestellingen(request):
    bestellingen_lijst = Bestelling.objects.all()
    return render(request, 'bestellingen.html', {'bestellingen': bestellingen_lijst})

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
        form = BestellingForm(request.POST, instance=bestelling)
        if form.is_valid():
            form.save()
            return redirect('bestelling_detail', pk=bestelling.pk)
    else:
        form = BestellingForm(instance=bestelling)
    return render(request, 'bestelling_bewerk.html', {'form': form})

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
def create_bestelling(request):
    if request.method == 'POST':
        form = BestellingForm(request.POST)
        formset = BestellingProductFormSet(request.POST, instance=form.instance)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('some_view_name')  # Pas aan naar de gewenste view naam
    else:
        form = BestellingForm()
        formset = BestellingProductFormSet(instance=Bestelling())

    return render(request, 'bestelling_create_manual.html', {'form': form, 'formset': formset})

@login_required
def bestelling_create_manual(request):
    BestellingProductFormSet = modelformset_factory(BestellingProduct, form=BestellingProductForm, extra=1, can_delete=True)
    
    if request.method == 'POST':
        form = BestellingForm(request.POST)
        formset = BestellingProductFormSet(request.POST, queryset=BestellingProduct.objects.none())
        
        if form.is_valid() and formset.is_valid():
            bestelling = form.save()
            for form in formset:
                bestelling_product = form.save(commit=False)
                bestelling_product.bestelling = bestelling
                bestelling_product.save()
            return redirect('bestellingen')
    else:
        form = BestellingForm()
        formset = BestellingProductFormSet(queryset=BestellingProduct.objects.none())
    
    return render(request, 'bestelling_create_manual.html', {'form': form, 'formset': formset})

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