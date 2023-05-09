from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import offer
from . models import news
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import logout
from django.shortcuts import render,get_object_or_404





def index(request,c_slug=None):
    hm=offer.objects.all()
    new=news.objects.all()
    return render(request,'index.html',{'hms':hm, 'news':new})





def details(request,place_id):
    detail=place.objects.get(pk=place_id)
    
    return render(request, 'details.html',{'details':detail})


def register(request):
    if request.method=="POST":
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        pswd=request.POST['pswd']
        pswdrpt=request.POST['pswdrpt']

        if pswd==pswdrpt:
            user=User.objects.create_user(first_name=name, username=username,email=email,password=pswd)
            user.save()
            messages.success(request, 'Registration successfull')
            print("successfully added")
            return redirect('login_user')
        else:
            messages.error(request, 'Something went wrong')
            return render(request, 'register.html')
        
    else:
        return render(request,'register.html')
    
def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        pswd=request.POST['pswd']
        print(username)

        user=auth.authenticate(username=username, password=pswd)
        print(user)

        if user is not None:
            print('working here')
            auth.login(request, user)
            messages.success(request, 'You are logged in successfully')
            print('Successfully loggedin')
            return redirect('/')
        
        else:
            messages.error(request, 'Invalid details')
            return redirect('login_user')
        
    else:
        return render(request, 'login.html')
    

def logout_user(request):
    auth.logout(request)
    return redirect('/')
    


