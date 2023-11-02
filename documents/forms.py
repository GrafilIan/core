# forms.py

from django import forms
from .models import Internship, WeeklyBin
from signup.models import Intern_Records
class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = ['starting_month']
        widgets = {
            'starting_month': forms.DateInput(attrs={'type': 'date'}),
        }

class WeeklyBinForm(forms.ModelForm):
    class Meta:
        model = WeeklyBin
        fields = ['week_number', 'document_submission','rendered_hours']

class AddBinForm(forms.ModelForm):
    class Meta:
        model = WeeklyBin
        fields = ['week_number']

class WeeklyHoursForm(forms.ModelForm):
    class Meta:
        model = Intern_Records
        fields = ['weekly_hours']

    def clean_weekly_hours(self):
        weekly_hours = self.cleaned_data['weekly_hours']
        if weekly_hours < 0:
            raise forms.ValidationError("Weekly hours cannot be negative.")
        return weekly_hours