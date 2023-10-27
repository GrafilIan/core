from django.db import models
from django.utils.timezone import now

class Announcement(models.Model):
    announcement_list = models.CharField(max_length=1000,null=True)
    image_announcement= models.ImageField(upload_to='media/images/', null=True, blank=True)
    document_announcement = models.FileField(upload_to='media/documents/', null=True, blank=True)
    pub_date = models.DateTimeField(default=now)

    def __str__(self):
        return f"Announcement {self.id}"