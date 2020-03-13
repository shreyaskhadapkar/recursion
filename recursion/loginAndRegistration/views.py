from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request,'index.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('login'))

def login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=name,password=password)
        if user:
            if user.is_active:
                auth_login(request,user)
                return redirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            
    return render(request,'login.html')

def registration(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username,password=password)
        return redirect(reverse('login'))
    return render(request,'registration.html')