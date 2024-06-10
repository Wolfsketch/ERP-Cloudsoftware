"""
models.py: Dit definieert de database-structuur, oftewel de modellen die worden gebruikt om de gegevens op te slaan. Dit is essentieel voor het opzetten van de database tabellen.

STAP 1 MAAK EEN DATABASE MODEL AAN (VOOR HET OPSLAAN VAN GEGEVENS)
"""

from django.db import models
import datetime

class Categorie(models.Model):
    Productnaam = models.CharField(max_length=50)

    def __str__(self):
        return self.Productnaam

class Klant(models.Model):
    Voornaam = models.CharField(max_length=50)
    Achternaam = models.CharField(max_length=50)
    Bedrijf = models.CharField(max_length=50)
    Facturatieadres = models.CharField(max_length=250)
    Adres = models.CharField(max_length=250)
    Telefoonnummer = models.CharField(max_length=18)
    Email = models.EmailField(max_length=100)
    Wachtwoord = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.Voornaam} {self.Achternaam}'

class Product(models.Model):
    naam = models.CharField(max_length=100)
    ean = models.CharField(max_length=50)
    omschrijving = models.CharField(max_length=250, default='', blank=True, null=True)
    prijs = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/product/')
    korting = models.BooleanField(default=False)
    korting_prijs = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.naam

class BestellingProduct(models.Model):
    bestelling = models.ForeignKey('Bestelling', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    omschrijving = models.CharField(max_length=250, blank=True, null=True)
    hoeveelheid = models.IntegerField(default=1)
    eenheidsprijs = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    belastingen = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def subtotaal(self):
        return self.hoeveelheid * self.eenheidsprijs

class Bestelling(models.Model):
    STATUS_CHOICES = [
        ('ordered', 'Product besteld bij de fabrikant'),
        ('arrived', 'Product aangekomen in het magazijn'),
        ('ready_for_delivery', 'Product aangemeld voor levering'),
        ('shipped', 'Product verstuurd'),
    ]

    klant = models.ForeignKey(Klant, on_delete=models.CASCADE)
    besteldatum = models.DateField(default=datetime.datetime.today)
    voorschot = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    totaal = models.DecimalField(default=0, decimal_places=2, max_digits=10, blank=True, null=True)
    betaling = models.CharField(max_length=50, default='', blank=True)
    producten = models.ManyToManyField(Product, through='BestellingProduct', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ordered')
    adres = models.CharField(max_length=250, default='', blank=True)

    def __str__(self):
        return f'Bestelling {self.id} voor {self.klant}'
