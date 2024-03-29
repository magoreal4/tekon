# Generated by Django 4.2.8 on 2023-12-18 01:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_sitios_remove_homepage_imgbanner_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitios",
            name="altura",
            field=models.IntegerField(
                choices=[("24", 24), ("42", 42), ("48", 48)],
                default=42,
                verbose_name="Altura Torre",
            ),
        ),
        migrations.AddField(
            model_name="sitios",
            name="cod",
            field=models.CharField(
                max_length=10, null=True, verbose_name="Codigo Sitio"
            ),
        ),
        migrations.AddField(
            model_name="sitios",
            name="comuna",
            field=models.CharField(blank=True, max_length=30, verbose_name="Comuna"),
        ),
        migrations.AddField(
            model_name="sitios",
            name="contratista",
            field=models.CharField(
                blank=True,
                choices=[("MER", "MER"), ("AJ", "AJ")],
                default="MER",
                max_length=120,
                verbose_name="contratista",
            ),
        ),
        migrations.AddField(
            model_name="sitios",
            name="estado",
            field=models.CharField(
                choices=[
                    ("Asignado", "ASG"),
                    ("Ejecución", "EJE"),
                    ("Postergado", "PTG"),
                    ("Cancelado", "CAN"),
                ],
                default="EJE",
                max_length=10,
                verbose_name="servicio",
            ),
        ),
        migrations.AddField(
            model_name="sitios",
            name="ito",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="ITO"
            ),
        ),
        migrations.AddField(
            model_name="sitios",
            name="lat",
            field=models.FloatField(
                blank=True, max_length=10, null=True, verbose_name="latitud"
            ),
        ),
        migrations.AddField(
            model_name="sitios",
            name="lon",
            field=models.FloatField(
                blank=True, max_length=10, null=True, verbose_name="longitud"
            ),
        ),
    ]
