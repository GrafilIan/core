from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Intern
from django.forms.widgets import Select

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


class InternForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = [
            'student_id',
            'middle_name',
            'suffix',
            'present_address',
            'status',
            'course',
            'year_level',
            'block',
            'company_name',
            'address',
            'contact_person',
            'contact_number',
            'profile_image',
        ]

    def __init__(self, *args, **kwargs):
        super(InternForm, self).__init__(*args, **kwargs)
        self.fields['student_id'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Student No.',
            'required': 'True'
        })
        self.fields['middle_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Middle Initial'
        })
        self.fields['suffix'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Suffix'
        })
        self.fields['present_address'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Present Address',
            'required': 'True'
        })

        SEMESTER_CHOICES = [
            ('1st Semester', '1st Semester'),
            ('2nd Semester', '2nd Semester'),
        ]
        self.fields['semester'].widget = Select(attrs={
            'class': 'form-control',
            'required': 'True'
        })
        self.fields['semester'].choices = SEMESTER_CHOICES

        COURSE_CHOICES = [
            ('BSIT', 'BSIT'),
            ('BSIS', 'BSIS'),
            ('BSCS', 'BSCS'),
            ('BSA', 'BSA'),
            ('BSAIS', 'BSAIS'),
            ('BPA', 'BPA'),
        ]
        self.fields['course'].widget = Select(attrs={
            'class': 'form-control',
            'required': 'True'
        })
        self.fields['course'].choices = COURSE_CHOICES

        def get_ojt_hours(self):
            COURSE_OJT_HOURS = {
                'BSIT': 366,
                'BSIS': 366,
                'BSCS': 182,
                'BSA': 300,
                'BSAIS': 400,
                'BPA': 300,
            }
            return COURSE_OJT_HOURS.get(self.cleaned_data['course'], 0)


        self.fields['year_level'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Year Level',
            'required': 'True'
        })
        self.fields['block'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Block',
            'required': 'True'
        })
        self.fields['company_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Company Name',
            'required': 'True'
        })
        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Company Address',
            'required': 'True'
        })
        self.fields['contact_person'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contact Person'
        })
        self.fields['contact_number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contact Number'
        })
        self.fields['profile_image'].widget.attrs.update({
            'class': 'form-control'
        })
