from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg, Max, Min
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import EnergyData
from .serializers import EnergyDataSerializer


@api_view(['GET'])
def get_latest_energy(request):
    latest = EnergyData.objects.order_by('-id').first()

    if not latest:
        return Response({"message": "No data available"})

    serializer = EnergyDataSerializer(latest)
    return Response(serializer.data)
@api_view(['GET'])
def get_energy_stats(request):
    stats = EnergyData.objects.aggregate(
        avg_voltage=Avg('voltage'),
        avg_current=Avg('current'),
        avg_power=Avg('power'),
        max_power=Max('power'),
        min_power=Min('power'),
    )
    return Response(stats)
@api_view(['GET'])
def get_energy_data(request):
    data = EnergyData.objects.all()
    serializer = EnergyDataSerializer(data, many=True)
    return Response(serializer.data)



def home(request):
    return render(request, 'home.html')
def login_view(request):
    return render(request, "login.html")
def forgot_password(request):
    return render(request, "forgot_password.html")
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "Email ou mot de passe incorrect"})

    return render(request, "login.html")
def dashboard_view(request):
    return render(request, "dashboard.html")
def historique_view(request):
    return render(request, 'historique.html')
def rapport_view(request):
    return render(request, 'rapport.html')