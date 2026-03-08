from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User
class User(AbstractUser):
    role = models.CharField(max_length=50, default="user")


# Machine
class Machine(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class EnergyData(models.Model):
    voltage = models.FloatField()
    current = models.FloatField()
    power = models.FloatField()
    energy = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} - {self.power} W"
    

    

class Mesure(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    tension = models.FloatField()
    courant = models.FloatField()
    puissance = models.FloatField()
    cos_phi = models.FloatField()
    frequence = models.FloatField()
    energie = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at}"
