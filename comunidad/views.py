from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .decorators import unauthenticated_user, allowed_users, admin_only
from .models import *
from .forms import *


def comunidad(request):
    users = User.objects.all()
    comunidades = Comunity.objects.all()
    empresas = Company.objects.all()
    
    context = {'title': 'Comunidad', 'users':users, 'comunidades':comunidades, 'empresas':empresas}
    return render(request, 'comunidad/comunidad.html', context)


# --------------- USUARIOS LOGS ------------------
def peopleRegister(request):
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        profile_form= ProfileForm(request.POST, request.FILES)

        regEmail = request.POST.get('inputmail')
        phone = request.POST.get('phone')
        
        if user_form.is_valid and profile_form.is_valid:
            # user = user_form.save()
            group = Group.objects.get(name='user')
            # user.groups.add(group)
            # user.save()
            userprofile = profile_form.save(commit=False)

            num = str(profile_form.cleaned_data.get('phone'))
            if len(num) == 10:
                phoneNum = ("("+num[:3]+")"+num[3:6]+"-"+num[6:])

            userprofile.phone = phoneNum
            userprofile.save()
            messages.success(request, f'La cuenta fue creada, ya puedes Iniciar sesión!')
            return redirect('main')
        else:
            messages.warning(request, f'Algo no salio bien, Intentalo otra vez porfa!')
            return redirect('peopleRegister')
    else:
        user_form = CreateUserForm()
        profile_form= ProfileForm()
    
    context = {'title':'Registro', 'user_form':user_form, 'profile_form':profile_form}
    return render(request, 'comunidad/people/peopleRegister.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Algo no salio bien, Intentalo de nuevo')

    context = {'title':'Login'}
    return render(request, 'comunidad/people/login.html', context)


def userLogout(request):
    logout(request)
    messages.info(request, 'Gracias por tu visita, Te estaremos esperando!')
    return redirect('/')


@login_required
def profile(request, pk):
    user = get_object_or_404(User, id=pk)

    context = {'title':'Usuario', 'user':user}
    return render(request, 'comunidad/people/profile.html', context)


@admin_only
def allusers(request):

    context = {'title':'Todos los Usuarios'}
    return render(request, 'comunidad/people/allusers.html', context)


# --------------- COMUNIDADES ---------------
def comunity(request):
    comunidades = Comunity.objects.all()
    
    context = {'title': 'Comunity', 'comunidades':comunidades}
    return render(request, 'comunidad/comunity/comunity.html', context)


def comunityRegister(request):
    if request.method == 'POST':
        form = ComunityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('comunity')
    else:
        form = ComunityForm()

    context = {'title': 'Registro de Comunity', 'form':form}
    return render(request, 'comunidad/comunity/comunityRegister.html', context)


def comunityProfile(request, pk):
    comunity = get_object_or_404(Comunity, id=pk)

    context = {'title':'Comunity', 'comunity':comunity}
    return render(request, 'comunidad/comunity/comunityProfile.html', context)


# --------------- EMPRESAS ------------------
def company(request):
    empresas = Company.objects.all()
    
    context = {'title': 'Empresas', 'empresas':empresas}
    return render(request, 'comunidad/company/company.html', context)


def companyRegister(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('company')
    else:
        form = CompanyForm()

    context = {'title': 'Registro de Empresas', 'form':form}
    return render(request, 'comunidad/company/companyRegister.html', context)


def companyProfile(request, pk):
    empresa = get_object_or_404(Company, id=pk)

    context = {'title':'Comunity', 'empresa':empresa}
    return render(request, 'comunidad/company/companyProfile.html', context)
