# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from movie_s import savedata
from models import DyModels

# Create your views here.
def index(request,page=0):
    page = int(page)
    if page > 1:
        return render(request,'index.html',context={'model_list':DyModels.objects.all()[(page-1)*15:page*15],'up':page+1,'down':page-1})
    else:
        return render(request,'index.html',context={'model_list':DyModels.objects.all()[:15],'up':page+1,'down':page-1})

def pa(request):
    savedata()
    return HttpResponse('ok')

def movie(request,id):
    model = DyModels.objects.get(id=id)
    return render(request,'content.html',context={'title':model.title,'content':model.content,'link':model.link})
