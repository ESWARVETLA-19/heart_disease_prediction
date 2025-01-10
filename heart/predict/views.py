from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def heart_disease_form(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        age = request.POST.get('dob')
        sex = request.POST.get('sex')
        chest_pain = request.POST.get('chest-pain')
        resting_bp = request.POST.get('resting-bp')
        cholesterol = request.POST.get('cholesterol')
        fasting_blood_sugar = 'fasting-blood-sugar' in request.POST
        exercise_induced_angina = 'exercise-induced-angina' in request.POST
        ecg = request.POST.get('ecg')
        max_heart_rate = request.POST.get('max-heart-rate')
        old_peak = request.POST.get('old-peak')
        slope = request.POST.get('slope')
        vessels = request.POST.get('vessels')
        thal = request.POST.get('thal')
        result_data = {
            'fullname': fullname,
            'age': age,
            'sex': sex,
            'chest_pain': chest_pain,
            'resting_bp': resting_bp,
            'cholesterol': cholesterol,
            'fasting_blood_sugar': fasting_blood_sugar,
            'exercise_induced_angina': exercise_induced_angina,
            'ecg': ecg,
            'max_heart_rate': max_heart_rate,
            'old_peak': old_peak,
            'slope': slope,
            'vessels': vessels,
            'thal': thal
        }

        # Render the result.html template with the result data
        return render(request, 'result.html', {'result_data': result_data})
    
    return render(request, 'index.html')
