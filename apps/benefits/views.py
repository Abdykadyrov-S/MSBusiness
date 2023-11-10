from django.shortcuts import render
from .models import Benefits
from apps.base.models import Settings
from apps.service.models import Service

# Create your views here.

def benefits(request):
    settings = Settings.objects.latest('id')
    benefits = Benefits.objects.all()
    service_footer = Service.objects.all().order_by('?')[:6]
    return render(request, "benefits/benefits.html",locals())

def benefits_detail(request,id):
    settings = Settings.objects.latest('id')
    benefits = Benefits.objects.get(id=id) 
    service_footer = Service.objects.all().order_by('?')[:6]

    return render(request, "benefits/benefits-detail.html",locals())