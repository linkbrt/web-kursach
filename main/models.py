from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    pass

class RoomReservation(models.Model):
    room = models.CharField(max_length=10)
    date = models.DateField()
    
    def __str__(self):
        return "Комната " + self.room + " " + self.date.isoformat()
