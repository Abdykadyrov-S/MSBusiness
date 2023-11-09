
from django.urls import path
from .views import services, services_detail

urlpatterns = [
    path('services/', services, name="services"),
    path('services_detail/<int:id>/', services_detail, name="services_detail"),
]