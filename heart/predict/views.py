from django.shortcuts import render
from django.http import HttpResponse
from .forms import HeartDiseaseForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def heart_disease_form(request):
    if request.method == 'POST':
        form = HeartDiseaseForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            fullname = cleaned_data.get('fullname')
            age = cleaned_data.get('dob')
            sex = cleaned_data.get('sex')
         
            return render(request, 'result.html', {'cleaned_data': cleaned_data})
    else:
        form = HeartDiseaseForm()

    return render(request, 'index.html', {'form': form})
