from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from elearning.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'registration/home.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/elearning/')
    else:
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'registration/registration.html', args)

def login(request):
    return render(request, 'registration/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'registration/profile.html')

@login_required
def edit_profile(request):
    if request.method =='POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/registration/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/edit_profile.html',args)

@login_required
def change_password(request):
    if request.method== 'POST':
        form = PasswordChangeForm(data = request.POST, user =request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/registration/profile')
        else:
            return redirect('/registration/change_password')


    else:
        form = PasswordChangeForm(user =request.user)
        args = {'form': form}
        return render(request, 'registration/change_password.html', args)
