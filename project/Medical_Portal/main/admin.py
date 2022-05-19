from django.contrib import admin
from .models import User, Medication, Posts
# Register your models here.
admin.site.register(User)
admin.site.register(Medication)
admin.site.register(Posts)