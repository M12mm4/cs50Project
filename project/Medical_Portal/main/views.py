from django.shortcuts import render, redirect
from .models import Medication, User, Posts
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
    form = UserRegister()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'main/register.html', {'form': form})


"""################ Medicatio CRUD ################"""



@login_required(login_url='login')
def add_med(request):
    if request.method == "POST":
        name = request.POST.get("medicine")
        times = request.POST.get("times")
        notes = request.POST.get("notes")

        if not name or not times or not notes:
            return messages.warning(request, "You Should fill every field", )
        
        current_user = request.user
        Medication.objects.create(
            patient = current_user,
            name = name,
            times = times,
            notes = notes,
        )

        return redirect("meds")
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

"""################### Posts Page ###################"""

@login_required(login_url='login')
def posts(request):
    posts = Posts.objects.all()

    return render(request, "main/posts.html", {
        "posts": posts,
    })



@login_required(login_url='login')
def add_post(request):
    current_user = request.user

    if request.method == "POST":
        diagnosis = request.POST.get("diagnosis")
        symptoms = request.POST.get("symptoms")
        notes = request.POST.get("notes")
        medications = request.POST.get("medications")

        if not notes or not symptoms or not diagnosis:
            messages.warning(request, "You should fill every field")

        Posts.objects.create(
            author = current_user,
            diagnosis = diagnosis,
            symptoms = symptoms,
            Notes = notes, 
            medications = medications
        ) 

        return redirect("posts")
    return render(request, "main/add_post.html")