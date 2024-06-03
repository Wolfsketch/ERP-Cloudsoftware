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