from django.shortcuts import render, redirect
from .models import Settings, About, Contact, OperationProcess, Service_Contact
from apps.team.models import Team
from apps.benefits.models import Benefits
from apps.telegram.views import get_text
from apps.service.models import Service

# Create your views here.

def index(request):
    settings = Settings.objects.latest('id')
    services = Service.objects.all().order_by('?')[:4]
    about = About.objects.latest('id')
    benefits = Benefits.objects.all().order_by('?')[:4]
    service_footer = Service.objects.all().order_by('?')[:6]
    benefits_footer = Benefits.objects.all().order_by('?')[:6]
    operetion_all = OperationProcess.objects.all()[:3]
    if request.method =="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        choice = request.POST.get('choice')
        email = request.POST.get('email')
        Service_Contact.objects.create(name=name, phone=phone, choice=choice, email=email)

        get_text(f""" Оставлена заявка на услугу {choice}
Имя пользователя: {name}
Номер телефона: {phone}
email: {email}
""")
        return redirect('index')
    return render(request, "base/index.html",locals())

def about(request):
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    team_about = Team.objects.all().order_by('?')[:4]
    service_footer = Service.objects.all().order_by('?')[:6]
    benefits_footer = Benefits.objects.all().order_by('?')[:6]

    return render(request, "base/about.html",locals())
    
def contact(request):
    settings = Settings.objects.latest('id')
    benefits_footer = Benefits.objects.all().order_by('?')[:6]
    service_footer = Service.objects.all().order_by('?')[:6]
    if request.method =="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        cause = request.POST.get('cause')
        Contact.objects.create(name=name, phone=phone, message=message, cause=cause)

        get_text(f""" Оставлен отзыв 
Имя пользователя: {name}
Номер телефона: {phone}
Причина: {cause}
Сообщение: {message}
""")
        return redirect('index')

    return render(request, "base/contact.html", locals())
