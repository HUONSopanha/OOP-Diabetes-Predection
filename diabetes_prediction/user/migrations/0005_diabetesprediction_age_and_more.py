# Generated by Django 5.1.3 on 2024-12-31 13:31

import user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_diabetesprediction_diabetespedigreefunction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='diabetesprediction',
            name='Age',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='diabetesprediction',
            name='diabetes_prediction',
            field=models.BinaryField(null=True),
        ),
    ]
