from django.shortcuts import render
from apps.base.models import Settings
from apps.service.models import Service
from apps.benefits.models import Benefits


# Create your views here.
def services(request):
    settings = Settings.objects.latest('id')
    service = Service.objects.all() 
    benefits_footer = Benefits.objects.all().order_by('?')[:6]
    service_footer = Service.objects.all().order_by('?')[:6]

    return render(request, "service/services.html",locals())

def services_detail(request,id):
    service_footer = Service.objects.all().order_by('?')[:6]
    settings = Settings.objects.latest('id')
    services = Service.objects.get(id=id)
    benefits_footer = Benefits.objects.all().order_by('?')[:6]
    return render(request, "service/service-details.html",locals())