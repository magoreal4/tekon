# Generated by Django 4.2.8 on 2024-01-08 22:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0021_pdffile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pdffile",
            name="title",
            field=models.CharField(blank=True, editable=False, max_length=100),
        ),
    ]
