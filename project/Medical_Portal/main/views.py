from django.shortcuts import render, redirect
from .models import Medication, User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegister
# Create your views here.
def home(request):
    return render(request, "main/index.html")

def meds(request):
    meds = Medication.objects.all()
    return render(request, "main/user_meds.html", {
        "meds": meds,
    })

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try :
            user = User.objects.get(username=username)
        except :
            messages.error(request, "User not exists")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username Or password is not correct")
    return render(request, "main/login.html")

def logoutUser(request):
    logout(request)
    return redirect("home")

def register_user(request):
    if request.method == "POST":
	    form = UserRegister(request.POST)
	    if form.is_valid():
	        form.save()
	        return redirect("home")
    else:
	    form = UserRegister()

    return render(request, "main/register.html", {"form":form})

def add_med(request):
    if request.method == "POST":
        name = request.POST.get("medicine")
        times = request.POST.get("times")
        notes = request.POST.get("notes")

        if not name or not times or notes :
            messages.error(request, "You Have to Fill Every Field")
        Medication.objects.create(
            patient__id = request.user.id,
            name = name,
            times = times,
            notes = notes,
        )
