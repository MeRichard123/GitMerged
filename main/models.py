from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Message(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author")
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="receiver", null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author} Message to {self.receiver}'

    def get_absolute_url(self):
        return reverse("date-page")
