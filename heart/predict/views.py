
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pickle
import numpy as np
import os
from .forms import HeartDiseaseForm
from xhtml2pdf import pisa
from django.template.loader import get_template

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
            
            request.session["cleaned_data"] = cleaned_data
            request.session["prediction"] = "High Risk" if prediction == 1 else "Low Risk"

            return render(request, "result.html", { 
                "cleaned_data":cleaned_data,
                "prediction": "High Risk" if prediction == 1 else "Low Risk"
            })
  
            
    else:
        form = HeartDiseaseForm()

    return render(request, "index.html", {"form": form}) 
 

#pdf Generator

from django.template.loader import get_template
from xhtml2pdf import pisa
import io
from django.http import HttpResponse

def generate_pdf(request):
    cleaned_data = request.session.get("cleaned_data")
    prediction = request.session.get("prediction")

    if not cleaned_data or not prediction:
        return HttpResponse("No data available for PDF generation.", status=400)



    context = {
        "cleaned_data": cleaned_data,
        "prediction": prediction,
    }

    template = get_template("downloadpdf.html")
    html = template.render(context)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("utf-8")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type="application/pdf")
    return HttpResponse("Error generating PDF", status=500)


