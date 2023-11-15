# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.safestring import mark_safe

from documents.models import Folder


# Create your models here.
class Intern_Records(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    folder = models.ForeignKey(Folder, on_delete=models.SET_NULL, blank=True, null=True)
    student_id = models.CharField(max_length=200, verbose_name='Student ID', null=True)
    middle_name = models.CharField(max_length=200, verbose_name='Middle Name', null=True)
    suffix = models.CharField(max_length=200, verbose_name='suffix', null=True)
    present_address = models.CharField(max_length=200, verbose_name='Present Address', null=True)
    academic_year = models.CharField(max_length=200, verbose_name='Academic Year', null=True)
    SEMESTER_CHOICES = [
        ('1st Semester', '1st Semester'),
        ('2nd Semester', '2nd Semester'),
    ]
    semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES, null=True)

    course = models.CharField(
        max_length=10,
        verbose_name='Course',
        choices=(
            ('BSIT', 'BSIT'),
            ('BSIS', 'BSIS'),
            ('BSCS', 'BSCS'),
            ('BSA', 'BSA'),
            ('BSAIS', 'BSAIS'),
            ('BPA', 'BPA'),
            ('BSE', 'BSE'),
        ),
        null=True
    )

    # Method to get OJT hours based on the selected course
    def get_ojt_hours(self):
        COURSE_OJT_HOURS = {
            'BSIT': 366,
            'BSIS': 366,
            'BSCS': 182,
            'BSA': 300,
            'BSAIS': 400,
            'BPA': 300,
            'BSE': 300,
        }
        return COURSE_OJT_HOURS.get(self.course, 0)


    def get_remaining_ojt_hours(self):
        COURSE_OJT_HOURS = {
            'BSIT': 366,
            'BSIS': 366,
            'BSCS': 182,
            'BSA': 300,
            'BSAIS': 400,
            'BPA': 300,
            'BSE': 300,
        }
        total_required_hours = COURSE_OJT_HOURS.get(self.course, 0)
        remaining_hours = total_required_hours - self.weekly_hours
        return remaining_hours

    weekly_hours = models.PositiveIntegerField(default=0, verbose_name='Weekly Hours')
    year_level = models.CharField(max_length=200, verbose_name='Year Level', null=True)
    block = models.CharField(max_length=200, verbose_name='Block', null=True)

    company_name = models.CharField(max_length=200, verbose_name='Company', null=True)
    address = models.CharField(max_length=200, verbose_name='Address', null=True)

    contact_person = models.CharField(max_length=200, verbose_name='Contact Person', null=True)
    contact_number = models.CharField(max_length=200, verbose_name='Contact Number', null=True)

    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/SSUProfile.png')
    pub_date = models.DateTimeField(default=now)

    # Intern Status
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

    @property
    def status_badge(self):
        # Define a dictionary that maps status choices to corresponding background colors
        status_colors = {
            'Not Placed': '#4d5059',
            'On OJT': '#00e738',  # Change color for 'On OJT' to green
            'Late OJT': '#ff8000',  # Change color for 'Terminated' to orange
            'On Leave': '#edbc62', # Change color for 'On Leave' to apricot
            'Suspended': '#1e1f22',  # Change color for 'Resigned' to black
            'Resigned': '#0000ff',  # Change color for 'Suspended' to blue
            'Extended': '#f2c115',  # Change color for 'Extended' to yellow
            'Terminated': '#ff0000',  # Change color for 'Late OJT' to red
            'Completed': '#00ffff',  # Change color for 'Completed' to cyan
        }

        # Get the CSS class based on the status choice
        background_color = status_colors.get(self.status, '')

        # Return the badge HTML

        return mark_safe(
            f'<span class="badge" style="background-color: {background_color}; color: white;">{self.status}</span>')

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True)

    form_filled_out = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)
