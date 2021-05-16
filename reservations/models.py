from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

from authentication.models import Doctor


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    spot = models.DateField()
