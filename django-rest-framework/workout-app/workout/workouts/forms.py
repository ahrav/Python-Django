from django import forms

from .models import Workout

class WorkoutForm(forms.ModelForm):
    name = forms.CharField(max_length=125, min_length=2)
    class Meta:
        model = Workout
        fields = [
            'user',
            'name',
            'sets',
            'repetitions',
            'rate_of_perceived_exertion',
            'percent_of_one_rep_max',
            'date'
        ]

    def clean_rate_of_perceived_exertion(self, *args, **kwargs):
        data = self.cleaned_data.get('rate_of_perceived_exertion')
        if data > 10:
            raise forms.ValidationError("Rate of perceived exertion can not exceed 10, you might die.")
        return data

    def clean_percent_of_one_rep_max(self, *args, **kwargs):
        data = self.cleaned_data.get('percent_of_one_rep_max')
        if data > 100:
            raise forms.ValidationError("Percent of 1 RM can not exceed 100, it's statistically impossible!")
        return data

    def clean(self, *args, **kwargs):
        return super().clean(*args, **kwargs)