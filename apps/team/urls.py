from django.urls import path
from .views import team, team_single

urlpatterns = [
    path('team/',team, name="team" ),
    path('team-single/<int:id>/', team_single, name="team-single"),
]