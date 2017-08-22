from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import *
from .models import Visitor

# Create your views here.

def login(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            print("ERROR DE AUTENTICACION...")
            return render(request,'login.html', {'error':True})
    else:
        return render(request, 'login.html', {})


def logout(request):
    auth_logout(request)
    return render(request, 'logout.html', {})


def noAccess(request):
    return render(request, 'noAccess.html', {})


@login_required(login_url='login')
def home(request):
    role = request.user.profile.role.name
    return render(request, 'home.html', {'role': role})

def body_check(user):
    return user.profile.role.name == "Guardia"

def resident_check(user):
    return user.profile.role.name == "Residente"

@login_required()
@user_passes_test(body_check,'noAccess')
def body_view(request):
    if request.method == 'GET':
        visitors = Visitor.objects.all()
        return render(request, 'visitorsList.html', {'role':request.user.profile.role.name, 'visitors':visitors})

@login_required()
@user_passes_test(resident_check,'noAccess')
def resident_view(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VisitorForm()
    return render(request,'baseform.html', {"role":request.user.profile.role.name,"form":form})
    