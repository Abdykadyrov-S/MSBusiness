from django.shortcuts import render
from apps.base.models import Settings
from apps.news.models import News
from apps.benefits.models import Benefits

# Create your views here.

def news(request):
    settings = Settings.objects.latest('id')
    news = News.objects.all() 
    benefits_footer = Benefits.objects.all()
    return render(request, "news/news.html",locals())

def news_detail(request,id):
    settings = Settings.objects.latest('id')
    news = News.objects.get(id=id) 
    from apps.benefits.models import Benefits
    benefits_footer = Benefits.objects.all()
    return render(request, "news/news-details.html",locals())