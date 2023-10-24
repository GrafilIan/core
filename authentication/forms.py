from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms


# uncomment this if you want to change the class/design of the login form
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username',
            'required': 'True'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
            'required': 'True'
        })


# Customizing Registration Form from UserCreationForm
def validate_sorsu_email(value):
    if not value.endswith('@sorsu.edu.ph'):
        raise forms.ValidationError("Only email addresses ending with @sorsu.edu.ph are allowed.")


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    # uncomment this if you want to change the class/design of the registration form inputs
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'First Name',
            'required': 'True'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Last Name',
            'required': 'True'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username',
            'required': 'True'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email',
            'required': 'True'
        })
        self.fields['email'].validators = [validate_sorsu_email]

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
            'required': 'True'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Retype Password',
            'required': 'True'
        })




