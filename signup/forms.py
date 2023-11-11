from .models import Intern_Records
from django.forms.widgets import Select
from django import forms


class InternForm(forms.ModelForm):
    class MiddleNameWidget(forms.TextInput):
        def render(self, name, value, attrs=None, renderer=None):
            if value.lower() == 'na':
                return ''
            return super().render(name, value, attrs, renderer)

    class SuffixNameWidget(forms.TextInput):
        def render(self, name, value, attrs=None, renderer=None):
            if value.lower() == 'na':
                return ''
            return super().render(name, value, attrs, renderer)

    class CompanyNameWidget(forms.TextInput):
        def render(self, name, value, attrs=None, renderer=None):
            if value.lower() == 'na':
                return ''
            return super().render(name, value, attrs, renderer)

    class AddressWidget(forms.TextInput):
        def render(self, name, value, attrs=None, renderer=None):
            if value.lower() == 'na':
                return ''
            return super().render(name, value, attrs, renderer)

    class Meta:
        model = Intern_Records
        fields = [
            'student_id',
            'middle_name',
            'suffix',
            'present_address',
            'academic_year',
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
            'placeholder': 'Type "na" if not applicable',
            'required': False
        })

        self.fields['suffix'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Type "na" if not applicable',
            'required': False
        })

        self.fields['present_address'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Present Address',
            'required': 'True'
        })

        self.fields['academic_year'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Academic Year (e.g 2023-2024)',
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
            ('BSE', 'BSE'),
        ]
        self.fields['course'].widget = Select(attrs={
            'class': 'form-control',
            'required': 'True'
        })

        self.fields['course'].choices = COURSE_CHOICES

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
            'placeholder': 'Type "na" if not applicable',
            'required': 'True'
        })
        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Type "na" if not applicable',
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
            ('On Leave', 'On Leave'),
            ('Late OJT', 'Late OJT'),
            ('Extended', 'Extended'),
            ('Completed', 'Completed'),

        ]
        self.fields['status'].widget = Select(attrs={
            'class': 'form-control',
            'required': 'True'
        })
        self.fields['status'].choices = STATUS_CHOICES


class InternStatusEditForm(forms.ModelForm):
    class Meta:
        model = Intern_Records
        fields = ['status']

    def __init__(self, *args, **kwargs):
       super(InternStatusEditForm, self).__init__(*args, **kwargs)

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
            'class': 'custom-select',
            'required': 'True'
        })
       self.fields['status'].choices = STATUS_CHOICES