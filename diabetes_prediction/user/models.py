from django.db import models
from datetime import date
from datetime import datetime
from user.model_diabetes import *
from user.to_csv import *
class DiabetesPrediction(models.Model):
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    def save(self, *args, **kwargs):
        if self.dob:
            # Ensure self.dob is a date object
            if isinstance(self.dob, str):
                self.dob = datetime.strptime(self.dob, '%Y-%m-%d').date()
            today = date.today()
            self.age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        super().save(*args, **kwargs)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    dob = models.DateField()  
    glucose = models.FloatField()
    skin_thickness = models.FloatField()
    num_pregnancies = models.IntegerField()
    bmi = models.FloatField()
    blood_pressure = models.FloatField()
    DiabetesPedigreeFunction = models.FloatField()
    insulin = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    age = models.IntegerField(blank=True, null=True)# Store age in the database
    diabetes_prediction = models.IntegerField(blank=True, null=True)
    pro_true = models.FloatField(blank=True, null=True)
    pro_false = models.FloatField(blank=True, null=True)

class Meta:
    db_table = 'user_diabetesprediction'
    