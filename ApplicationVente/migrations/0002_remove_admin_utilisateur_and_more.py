# Generated by Django 5.0.4 on 2024-04-09 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ApplicationVente", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="admin",
            name="utilisateur",
        ),
        migrations.RemoveField(
            model_name="consommateur",
            name="utilisateur",
        ),
        migrations.RemoveField(
            model_name="visiteur",
            name="adresse",
        ),
    ]
