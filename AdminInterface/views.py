from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Bestelling
from django.core.mail import send_mail
from .models import Bestelling
from .Forms import BestellingForm

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

def bestelling_detail(request, id):
    bestelling = get_object_or_404(Bestelling, id=id)
    return render(request, 'bestelling_detail.html', {'bestelling': bestelling})

def bestelling_bewerk(request, id):
    bestelling = get_object_or_404(Bestelling, id=id)
    if request.method == 'POST':
        form = BestellingForm(request.POST, instance=bestelling)
        if form.is_valid():
            form.save()
            return redirect('bestellingen')
    else:
        form = BestellingForm(instance=bestelling)
    return render(request, 'bestelling_bewerk.html', {'form': form})

def bestelling_verwijder(request, id):
    bestelling = get_object_or_404(Bestelling, id=id)
    if request.method == 'POST':
        bestelling.delete()
        return redirect('bestellingen')
    return render(request, 'bestelling_verwijder.html', {'bestelling': bestelling})

def bestelling_mail(request, id):
    bestelling = get_object_or_404(Bestelling, id=id)
    # Voeg je logica toe om een e-mail te sturen
    return redirect('bestellingen')