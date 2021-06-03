from django.contrib.auth import get_user_model
from django.db import models

from authentication.models import Doctor
User = get_user_model()


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        line = 'Appointment with Doctor {} at {}'.format(str(self.doctor), self.time.__format__('%H:%M'))
        return line
