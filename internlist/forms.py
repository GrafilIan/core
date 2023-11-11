# forms.py
from django import forms

class UserDeleteForm(forms.Form):
    user_id = forms.IntegerField(widget=forms.HiddenInput())
    # You can add other fields as needed

