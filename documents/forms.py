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
    Weekly_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'summernote',  # Add necessary CSS classes
            'placeholder': 'Title',  # Set the placeholder text
            'required': 'True',
        })
    )

    class Meta:
        model = WeeklyBin
        fields = ['week_number', 'Weekly_text','document_submission','rendered_hours']

    def __init__(self, *args, **kwargs):
        super(WeeklyBinForm, self).__init__(*args, **kwargs)
        self.fields['week_number'].widget.attrs.update({
            'class': 'form-group',  # Add necessary CSS classes
            'placeholder': 'Week Number',  # Set the placeholder text
            'required': False
        })
        self.fields['document_submission'].widget.attrs.update({
            'class': 'form-control',  # Add necessary CSS classes
            'placeholder': 'Weekly Report',  # Set the placeholder text
            'required': False
        })
        self.fields['rendered_hours'].widget.attrs.update({
            'class': 'form-control',  # Add necessary CSS classes
            'placeholder': 'Hours Rendered',  # Set the placeholder text
            'required': False
        })

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