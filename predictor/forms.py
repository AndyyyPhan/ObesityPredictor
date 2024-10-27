from django import forms

from django import forms


class ObesityPredictionForm(forms.Form):
    sex = forms.ChoiceField(label='Sex', choices=[('Male', 'Male'), ('Female', 'Female')])
    age = forms.IntegerField(label='Age')
    height = forms.IntegerField(label='Height (cm)')
    overweight_obese_family = forms.ChoiceField(label='Overweight/Obese Families',
                                                choices=[('Yes', 'Yes'), ('No', 'No')])
    consumption_of_fast_food = forms.ChoiceField(label='Consumption of Fast Food',
                                                 choices=[('Yes', 'Yes'), ('No', 'No')])
    frequency_of_consuming_vegetables = forms.ChoiceField(label='Frequency of Consuming Vegetables',
                                                          choices=[('Rarely', 'Rarely'), ('Sometimes', 'Sometimes'),
                                                                   ('Always', 'Always')])
    number_of_main_meals_daily = forms.ChoiceField(label='Number of Main Meals Daily',
                                                   choices=[('1-2', '1-2'), ('3', '3'), ('3+', '3+')])
    food_intake_between_meals = forms.ChoiceField(label='Food Intake Between Meals',
                                                  choices=[('Rarely', 'Rarely'), ('Sometimes', 'Sometimes'),
                                                           ('Usually', 'Usually'), ('Always', 'Always')])
    smoking = forms.ChoiceField(label='Smoking', choices=[('Yes', 'Yes'), ('No', 'No')])
    liquid_intake_daily = forms.ChoiceField(label='Liquid Intake Daily',
                                            choices=[('Less than 1 liter', 'Less than 1 liter'),
                                                     ('1 to 2 liters', '1 to 2 liters'),
                                                     ('More than 2 liters', 'More than 2 liters')])
    calculation_of_calorie_intake = forms.ChoiceField(label='Calculation of Calorie Intake',
                                                      choices=[('Yes', 'Yes'), ('No', 'No')])
    physical_exercise = forms.ChoiceField(label='Physical Exercise',
                                          choices=[('No physical activity', 'No physical activity'), ('1-2 days', '1-2 days'),
                                                   ('3-4 days', '3-4 days'), ('5-6 days', '5-6 days'),
                                                   ('6+ days', '6+ days')])
    schedule_dedicated_to_technology = forms.ChoiceField(label='Schedule Dedicated to Technology',
                                                         choices=[('0-2 hours', '0-2 hours'),
                                                                  ('3-5 hours', '3-5 hours'),
                                                                  ('>5 hours', '>5 hours')])
    type_of_transportation_used = forms.ChoiceField(label='Type of Transportation Used',
                                                    choices=[('Automobile', 'Automobile'), ('Motorbike', 'Motorbike'),
                                                             ('Bike', 'Bike'),
                                                             ('Public transportation', 'Public transportation'),
                                                             ('Walking', 'Walking')])
