from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
# Create your views here.
@login_required(login_url='/login/')
def recipes(request):
    if request.method=='POST':
        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        recipe_image=request.FILES.get('recipe_image')
        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image
        )
        return redirect('/recipes/')
    queryset=Recipe.objects.all()
    if request.GET.get('search'):
        queryset=queryset.filter(recipe_name__icontains=request.GET.get('search'))

    context={'recipes':queryset}
    return render(request,'recipe.html',context)

def delete_recipes(request,id):
    queryset=Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')

def update_recipes(request,id):
    queryset=Recipe.objects.get(id=id)
    if request.method=='POST':
        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        recipe_image=request.FILES.get('recipe_image')
        queryset.recipe_name=recipe_name
        queryset.recipe_description=recipe_description
        if recipe_image:
            queryset.recipe_image=recipe_image
        queryset.save()
        return redirect('/recipes/')
    context={'recipes':queryset}
    return render(request,'updaterecipe.html',context)


def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not  User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')

        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,"Invalid password")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/recipes/')

    return render(request,"login.html")

def register_page(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"Username already exists")
            return redirect('/register/')


        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,

        )
        user.set_password(password)
        user.save()
        messages.info(request,"Account successfully created")
        return redirect('/register/')
    return render(request,'register.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

from django.db.models import Q,Sum 
def get_students(request):
    queryset=Student.objects.all()
    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(
            Q(student_name__icontains=search)|
            Q(department__department__icontains=search)|
            Q(student_age__icontains=search)|
            Q(student_email__icontains=search)|
            Q(student_address__icontains=search)
            )


    paginator = Paginator(queryset, 20)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    return render(request,'student.html',{'queryset':page_obj})

from .seed import generate_report_card
def see_marks(request,student_id):
    queryset=SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    # ranks=Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks','-student_age')
    # current_rank=-1
    # i=1
    # for rank in ranks:
    #     if student_id==rank.student_id.student_id:
    #         current_rank=i
    #         break
    #     i=i+1
    total_marks=queryset.aggregate(total_marks=Sum('marks'))
    
    return render(request,'see_marks.html',{'queryset':queryset,'total_marks':total_marks})