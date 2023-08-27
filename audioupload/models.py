from django.contrib.auth.models import User
from django.db import models

class UploadedAudio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='uploaded_audio/')
    duration = models.IntegerField()  # Duration in seconds
    extension = models.CharField(max_length=10)
    size = models.PositiveIntegerField()

    def __str__(self):
        return self.audio_file.name
