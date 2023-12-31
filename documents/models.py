# models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Internship(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    starting_month = models.DateField()

    def __str__(self):
        return self.user.username

class WeeklyBin(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    week_number = models.PositiveIntegerField(null=True)
    Weekly_text = models.TextField()
    document_submission = models.FileField(upload_to='documents/', null=True, blank=True)
    rendered_hours = models.PositiveIntegerField(default=0)  # Add this field
    pub_date = models.DateTimeField(default=now)

    def __str__(self):
        return f"Week {self.week_number} - {self.internship.user.username}"



class Folder(models.Model):
    name = models.CharField(max_length=255)

class Record(models.Model):
    name = models.CharField(max_length=255)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

class Requirements(models.Model):
    REQUIREMENT_CHOICES = [
        ('Acceptance Form for OJT', 'Acceptance Form for OJT'),
        ('Cedula or CTC/GSIS/SSS No.', 'Cedula or CTC/GSIS/SSS No.'),
        ('Driver License/National ID/Senior Citizen ID', 'Driver License/National ID/Senior Citizen ID'),
        ('Evaluation of Grades', 'Evaluation of Grades'),
        ('Internship Agreement', 'Internship Agreement'),
        ('Medical Certificate', 'Medical Certificate'),
        ('Memorandum of Agreement (MOA)', 'Memorandum of Agreement (MOA)'),
        ('Parent Consent', 'Parent Consent'),
        ('Police Clearance', 'Police Clearance'),
        ('Student Information Sheet', 'Student Information Sheet'),

        # Add more choices as needed
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    requirement = models.CharField(max_length=300, choices=REQUIREMENT_CHOICES)
    document_image = models.ImageField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return f"{self.requirement} - {self.id}"

class DailyTimeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    DTR_Number = models.PositiveIntegerField(null=True)
    DTR_submission = models.FileField(upload_to='documents/',null=True, blank=True)

    def __str__(self):
        return f"DTR Report for {self.user}"

class NarrativeReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Narrative_Number = models.PositiveIntegerField(null=True)
    Narrative_Text = models.TextField()
    document_submission = models.FileField(upload_to='documents/',null=True, blank=True)

    def __str__(self):
        return f"Narrative Report for {self.user}"

class Post_Requirements(models.Model):
    POST_REQUIREMENT_CHOICES = [
        ('Monitoring Evaluation Sheet', 'Monitoring Evaluation Sheet'),
        ('Merit of Rating', 'Merit of Rating'),
        ('Student Feedback Form', 'Student Feedback Form'),
        ('Supervisor Feedback Form', 'Supervisor Feedback Form'),
        # Add more choices as needed
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_requirement = models.CharField(max_length=300, choices=POST_REQUIREMENT_CHOICES)
    document_image = models.ImageField(upload_to='documents/', blank=True, null=True)


    def __str__(self):
        return f"{self.post_requirement} - {self.id}"