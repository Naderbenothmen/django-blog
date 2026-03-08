from django.urls import path
from . import views

urlpatterns = [

    # Energy API
    path('energy/', views.get_energy_data, name='energy'),
    path('energy/latest/', views.get_latest_energy, name='latest_energy'),
    path('energy/stats/', views.get_energy_stats, name='energy_stats'),
    path('api/chart/', views.get_chart_data, name='chart_data'),

    # Users
    path('gestion-users/', views.gestion_users, name='gestion_users'),
    path('add-user/', views.add_user, name='add_user'),
    path('edit-user/<int:id>/', views.edit_user, name='edit_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('toggle-user/<int:user_id>/', views.toggle_user, name='toggle_user'),

    # Machines
    path('machines/', views.machine_list, name='machine_list'),
    path('add-machine/', views.add_machine, name='add_machine'),

    # Settings
    path('settings/', views.settings_view, name='settings'),

]

