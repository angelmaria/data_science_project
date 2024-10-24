from django.shortcuts import render
from .forms import StrokeForm
import joblib
import numpy as np


def predict_stroke(request):
    if request.method == 'POST':
        form = StrokeForm(request.POST)
        if form.is_valid():
            # Cargar el modelo
            model = joblib.load('notebooks/full_stroke_prediction_pipeline.pkl')
            
            # Preparar los datos de entrada
            input_data = np.array([[
                form.cleaned_data['gender'],
                form.cleaned_data['age'],
                form.cleaned_data['hypertension'],
                form.cleaned_data['heart_disease'],
                form.cleaned_data['ever_married'],
                form.cleaned_data['work_type'],
                form.cleaned_data['Residence_type'],
                form.cleaned_data['avg_glucose_level'],
                form.cleaned_data['bmi'],
                form.cleaned_data['smoking_status'],
            ]])
            
            # Realizar la predicción
            probability = model.predict_proba(input_data)[0][1]
            risk = "High" if probability > 0.5 else "Low"
            
            return render(request, 'stroke_app/prediction_form.html', {
                'form': form,
                'show_result': True,
                'risk': risk,
                'probability': f"{probability:.2%}"
            })
    else:
        form = StrokeForm()
    
    return render(request, 'stroke_app/prediction_form.html', {'form': form})

def upload_csv_and_predict(request):
    print(request.FILES)
