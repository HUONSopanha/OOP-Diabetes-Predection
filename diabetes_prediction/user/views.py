from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import DiabetesPrediction
from django.shortcuts import render
from django.http import HttpResponse
from user.to_csv import *
from user.model_diabetes import *
from datetime import date
from datetime import datetime

# Create your views here.
def age(dob):
        if dob:
            # Ensure self.dob is a date object
            if isinstance(dob, str):
                dob = datetime.strptime(dob, '%Y-%m-%d').date()
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age
def home_screen_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        sex = request.POST.get('sex')
        dob = request.POST.get('dob')  
        glucose = float(request.POST.get('glucose'))
        skin_thickness = float(request.POST.get('skin_thickness'))

        # Handle the case where the user selects "Male" as their sex
        if sex == 'male':
            num_pregnancies = 0
        else:
            num_pregnancies = int(request.POST.get('num_pregnancies'))

        bmi = float(request.POST.get('bmi'))
        blood_pressure = float(request.POST.get('blood_pressure'))
        DiabetesPedigreeFunction = float(request.POST.get('DiabetesPedigreeFunction'))
    
        insulin = float(request.POST.get('Insulin'))
        true, false = probability(num_pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, DiabetesPedigreeFunction, age(dob))  # Replace with the actual function or import it
        if true>=false:
            diabetes_prediction=1
        else:
            diabetes_prediction= 0
        prediction = DiabetesPrediction(
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            dob=dob,  
            glucose=glucose,
            skin_thickness=skin_thickness,
            num_pregnancies=num_pregnancies,
            bmi=bmi,
            blood_pressure=blood_pressure,
            DiabetesPedigreeFunction=DiabetesPedigreeFunction,
            insulin=insulin,
            diabetes_prediction=diabetes_prediction,
            pro_true=round(true*100,2),
            pro_false=round(false*100,2),
        )
        prediction.save()
        return redirect('success_page')

    return render(request, "base.html", {})



def success_view(request):
    success_message = "Your form has been submitted successfully!"
    return render(request, 'success.html', {'success_message': success_message,
                                            'true':DiabetesPrediction.objects.last().pro_true,
                                            'false':DiabetesPrediction.objects.last().pro_false})
def success1_view(request):
    success1_message = "Your form has been submitted successfully!"
    return render(request, 'success1.html', {'success_message': success1_message,
                                            'true':DiabetesPrediction.objects.last().pro_true,
                                            'false':DiabetesPrediction.objects.last().pro_false})
    
def diabetes_blog(request):
    paragraph_1 = (
        "Diabetes is a chronic metabolic disorder characterized by elevated levels of glucose in the bloodstream, known as hyperglycemia. "
        "This condition arises when the body either cannot produce sufficient insulin or cannot effectively utilize the insulin it produces. "
        "Insulin is a hormone secreted by the pancreas that plays a crucial role in regulating blood sugar levels by facilitating the entry of glucose into cells for energy. "
        "There are primarily two types of diabetes: Type 1 and Type 2. Type 1 diabetes is an autoimmune condition where the immune system attacks the insulin-producing beta cells in the pancreas, leading to little or no insulin production. "
        "Type 2 diabetes, more common and often associated with lifestyle factors, occurs when the body becomes resistant to insulin or when the pancreas fails to produce enough insulin. "
        "If left unmanaged, diabetes can lead to serious complications, including cardiovascular disease, nerve damage, kidney failure, and vision problems, making early diagnosis and effective management essential for maintaining health and quality of life."
    )
    paragraph_2 = (
        "Diabetes is classified into three main types: Type 1, Type 2, and gestational diabetes. Type 1 diabetes typically develops in childhood or adolescence and is characterized by the body's inability to produce insulin due to autoimmune destruction of the pancreatic beta cells. "
        "Individuals with Type 1 diabetes require lifelong insulin therapy to manage their blood sugar levels. Type 2 diabetes is the most prevalent form, often developing in adulthood, although it is increasingly seen in younger populations due to rising obesity rates. "
        "In Type 2 diabetes, the body either becomes resistant to insulin or does not produce enough insulin to maintain normal glucose levels. Gestational diabetes occurs during pregnancy and usually resolves after childbirth, but it increases the risk of developing Type 2 diabetes later in life. "
        "Each type of diabetes has distinct causes, risk factors, and management strategies, necessitating tailored approaches to treatment and lifestyle modifications to maintain optimal health."
    )
    paragraph_3 = (
        "The symptoms of diabetes can vary widely depending on the type and severity of the condition. Common symptoms include excessive thirst (polydipsia), frequent urination (polyuria), extreme fatigue, and blurred vision. "
        "Excessive thirst occurs as the body attempts to dilute high blood sugar levels, leading to dehydration and prompting increased fluid intake. Frequent urination is a result of the kidneys working to remove excess glucose from the bloodstream, which can also lead to weight loss. "
        "Individuals may experience extreme fatigue due to the body's inability to effectively convert glucose into energy. Blurred vision can arise from fluid changes in the lenses of the eyes caused by fluctuating blood sugar levels. "
        "Other symptoms may include slow-healing wounds, frequent infections, and tingling or numbness in the extremities, indicating possible nerve damage. Recognizing these symptoms early is crucial for timely diagnosis and intervention, as unmanaged diabetes can lead to severe complications affecting multiple organ systems."
    )
    paragraph_4 = (
        "Currently, there is no definitive cure for diabetes; however, it can be effectively managed through a combination of lifestyle changes, medication, and monitoring. For Type 1 diabetes, lifelong insulin therapy is essential, as the body cannot produce insulin. "
        "Management involves regular blood sugar monitoring, adherence to a balanced diet, and consistent physical activity. For Type 2 diabetes, lifestyle modifications are critical. This includes adopting a healthy diet rich in whole grains, lean proteins, fruits, and vegetables while minimizing processed foods and sugars. "
        "Regular exercise helps improve insulin sensitivity and aids in weight management. In some cases, medication or insulin therapy may be required to help regulate blood sugar levels. Additionally, ongoing education about diabetes management empowers individuals to make informed choices regarding their health. "
        "While a complete cure remains elusive, maintaining optimal blood sugar levels can significantly reduce the risk of complications and enhance overall quality of life."
    )
    paragraph_5 = (
        "Long-term complications of diabetes can be severe and impact various organ systems in the body. Chronic high blood sugar levels can lead to cardiovascular disease, increasing the risk of heart attacks and strokes. "
        "Diabetic neuropathy, a condition resulting from nerve damage due to prolonged hyperglycemia, can cause pain, tingling, and loss of sensation in the extremities. Additionally, diabetes can lead to kidney damage, known as diabetic nephropathy, which may progress to kidney failure requiring dialysis or transplantation. "
        "Vision problems, including diabetic retinopathy, can result from damage to the blood vessels in the retina, potentially leading to blindness if not managed properly. Furthermore, individuals with diabetes are more susceptible to infections and may experience slow-healing wounds, increasing the risk of amputations. "
        "Regular medical check-ups, blood sugar monitoring, and adherence to treatment plans are essential in preventing or minimizing these complications, allowing individuals with diabetes to lead healthier lives and reduce the risk of long-term health issues."
    )

    return render(request, 'diabetes_blog.html', {
        'paragraph_1': paragraph_1,
        'paragraph_2': paragraph_2,
        'paragraph_3': paragraph_3,
        'paragraph_4': paragraph_4,
        'paragraph_5': paragraph_5,
    })
    
