import random
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proments.settings")
django.setup()

from monitoring.models import EnergyData

EnergyData.objects.create(
    voltage=random.uniform(210, 230),
    current=random.uniform(5, 15),
    power=random.uniform(1000, 3000),
    energy=random.uniform(10, 50)
)

print("Data inserted ✅")
