from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Complaint   # 👈 add Complaint here

admin.site.register(Customer)
admin.site.register(Complaint)            # 👈 add this line
