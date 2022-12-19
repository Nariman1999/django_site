from django.shortcuts import render
from django.db.models import F
from django.views.generic import ListView, DetailView
from . import models
from django.db.models.functions import Lower



def index(request):
    articles = models.Article.objects.all().update(ostatok = 2400 - F('sdal'))
    articles = models.Article.objects.filter(date__year='2022')
    s = 0
    o = 0
    
    for i in articles:
        s = s + i.sdal
        o = o + i.ostatok
        ind =+1
    summ = s
    ost = o
    
    novosts = models.Novosti.objects.order_by('-date_time')[:3]
    context = {
        'articles': articles,
        'summ' : summ,
        'ost' : ost,
        's' : s,
        'novosts' : novosts,
    }
    return render(request, 'main/index.html', context)



def index3(request,pk):
    articles = models.Article.objects.all().update(ostatok = 2400 - F('sdal'))
    a = models.Article.objects.filter(date__year=pk)
    articles = models.Article.objects.filter(date__year=pk)
    s = 0
    o = 0
    
    for i in a:
        s = s + i.sdal
        o = o + i.ostatok
        ind =+1
    summ = s
    ost = o
    
    novosts = models.Novosti.objects.order_by('-date_time')[:3]
    context = {
        'articles': articles,
        'summ' : summ,
        'ost' : ost,
        's' : s,
        'novosts' : novosts,
    }
    return render(request, 'main/index.html', context)


def novosti(request):
    novosts = models.Novosti.objects.order_by('-date_time')[:10]
    context = {
        'novosts' : novosts,
    }
    return render(request, 'main/novosti.html', context)

def detail_novosti(request,pk):
    novosts = models.Novosti.objects.get(id=pk)
    context = {
        'novosts' : novosts,
    }
    return render(request, 'main/detail_novosti.html', context)

def document(request):
    documents = models.Document.objects.filter(boolens = True).order_by('-date_time')
    context = {
        'documents' : documents,
    }
    return render(request, 'main/documents.html', context)


def dohod(request):
    dohods = models.Dohods.objects.order_by('-date')
    articles = models.Article.objects.all()
    # articles_now = models.Article.objects.filter(date__year='2022')
    rashods = models.Rashods.objects.all()
    s = 0
    o = 0
    for i in articles:
        s = s + i.sdal
        o = o + i.ostatok
    summ = s
    ost = o
    
    d = 0
    for i in dohods:
        d = d + i.summa
    drugiy = d

    r = 0
    for i in rashods:
        r = r + i.summr
    ras = r

    obshiy = summ + drugiy 

    itogo = obshiy - ras
    context = {
        'dohods' : dohods,
        'summ' : summ,
        'ost' : ost,
        'drugiy' : drugiy,
        'obshiy' : obshiy,
        'itogo' : itogo,
    }
    return render(request, 'main/dohod.html', context)

  
def rashods(request):
    rashods = models.Rashods.objects.order_by('-date')
    dohods = models.Dohods.objects.all()
    articles = models.Article.objects.all()
    s = 0
    for i in articles:
        s = s + i.sdal
    summ = s

    d = 0
    for i in dohods:
        d = d + i.summa
    drugiy = d

    r = 0
    for i in rashods:
        r = r + i.summr
    ras = r

    obshiy = summ + drugiy

    itogo = obshiy - ras
    context = {
        'rashods' : rashods,
        'obshiy' : obshiy,
        'itogo' : itogo,
        'ras': ras,
    }
    return render(request, 'main/rashod.html', context)
