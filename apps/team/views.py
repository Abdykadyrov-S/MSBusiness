from django.shortcuts import render, redirect
from apps.base.models import Settings
from .models import Team
from apps.telegram.views import get_text_doctor
from apps.benefits.models import Benefits
from apps.service.models import Service


# Create your views here.
def team(request):
    settings = Settings.objects.latest("id")
    team = Team.objects.all()
    benefits_footer = Benefits.objects.all().order_by('?')[:6]
    service_footer = Service.objects.all().order_by('?')[:6]

    return render(request, "team/team.html",locals())

def team_single(request, id):
    team = Team.objects.get(id=id)
    settings = Settings.objects.latest('id')
    benefits_footer = Benefits.objects.all().order_by('?')[:6]
    service_footer = Service.objects.all().order_by('?')[:6]

    return render (request, "team/team-single.html", locals())