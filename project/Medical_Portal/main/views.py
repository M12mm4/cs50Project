from django.shortcuts import render, redirect
from .models import Medication, User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegister
from django.contrib.auth.decorators import login_required
# Create your views here.

"""################ Home and meds page ################"""



def home(request):
    return render(request, "main/index.html")

@login_required(login_url='login')
def meds(request):
    meds = Medication.objects.filter(patient=request.user)
    return render(request, "main/user_meds.html", {
        "meds": meds,
    })


"""################ Authenication ################"""



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


"""################ Medicatio CRUD ################"""



@login_required(login_url='login')
def add_med(request):
    if request.method == "POST":
        name = request.POST.get("medicine")
        times = request.POST.get("times")
        notes = request.POST.get("notes")
        
        print(f"\n\n##### {name} {times} {notes} #######")
        current_user = request.user
        Medication.objects.create(
            patient = current_user,
            name = name,
            times = times,
            notes = notes,
        )
    return render(request, "main/add_med.html")

@login_required(login_url='login')
def edit_medication(request, pk):
    current_user = request.user
    med = Medication.objects.get(
        id=pk,
        patient=current_user
        )

    if request.method == "POST":
        med.name = request.POST.get("name")
        med.times = request.POST.get("times")
        med.notes = request.POST.get("notes")
        med.save()
        return redirect("meds")
    return render(request,"main/edit_med.html", {
        "med": med,
    })

@login_required(login_url='login')
def delete_med(request, pk):
    med = Medication.objects.get(id=pk)
    if request.method == "POST":
        med.delete()
        return redirect("meds")
    return render(request, "main/delete.html", {
        "med": med,
    })

