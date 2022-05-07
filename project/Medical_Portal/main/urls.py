from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('meds/', views.meds, name='meds'),
    path('Login/', views.login_page, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register_user, name='register')
]