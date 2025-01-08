from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DiabetesPrediction)
#admin.register(DiabetesPrediction)
#class DiabetesPredictionAdmin(admin.ModelAdmin):
#    list_display = ('first_name', 'last_name', 'sex', 'date_of_birth', 'glucose', 'skin_thickness', 'num_pregnancies', 'bmi', 'blood_pressure', 'created_at', 'updated_at')
