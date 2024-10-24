from django.db import models

class StrokePrediction(models.Model):
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    hypertension = models.BooleanField()
    heart_disease = models.BooleanField()
    ever_married = models.CharField(max_length=3)
    work_type = models.CharField(max_length=20)
    Residence_type = models.CharField(max_length=10)
    avg_glucose_level = models.FloatField()
    bmi = models.FloatField()
    smoking_status = models.CharField(max_length=20)
    risk = models.CharField(max_length=4)
    probability = models.FloatField()

    def __str__(self):
        return f"Prediction for {self.gender}, {self.age} years old"