from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import DiabetesPrediction


def home_screen_view(request):
    # hello, if you see this please respond
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        sex = request.POST.get('sex')
        dob = (request.POST.get('age'))
        glucose = float(request.POST.get('glucose'))
        skin_thickness = float(request.POST.get('skin_thickness'))
        
        # Handle the case where the user selects "Male" as their sex
        if sex == 'male':
            num_pregnancies = 0
        else:
            num_pregnancies = int(request.POST.get('num_pregnancies'))
        
        bmi = float(request.POST.get('bmi'))
        blood_pressure = float(request.POST.get('blood_pressure'))

        prediction = DiabetesPrediction(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            dob = dob,
            glucose=glucose,
            skin_thickness=skin_thickness,
            num_pregnancies=num_pregnancies,
            bmi=bmi,
            blood_pressure=blood_pressure
        )
        prediction.save()
        return redirect('success_page')

    print(request.headers)
    return render(request, "base.html", {})

# Create your views here.
