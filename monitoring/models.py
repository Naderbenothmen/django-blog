from django.db import models

class EnergyData(models.Model):
    voltage = models.FloatField()
    current = models.FloatField()
    power = models.FloatField()
    energy = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} - {self.power} W"
