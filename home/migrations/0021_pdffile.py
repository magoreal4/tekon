# Generated by Django 4.2.8 on 2024-01-08 22:06

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0020_delete_pdffile"),
    ]

    operations = [
        migrations.CreateModel(
            name="PdfFile",
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
                ("title", models.CharField(max_length=100)),
                (
                    "pdf",
                    models.FileField(
                        storage=home.models.OverwriteStorage(), upload_to="pdfs/"
                    ),
                ),
            ],
        ),
    ]