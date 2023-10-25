from .models import Intern_Records
from django.forms.widgets import Select
from django import forms


class InternForm(forms.ModelForm):
    class Meta:
        model = Intern_Records
        fields = [
            'student_id',
            'middle_name',
            'suffix',
            'present_address',
            'semester',
            'course',
            'year_level',
            'block',
            'company_name',
            'address',
            'contact_person',
            'contact_number',
            'profile_image',
            'status',
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
            'placeholder': 'Suffix',
            'required': 'False'
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

        STATUS_CHOICES = [
            ('Not Placed', 'Not Placed'),
            ('On OJT', 'On OJT'),
            ('Late OJT', 'Late OJT'),
            ('On Leave', 'On Leave'),
            ('Suspended', 'Suspended'),
            ('Resigned', 'Resigned'),
            ('Extended', 'Extended'),
            ('Terminated', 'Terminated'),
            ('Completed', 'Completed'),
        ]
        self.fields['status'].widget = Select(attrs={
            'class': 'form-control',
            'required': 'True'
        })
        self.fields['status'].choices = STATUS_CHOICES

