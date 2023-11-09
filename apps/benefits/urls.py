from django.urls import path

from .views import benefits, benefits_detail

urlpatterns = [
    path('benefits/', benefits, name="benefits"),
    path('benefits_detail/<int:id>/', benefits_detail, name="benefits_detail"),
]