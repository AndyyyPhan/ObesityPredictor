from django.shortcuts import render, redirect
from django.urls import reverse
import joblib
from predictor.forms import ObesityPredictionForm
import pandas as pd

model = joblib.load("ml_model/random_forest_model.pkl")
preprocessor = joblib.load("ml_model/preprocessor.pkl")


def predict_obesity(request):
    if request.method == 'POST':
        form = ObesityPredictionForm(request.POST)
        if form.is_valid():
            user_input = [
                form.cleaned_data['sex'],
                int(form.cleaned_data['age']),
                int(form.cleaned_data['height']),
                form.cleaned_data['overweight_obese_family'],
                form.cleaned_data['consumption_of_fast_food'],
                form.cleaned_data['frequency_of_consuming_vegetables'],
                form.cleaned_data['number_of_main_meals_daily'],
                form.cleaned_data['food_intake_between_meals'],
                form.cleaned_data['smoking'],
                form.cleaned_data['liquid_intake_daily'],
                form.cleaned_data['calculation_of_calorie_intake'],
                form.cleaned_data['physical_exercise'],
                form.cleaned_data['schedule_dedicated_to_technology'],
                form.cleaned_data['type_of_transportation_used'],
            ]

            column_names = [
                'Sex', 'Age', 'Height', 'Overweight_Obese_Family',
                'Consumption_of_Fast_Food', 'Frequency_of_Consuming_Vegetables',
                'Number_of_Main_Meals_Daily', 'Food_Intake_Between_Meals', 'Smoking',
                'Liquid_Intake_Daily', 'Calculation_of_Calorie_Intake', 'Physical_Excercise',
                'Schedule_Dedicated_to_Technology', 'Type_of_Transportation_Used'
            ]

            user_input_df = pd.DataFrame([user_input], columns=column_names)

            processed_input = preprocessor.transform(user_input_df)

            result = model.predict(processed_input)[0]

            return redirect(reverse('obesity_result') + f'?result={result}')
        else:
            print(form.errors)
    else:
        form = ObesityPredictionForm()
    return render(request, "predictor/index.html", {"form": form})


def obesity_result(request):
    result = request.GET.get("result", "No result available")
    return render(request, "predictor/result.html", {"prediction_text": result})