def about_us(request): 
    article_1 = (
        "We are junior students from the Department of Applied Mathematics and Statistics at the Institute of Technology of Cambodia. "
        "This project represents the culmination of our efforts in two key areas: Object-Oriented Programming and Introduction to Data Science."
    )
    article_2 = ("Our primary objective is to develop a predictive model for assessing the likelihood of diabetes using machine learning techniques applied to existing data. "
                 "To enhance user experience, we are creating a user-friendly interface that allows individuals to input essential health information, including glucose levels, skin thickness, insulin levels, body mass index (BMI), age, and the number of pregnancies. "
                 "This interface is being developed using Django and Python, enabling the construction of a robust and efficient web application."
                 )
    article_3 = (
                "We would like to express our profound gratitude to our esteemed lecturers, Dr. Phauk Sokkhey, our Introduction to Data Science lecturer, and Mr. Ngin Kimlong, our Object-Oriented Programming lecturer. "
                "Their invaluable support, guidance, and expertise have significantly contributed to the success of this project."
                )
    team_members = [
    {
        "name": "Huon Sophana",
        "id": "e20220209",
        "position": ["Project Manager (OOP)", "Data Engineer (IDS)"],
        "contact": {
            "Telegram": "https://t.me/Loid168",
            "Email": "sopanhahuon@gmail.com"
        },
    },
    {
        "name": "HANG Muykhorng",
        "id": "e20220209",
        "position": ["Frontend Developer (OOP)", "Data Analyst (IDS)"],
        "contact": {
            "Telegram": " https://t.me/Muykhorng",
            "Email": "muykhorng520@gmail.com"
        },
    },
    
    {
        "name": "HUN Sopheak",
        "id": "e20220446",
        "position": ["Backend Developer (OOP)", "Project Manager (IDS)"],
        "contact": {
            "Telegram": "https://t.me/sofia_desu",
            "Email": "sopheakhun593@gmail.com"
        },
    },
    
    {
        "name": "CHHOUK Phalthunin",
        "id": "e20220467",
        "position": ["Backend Developer (OOP)", "Document Specialist (IDS)"],
        "contact": {
            "Telegram": "https://t.me/Phalthunin",
            "Email": "phalthunin@gmail.com"
        },
    },
    
    {
        "name": "CHOEURN Brospov",
        "id": "20221157",
        "position": ["UI/UX (OOP)", "Data Collector(IDS)"],
        "contact": {
            "Telegram": "https://t.me/fong_enjoyeasylife",
            "Email": "brozzpov15022000@gmail.com"
        },
    }
    ] 
      
    return render(request, 'about_us.html', {
        'article_1': article_1,
        'article_2': article_2,
        'article_3': article_3,
        'team_members': team_members
    })
        
        

    
    
    
    




