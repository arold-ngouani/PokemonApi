# Generated by Django 3.2.12 on 2022-03-11 16:07
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pokemon",
            old_name="nickname",
            new_name="nickname",
        ),
    ]