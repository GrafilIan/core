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
