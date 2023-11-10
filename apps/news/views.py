from django.shortcuts import render
from apps.base.models import Settings
from apps.news.models import News
from apps.benefits.models import Benefits
from apps.service.models import Service

# Create your views here.

def news(request):
    settings = Settings.objects.latest('id')
    news = News.objects.all() 
    service_footer = Service.objects.all().order_by('?')[:6] 
    benefits_footer = Benefits.objects.all().order_by('?')[:6]
    return render(request, "news/news.html",locals())

def news_detail(request,id):
    settings = Settings.objects.latest('id')
    news = News.objects.get(id=id) 
    service_footer = Service.objects.all().order_by('?')[:6]
    benefits_footer = Benefits.objects.all().order_by('?')[:6]
    return render(request, "news/news-details.html",locals())