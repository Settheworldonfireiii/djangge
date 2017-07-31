# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404
from startup.models import Category, Good
from django.core.paginator import *



def index(request, cat_id):
    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num =  1   
    cats = Category.objects.all().order_by("name")
    if cat_id == None:
      cat = Category.objects.first()
    else:
      try:  
        cat =  Category.objects.get(pk = cat_id)
      except Category.DoesNotExist:
        raise Http404  
    paginator = Paginator( Good.objects.filter(category =  cat).order_by("name"), 10)    
    try:
        goods = paginator.page(page_num)
    except InvalidPage:
        goods = paginator.page(1) 
    #goods = Good.objects.filter(category =  cat).order_by("name")    
    return render(request, "index.html", {"category":cat, "cats":cats, "goods":goods})         





def good(request, good_id):
    try:
        page_num = request.GET["page"]
    except:
        page_num = 1    
    cats =Category.objects.all().order_by("name")
    try:
      good = Good.objects.get(pk = good_id)
    except Good.DoesNotExist:
      raise Http404     
    s = good.name + "<br><br>" + good.category.name + "<br><br>" + good.description
    return render(request, "good.html", {"good":good, "cats":cats, "pn":page_num})    
# Create your views here.



def catlist(request):
  cats = Category.objects.all()
  cats.order_by("name") 
  s = "Сьпiс катэгорый бля" + "<br>"
  for cat in cats:
    s = s + cat.name + "<br>" 
  return HttpResponse(s)
        