from django.shortcuts import render
from .models import Projects
from apps.base.models import Settings
from apps.benefits.models import Benefits
from apps.service.models import Service


# Create your views here.

def projects(request):
    settings = Settings.objects.latest('id')
    projects = Projects.objects.all()
    benefits_footer = Benefits.objects.all().order_by('?')[:6]
    service_footer = Service.objects.all().order_by('?')[:6]

    return render(request, "our_project/our-project.html",locals())

def projects_detail(request,id):
    settings = Settings.objects.latest('id')
    projects = Projects.objects.get(id=id)
    benefits_footer = Benefits.objects.all().order_by('?')[:6]
    service_footer = Service.objects.all().order_by('?')[:6]

    return render(request, "our_project/project-detail.html",locals())