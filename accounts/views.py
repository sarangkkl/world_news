from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import logout,login
from .models import author
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def login_page(request):
    return render(request,'accounts/login_page.html')
def signup_page(request):
    return render(request,'accounts/signup_page.html')


def login_handle(request):
    if request.method == "POST":
        username = request.POST.get('your_name')
        password = request.POST.get('your_pass')
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            
            messages.info(request,"You are succefully logged in")
            return redirect('/accounts/author_page') 
        else:
            messages.info(request,"You are not logged in")
            return redirect('/accounts/login_page') 
    else:
        return HttpResponse("Not applicable")


def signup_handle(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass')
        pass2 = request.POST.get('re_pass')
        pass2 = request.POST.get('re_pass')
        check = request.POST.get('agree-term')

        if(pass1 != pass2):
            messages.info(request,"Password does not matches dear")
            return redirect('/accounts/signup_page')
        else:
            x = User.objects.create(email = email,username = email,first_name = name,is_staff = False)
            x.set_password(pass1)
            x.save()
            y = author(user = x,name = name,status = "deactive",email = email)
            y.save()
        # print(f"lets varify the data name = {name},{check}")
        messages.info(request,"Your account has been succesfully created Now Login")
        return redirect('/accounts/login_page')
    else:
        return HttpResponse("Babe something goes wrong")



def logout_handle(request):
    logout(request)
    messages.info(request,"Your Have been logged out succefully")
    return redirect('/accounts/login_page')

@login_required(login_url='accounts/login_page')
def user_dashboard(request):
    return render(request,'accounts/user_dashboard.html')
