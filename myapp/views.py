from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import *


# Create your views here.

def cybervision(request):
    return render(request,"cybervision.html")

def chooseoption(request):
    return render(request,"chooseoption.html")


def datasetprivate(request):
    return render(request,"datasetprivate.html")


def datasetpublic(request):
    return render(request,"datasetpublic.html")



def camerapublic1(request):
    return render(request,"camerapublic1.html")


def camerapublic2(request):
    return render(request,"camerapublic2.html")


def camerapublic3(request):
    return render(request,"camerapublic3.html")


def camerapublic4(request):
    return render(request,"camerapublic4.html")




def cameraprivate1(request):
    return render(request,"cameraprivate1.html")


def cameraprivate2(request):
    return render(request,"cameraprivate2.html")


def cameraprivate3(request):
    return render(request,"cameraprivate3.html")


def cameraprivate4(request):
    return render(request,"cameraprivate4.html")



def geotrack(request):
    return render(request,"geotrack.html")




# def dataset(request):
#     return render(request,"dataset.html")

def signup(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('confirm_password')
        en=Word(text=uname)
        en.save()
        if User.objects.filter(username=uname).exists():
            messages.error(request,'Username already exits!!')
            return redirect('signup')
        if password!=cpassword: 
            return redirect('signup')
        else:    
            my_user=User.objects.create_user(uname,email,password)
            my_user.save()
        return redirect('signin')

    return render(request,"signup.html")

def signin(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('afterlogin')
        else:
            return redirect('signin')

    return render(request,"signin.html")

def error_404(request,exception):
    return render(request,"404.html")

def afterlogin(request):
    us=Word.objects.last()
    return render(request,"afterlogin.html",{'us':us})

def cameraperson(request):
    if request.method == 'POST':
        text=request.POST.get('name')
        email=request.POST.get('email')
        cameracompany=request.POST.get('cameracompany')
        latitude=request.POST.get('latitude')
        longitude=request.POST.get('longitude')        
        range=request.POST.get('range')
        location=request.POST.get('location')
        pincode=request.POST.get('pincode')
        mobile=request.POST.get('mobile')
        ece=UserDataCompany(text=text,email=email,cameracompany=cameracompany,phone=mobile,latitude=latitude,longitude=longitude,range=range,location=location,pincode=pincode)
        ece.save()
        return redirect('signin')
        
    return render(request,"cameraperson.html")
