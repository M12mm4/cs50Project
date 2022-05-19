from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('meds/', views.meds, name='meds'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register_user, name='register'),
    path('AddMedication/', views.add_med, name='add_meds'),
    path('EditMedication/<str:pk>/', views.edit_medication, name='edit_med'),
    path('DeleteMedication/<str:pk>/', views.delete_med, name='delete_med'),

    ############### Posts Urls ###########################
    path('posts/', views.posts, name='posts'), 
    path('posts/AddPost', views.add_post, name='add_post')


]