# Generated by Django 4.2.8 on 2024-01-08 13:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0016_reporte"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reporte",
            old_name="pdf",
            new_name="archivo",
        ),
        migrations.RemoveField(
            model_name="reporte",
            name="titulo",
        ),
    ]
