from django.core import paginator
from . models import Product
from django.shortcuts import render,get_object_or_404
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator
from taggit.models import Tag

def Product_ListView(request,tag_slug=None):
    product_list=Product.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        product_list=product_list.filter(tags__in=[tag])
    paginator=Paginator(product_list,4)
    page_number=request.GET.get('page')
    try:
        product_list=paginator.page(page_number)
    except PageNotAnInteger:
        product_list=paginator.page(1)
    except EmptyPage:
        product_list=paginator.page(paginator.num_pages)        
    return render(request,'bmart/home.html',{'product_list':product_list,'tag':tag})

def Pelectronic_view(request,tag_slug=None):
    product_list=Product.objects.filter(product1__icontains='electronics')
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        product_list=product_list.filter(tags__in=[tag]) 
    paginator=Paginator(product_list,4)
    page_number=request.GET.get('page')
    try:
        product_list=paginator.page(page_number)
    except PageNotAnInteger:
        product_list=paginator.page(1)
    except EmptyPage:
        product_list=paginator.page(paginator.num_pages) 
    return render(request,'bmart/electronics.html',{'product_list':product_list})

def Pfashion_view(request,tag_slug=None):
    product_list=Product.objects.filter(product1__icontains='fashion')
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        product_list=product_list.filter(tags__in=[tag]) 
    paginator=Paginator(product_list,4)
    page_number=request.GET.get('page')
    try:
        product_list=paginator.page(page_number)
    except PageNotAnInteger:
        product_list=paginator.page(1)
    except EmptyPage:
        product_list=paginator.page(paginator.num_pages) 
    return render(request,'bmart/fashion.html',{'product_list':product_list})    

