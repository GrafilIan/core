# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Intern(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  # Use OneToOneField
    student_id = models.CharField(max_length=200, verbose_name='Student ID', null=True)
    middle_name = models.CharField(max_length=200, verbose_name='Middle Name', null=True)
    suffix = models.CharField(max_length=200, verbose_name='suffix', null=True)
    present_address = models.CharField(max_length=200, verbose_name='Present Address', null=True)
    SEMESTER_CHOICES =[
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
        }
        return COURSE_OJT_HOURS.get(self.course, 0)

    year_level = models.CharField(max_length=200, verbose_name='Year Level', null=True)
    block = models.CharField(max_length=200, verbose_name='Block', null=True)

    company_name = models.CharField(max_length=200, verbose_name='Company', null=True)
    address = models.CharField(max_length=200, verbose_name='Address', null=True)

    contact_person = models.CharField(max_length=200, verbose_name='Contact Person', null=True)
    contact_number = models.CharField(max_length=200, verbose_name='Contact Number', null=True)

    profile_image = models.ImageField(upload_to='profile_images/', default='images/default_profile_image.png')
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
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return self.student_id
