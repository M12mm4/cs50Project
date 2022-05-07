from .models import User, Medication
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
class UserRegister(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#class MedicationAdd(ModelForm):
 #   class Meta:
  #      model = Medication
   #     fields =  ['name', 'times', 'note']