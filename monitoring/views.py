from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg, Max, Min
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import EnergyData, Mesure, Machine
from .serializers import EnergyDataSerializer
from .forms import UserForm, MachineForm
import random
import json

User = get_user_model()

# ---------------- API ENERGY ---------------- #

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


# ---------------- AUTH ---------------- #

def home(request):
    return render(request, 'home.html')


from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

User = get_user_model()

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        print(request.POST)  # 🔥 نشوف شنوّة يتبعث

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


def forgot_password(request):
    return render(request, "forgot_password.html")


# ---------------- DASHBOARD ---------------- #

def dashboard_view(request):
    return render(request, "dashboard.html")


def historique_view(request):
    return render(request, 'historique.html')


def rapport_view(request):
    return render(request, 'rapport.html')


def settings_view(request):
    return render(request, "settings.html")


# ---------------- USERS MANAGEMENT ---------------- #

@staff_member_required
def gestion_users(request):
    users = User.objects.all()
    return render(request, 'gestion_users.html', {'users': users})


@staff_member_required
def toggle_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if not user.is_superuser:
        user.is_active = not user.is_active
        user.save()
    return redirect('gestion_users')


@staff_member_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if not user.is_superuser:
        user.delete()
    return redirect('gestion_users')


def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('gestion_users')
    else:
        form = UserForm()

    return render(request, 'add_user.html', {'form': form})


# ---------------- MACHINE MANAGEMENT ---------------- #

def add_machine(request):
    if request.method == "POST":
        form = MachineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('machine_list')
    else:
        form = MachineForm()

    return render(request, 'add_machine.html', {'form': form})


def machine_list(request):
    machines = Machine.objects.all()
    return render(request, 'machine_list.html', {'machines': machines})


# ---------------- ESP32 DATA ---------------- #

@csrf_exempt
def receive_data(request):
    if request.method == "POST":
        data = json.loads(request.body)

        Mesure.objects.create(
            tension=data["tension"],
            courant=data["courant"],
            puissance=data["puissance"],
            cos_phi=data["cos_phi"],
            frequence=data["frequence"],
            energie=data["energie"]
        )

        return JsonResponse({"status": "ok"})


def get_chart_data(request):
    mesures = Mesure.objects.all().order_by('-id')[:20]

    data = {
        "labels": [m.created_at.strftime("%H:%M:%S") for m in mesures][::-1],
        "tension": [m.tension for m in mesures][::-1],
        "courant": [m.courant for m in mesures][::-1],
        "puissance": [m.puissance for m in mesures][::-1],
        "cos_phi": [m.cos_phi for m in mesures][::-1],
        "frequence": [m.frequence for m in mesures][::-1],
    }

    return JsonResponse(data)


from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

User = get_user_model()

def users_list(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})


def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect("users")

def toggle_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = not user.is_active
    user.save()
    return redirect("users")
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

User = get_user_model()

def add_user(request):

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("gestion_users")

    return render(request, 'add_user.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import User

def edit_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.save()
        return redirect("gestion_users")

    return render(request, "edit_user.html", {"user": user})