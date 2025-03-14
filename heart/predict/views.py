# from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import HeartDiseaseForm
# from django.views.decorators.csrf import csrf_exempt
# import pickle
# import numpy as np

# @csrf_exempt 
# def heart_disease_form(request):
#     if request.method == 'POST':
#         form = HeartDiseaseForm(request.POST)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             fullname = cleaned_data.get('fullname')
            
#             age = cleaned_data.get('age')
#             sex = cleaned_data.get('sex')
#             chest_pain = cleaned_data.get('chest_pain')
#             resting_bp = cleaned_data.get('resting_bp')
#             cholesterol = cleaned_data.get('cholesterol')
#             fasting_blood_sugar = cleaned_data.get('fasting_blood_sugar')
#             exercise_induced_angina = cleaned_data.get('exercise_induced_angina')
#             ecg = cleaned_data.get('ecg')
#             max_heart_rate = cleaned_data.get('max_heart_rate')
#             old_peak = cleaned_data.get('old_peak')
#             slope = cleaned_data.get('slope')
#             vessels = cleaned_data.get('vessels')
#             thal = cleaned_data.get('thal')
            
        
#             features = [
#                 float(age), 
#                 float(sex), 
#                 float(chest_pain), 
#                 float(resting_bp), 
#                 float(cholesterol), 
#                 float(fasting_blood_sugar), 
#                 float(ecg), 
#                 float(max_heart_rate), 
#                 float(exercise_induced_angina), 
#                 float(old_peak), 
#                 float(slope), 
#                 float(vessels), 
#                 float(thal)
#             ]
                                

#             print(sex)      
#             print(features) 
#             input_data_array = np.asarray(features, dtype=np.float64)
#             input_array=input_data_array.reshape(1, -1) 
#             try:
#                 with open('trained_model.pkl', 'rb') as file:
#                     pickle_data = pickle.load(file)
#                     data=pickle_data.predict(input_array) 
#             except Exception as e:
#                 pickle_data = {'error': str(e)}

            
#             return render(request, 'result.html', {
#                 'cleaned_data': cleaned_data,
#                 'pickle_data': pickle_data
#             })

#     else:
#         form = HeartDiseaseForm()

#     return render(request, 'index.html', {'form': form}) 

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pickle
import numpy as np
import os
from .forms import HeartDiseaseForm

# Get the BASE directory (Root Django Project Folder)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define correct paths for the model and scaler (outside `prediction/`)
model_path = os.path.join(BASE_DIR, "testxgb_model.pkl")
scaler_path = os.path.join(BASE_DIR, "testscaler.pkl")

# Load the trained model and scaler
trained_model, scaler = None, None

try:
    with open(model_path, "rb") as model_file:
        trained_model = pickle.load(model_file)
    with open(scaler_path, "rb") as scaler_file: 
        scaler = pickle.load(scaler_file)

    if trained_model is None or scaler is None:
        raise ValueError("Model or Scaler failed to load.")
    print(" Model and Scaler loaded successfully!")
except Exception as e:
    print(f" Error loading model or scaler: {e}")

@csrf_exempt
def heart_disease_form(request):
    if request.method == "POST":
        form = HeartDiseaseForm(request.POST)
        
        if form.is_valid():
            cleaned_data = form.cleaned_data
            features = [
                float(cleaned_data["age"]),
                float(cleaned_data["sex"]),
                float(cleaned_data["chest_pain"]),
                float(cleaned_data["resting_bp"]),
                float(cleaned_data["cholesterol"]),
                float(cleaned_data["fasting_blood_sugar"]),
                float(cleaned_data["ecg"]),
                float(cleaned_data["max_heart_rate"]),
                float(cleaned_data["exercise_induced_angina"]),
                float(cleaned_data["old_peak"]),
                float(cleaned_data["slope"]),
                float(cleaned_data["vessels"]),
                float(cleaned_data["thal"]),
            ]

            # Convert input to NumPy array
            input_array = np.array(features, dtype=np.float64).reshape(1, -1)

            if trained_model is None or scaler is None:
                return JsonResponse({"error": "Model or scaler not loaded properly."}, status=500)

            try:
                # Scale input data before prediction
                input_data_scaled = scaler.transform(input_array)

                # Make prediction
                prediction = trained_model.predict(input_data_scaled)[0]

            except Exception as e:
                return JsonResponse({"error": f"Prediction error: {str(e)}"}, status=500)

            return render(request, "result.html", { 
                "cleaned_data":cleaned_data,
                "prediction": "High Risk" if prediction == 1 else "Low Risk"
            })

    else:
        form = HeartDiseaseForm()

    return render(request, "index.html", {"form": form}) 
 
