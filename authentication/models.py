from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
