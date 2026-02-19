from django.urls import path
from .views import get_energy_data, get_latest_energy, get_energy_stats

urlpatterns = [
    path('energy/', get_energy_data),
    path('energy/latest/', get_latest_energy),
    path('energy/stats/', get_energy_stats),
]

