from django.contrib import admin
from django.urls import path
from customers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('complaint/', views.complaint_form),   # 👈 ADD THIS
]
from customers.views import home
path('', home),
