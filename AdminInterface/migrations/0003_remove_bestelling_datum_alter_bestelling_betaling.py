# Generated by Django 5.0.6 on 2024-06-03 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminInterface', '0002_bestelling_besteldatum_bestelling_betaling_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bestelling',
            name='Datum',
        ),
        migrations.AlterField(
            model_name='bestelling',
            name='Betaling',
            field=models.CharField(max_length=50),
        ),
    ]
