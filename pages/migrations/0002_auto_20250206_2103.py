# Generated by Django 3.2.6 on 2025-02-06 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='distance_km',
        ),
        migrations.AddField(
            model_name='hospital',
            name='contact_number',
            field=models.CharField(default=9988007742, max_length=15),
            preserve_default=False,
        ),
    ]
