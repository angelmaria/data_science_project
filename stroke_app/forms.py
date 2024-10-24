from django import forms

class StrokeForm(forms.Form):
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    age = forms.IntegerField(min_value=0, max_value=100)
    hypertension = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')])
    heart_disease = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')])
    ever_married = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    work_type = forms.ChoiceField(choices=[
        ('Private', 'Private'),
        ('Self-employed', 'Self-employed'),
        ('Govt_job', 'Government Job'),
        ('children', 'Children'),
        ('Never_worked', 'Never worked')
    ])
    Residence_type = forms.ChoiceField(choices=[('Urban', 'Urban'), ('Rural', 'Rural')])
    avg_glucose_level = forms.FloatField(min_value=50, max_value=200)
    bmi = forms.FloatField(min_value=10, max_value=50)
    smoking_status = forms.ChoiceField(choices=[
        ('formerly smoked', 'Formerly smoked'),
        ('never smoked', 'Never smoked'),
        ('smokes', 'Smokes'),
        ('Unknown', 'Unknown')
    ])