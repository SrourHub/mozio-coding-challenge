# Generated by Django 4.0.5 on 2022-06-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicearea',
            name='geojson_information',
            field=models.JSONField(verbose_name='GEOJSON_INFORMATION'),
        ),
    ]