from django.urls import path

from .views import projects, projects_detail

urlpatterns = [
    path('projects/', projects, name="projects"),
    path('projects_detail/<int:id>/', projects_detail, name="projects_detail"),
]