from django.shortcuts import render
from django.http import HttpResponse
from .forms import HeartDiseaseForm
from django.views.decorators.csrf import csrf_exempt
import pickle
import numpy as np

@csrf_exempt 
def heart_disease_form(request):
    if request.method == 'POST':
        form = HeartDiseaseForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            fullname = cleaned_data.get('fullname')
            # age = cleaned_data.get('age') 
            # sex = cleaned_data.get('sex')
            # cp=cleaned_data.get('chest_pain')
            # trestbps=cleaned_data.get('resting_bp')
            # chol=cleaned_data.get('cholesterol')
            # fbs=cleaned_data.get('fasting_blood_sugar')
            # exang=cleaned_data.get('exercise_induced_angina')
            # restecg=cleaned_data.get('ecg')
            # thalach=cleaned_data.get('max_heart_rate')
            # oldpeak=cleaned_data.get('old_peak')
            # slope=cleaned_data.get('slope')
            # ca=cleaned_data.get('vessels')
            # thal=cleaned_data.get('thal')
            age = cleaned_data.get('age')
            sex = cleaned_data.get('sex')
            chest_pain = cleaned_data.get('chest_pain')
            resting_bp = cleaned_data.get('resting_bp')
            cholesterol = cleaned_data.get('cholesterol')
            fasting_blood_sugar = cleaned_data.get('fasting_blood_sugar')
            exercise_induced_angina = cleaned_data.get('exercise_induced_angina')
            ecg = cleaned_data.get('ecg')
            max_heart_rate = cleaned_data.get('max_heart_rate')
            old_peak = cleaned_data.get('old_peak')
            slope = cleaned_data.get('slope')
            vessels = cleaned_data.get('vessels')
            thal = cleaned_data.get('thal')
            # features =[float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg), float(thalach),
            #  float(exang), float(oldpeak), float(slope), float(ca), float(thal)] 
        
            features = [
                float(age), 
                float(sex), 
                float(chest_pain), 
                float(resting_bp), 
                float(cholesterol), 
                float(fasting_blood_sugar), 
                float(ecg), 
                float(max_heart_rate), 
                float(exercise_induced_angina), 
                float(old_peak), 
                float(slope), 
                float(vessels), 
                float(thal)
            ]
                                

            print(sex)      
            print(features) 
            input_data_array = np.asarray(features, dtype=np.float64)
            input_array=input_data_array.reshape(1, -1) 
            try:
                with open('trained_model.pkl', 'rb') as file:
                    pickle_data = pickle.load(file)
                    data=pickle_data.predict(input_array) 
            except Exception as e:
                pickle_data = {'error': str(e)}

            
            return render(request, 'result.html', {
                'cleaned_data': cleaned_data,
                'pickle_data': pickle_data
            })

    else:
        form = HeartDiseaseForm()

    return render(request, 'index.html', {'form': form}) 
