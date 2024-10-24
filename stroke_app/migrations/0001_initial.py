# Generated by Django 3.2.10 on 2024-10-24 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StrokePrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('hypertension', models.BooleanField()),
                ('heart_disease', models.BooleanField()),
                ('ever_married', models.CharField(max_length=3)),
                ('work_type', models.CharField(max_length=20)),
                ('Residence_type', models.CharField(max_length=10)),
                ('avg_glucose_level', models.FloatField()),
                ('bmi', models.FloatField()),
                ('smoking_status', models.CharField(max_length=20)),
                ('risk', models.CharField(max_length=4)),
                ('probability', models.FloatField()),
            ],
        ),
    ]