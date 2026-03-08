from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Machine, EnergyData, Mesure

admin.site.register(User)
admin.site.register(Machine)
admin.site.register(EnergyData)
admin.site.register(Mesure)