from django.db import models

class DiabetesPrediction(models.Model):
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    dob = models.DateField()
    glucose = models.FloatField()
    skin_thickness = models.FloatField()
    num_pregnancies = models.IntegerField()
    bmi = models.FloatField()
    blood_pressure = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# Create your models here.
