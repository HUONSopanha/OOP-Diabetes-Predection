# Generated by Django 5.1.3 on 2025-01-01 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_diabetesprediction_diabetespedigreefunction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diabetesprediction',
            name='diabetes_prediction',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
