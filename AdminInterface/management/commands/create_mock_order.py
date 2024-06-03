# create_mock_order.py

from django.core.management.base import BaseCommand
from AdminInterface.models import Bestelling, Klant, Product, Categorie
from datetime import datetime

class Command(BaseCommand):
    help = 'Maak een mock bestelling aan voor testdoeleinden'

    def handle(self, *args, **kwargs):
        # Maak mock data aan indien niet aanwezig
        if not Categorie.objects.exists():
            categorie = Categorie.objects.create(Productnaam="Electronics")
        else:
            categorie = Categorie.objects.first()
        
        if not Product.objects.exists():
            product = Product.objects.create(
                Naam="Mock Product",
                EAN="123456789",
                Omschrijving="Dit is een mock product.",
                Prijs=100,
                Categorie=categorie,
                Image="uploads/product/mock_product.jpg",
                Korting=False,
                Korting_prijs=0,
            )
        else:
            product = Product.objects.first()

        if not Klant.objects.exists():
            klant = Klant.objects.create(
                Voornaam="Mock",
                Achternaam="Customer",
                Bedrijf="Mock Inc.",
                Facturatieadres="1234 Mock St.",
                Adres="1234 Mock St.",
                Telefoonnummer="123-456-7890",
                Email="mock@customer.com",
                Wachtwoord="mockpassword"
            )
        else:
            klant = Klant.objects.first()

        Bestelling.objects.create(
            Product=product,
            Klant=klant,
            Hoeveelheid=1,
            Adres="1234 Mock St.",
            Telefoonnummer="123-456-7890",
            Besteldatum=datetime.now(),
            Gewijzigde_datum=datetime.now(),
            Status=False,
            Betaling="Not Paid",
            Totaal=100,
            Voorschot=0
        )

        self.stdout.write(self.style.SUCCESS('Mock bestelling succesvol aangemaakt'))
