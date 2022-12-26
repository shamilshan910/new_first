from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import tab1,tab2
from django.contrib import messages, auth


# Create your views here.
def geting(request):
    obj=tab1.objects.all()
    obj2 = tab2.objects.all()
    return render(request, "index.html",{'result':obj,'result2':obj2})

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
           if User.objects.all().filter(username=username).exists():
               messages.info(request,"username already taken")
               return redirect('register')

           elif User.objects.all().filter(email=email).exists():
               messages.info(request,"email already taken")
               return redirect('register')
           else:
               user1=User.objects.create_user(username=username,
                                               email=email,
                                               password=password,first_name=first_name,last_name=last_name)
               user1.save()
               return redirect('login')

        else:
            messages.info(request,"password didnt matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register2.html')
def login(request):
    if request.method=='POST':
        user = request.POST['user']
        password = request.POST['password']
        user=auth.authenticate(username=user,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid input")
            return redirect('login/')
    return render(request,'login.html')

