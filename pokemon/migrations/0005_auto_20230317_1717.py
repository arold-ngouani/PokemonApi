# Generated by Django 3.2.12 on 2023-03-17 16:17
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_object", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pokemon", "0004_pokemon_pokemon_object"),
    ]

    operations = [
        migrations.CreateModel(
            name="PokemonTeam",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100)),
                (
                    "trainer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Trainer pokemon's team",
                "ordering": ["name"],
            },
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="pokemon_object",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="pokemon_object.pokemonpreferredobject",
            ),
        ),
        migrations.DeleteModel(
            name="PokemonPreferredObject",
        ),
        migrations.AddField(
            model_name="pokemon",
            name="pokemon_team",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="pokemon.pokemonteam",
            ),
        ),
    ]