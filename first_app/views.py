from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Hello world")

def success_page(request):
    return HttpResponse("<h1>Hey this is a success page </h1>")

def index(request):
    peoples=[
        {'name':'anushika','age':23},
        {'name':'pratush','age':20},
        {'name':'abc','age':15},
        {'name':'def','age':20},
        {'name':'qwer','age':14},
        {'name':'deepanshu','age':22}
    ]
    return render(request,'index.html',{'peoples':peoples})

def index1(request):
    peoples=[
        {'name':'anushika','age':23},
        {'name':'pratush','age':20},
        {'name':'abc','age':15},
        {'name':'def','age':20},
        {'name':'qwer','age':14},
        {'name':'deepanshu','age':22}
    ]
    return render(request,'index1.html',{'peoples':peoples,'page':'Django Tutorial'})

def contact(request):
    
    return render(request,'contact.html',{'page':'contact'})
def about(request):
    
    return render(request,'about.html',{'page':'about'})