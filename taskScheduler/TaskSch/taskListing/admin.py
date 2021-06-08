from django.contrib import admin
from django.contrib.auth.models import User
from .models import Appointment
# Register your models here.

class AppontmentTable(admin.ModelAdmin):
    list_display = ('timestamp', 'description')

admin.site.register(Appointment, AppontmentTable)