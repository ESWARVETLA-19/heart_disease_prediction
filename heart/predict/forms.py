from django import forms

class HeartDiseaseForm(forms.Form):
    fullname = forms.CharField(
        label="Full Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your name',
            'class': 'input',
            'required': True,
        })
    )

    age = forms.IntegerField(
        label="AGE",
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter Your Age',
            'class': 'input',
            'required': True,
        })
    )

    sex = forms.ChoiceField(
        label="Sex",
        choices=[('1', 'Male'), ('0', 'Female')],  
        widget=forms.RadioSelect(attrs={
            'class': 'radio',
            'required': True,
        })
    )

    chest_pain = forms.ChoiceField(
        label="Chest Pain Type",
        choices=[
            ('0', 'Typical Angina'),
            ('1', 'Atypical Angina'),
            ('2', 'Nonanginal Pain'),
            ('3', 'Asymptomatic'),
        ],
        widget=forms.Select(attrs={
            'class': 'select',
            'required': True,
        })
    )

    resting_bp = forms.FloatField(
        label="Resting BP",
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter value',
            'class': 'input',
            'step': '0.01',
            'required': True,
        })
    )

    cholesterol = forms.FloatField(
        label="Serum Cholesterol (mg/dl)",
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter value',
            'class': 'input',
            'step': '0.01',
            'required': True,
        })
    )

    fasting_blood_sugar = forms.BooleanField(
        label="Fasting blood sugar > 120 mg/dl",
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'checkbox',
        })
    )

    exercise_induced_angina = forms.BooleanField(
        label="Exercise induced Angina",
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'checkbox',
        })
    )

    ecg = forms.ChoiceField(
        label="Resting Electrocardiograph Result",
        choices=[
            ('0', 'Normal'),
            ('1', 'ST-T wave abnormality'),
            ('2', 'Left ventricular hypertrophy'),
        ],
        widget=forms.Select(attrs={
            'class': 'select',
            'required': True,
        })
    )

    max_heart_rate = forms.FloatField(
        label="Maximum Heart Rate Achieved",
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter value',
            'class': 'input',
            'step': '0.01',
            'required': True,
        })
    )

    old_peak = forms.FloatField(
        label="Old Peak",
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter value',
            'class': 'input',
            'step': '0.01',
            'required': True,
        })
    )

    slope = forms.ChoiceField(
        label="Slope of the Peak Exercise ST Segment",
        choices=[
            ('0', 'Up Sloping'),
            ('1', 'Flat'),
            ('2', 'Down Sloping'),
        ],
        widget=forms.Select(attrs={
            'class': 'select',
            'required': True,
        })
    )

    vessels = forms.IntegerField(
        label="Number of Major Vessels (0-3)",
        min_value=0,
        max_value=3,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter value',
            'class': 'input',
            'required': True,
        })
    )

    thal = forms.ChoiceField(
        label="Thal Value",
        choices=[
            ('0', 'Negative'),
            ('1', 'Positive'),
            ('2', 'In conclusive'),
        ],
        widget=forms.Select(attrs={
            'class': 'select',
            'required': True,
        })
    )
