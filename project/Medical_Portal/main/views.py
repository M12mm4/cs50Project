from django.shortcuts import render
from .models import Medication
# Create your views here.
def home(request):
    return render(request, "main/index.html")

def meds(request):
    meds = Medication.objects.all()
    return render(request, "main/user_meds.html", {
        "meds": meds,
    })