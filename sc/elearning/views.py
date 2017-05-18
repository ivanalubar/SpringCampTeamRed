from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, EditUserForm, EditUserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

#@login_required
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


@login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'registration/profile.html')

@login_required
def edit_profile(request):
    if request.method =='POST':
        form_user = EditUserForm(instance=request.user)
        form_userprofile = EditUserProfileForm(instance=request.user)
        if form_user.is_valid() and form_userprofile.is_valid():
            form_user.save()
            form_userprofile.save()
            return redirect('/registration/profile')
        else:
            form_user = EditUserForm(instance=request.user)
            form_userprofile = EditUserProfileForm(instance=request.user)
            args = {'form_user': form_user, 'form_userprofile': form_userprofile}
            return render(request, 'registration/edit_profile.html', args)

    else:
        form_user = EditUserForm(instance=request.user)
        form_userprofile=EditUserProfileForm(instance=request.user)
        args = {'form_user': form_user, 'form_userprofile': form_userprofile}
        return render(request, 'registration/edit_profile.html',args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
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

def course(request):
    args = {'course': request.user.course}
    return render(request, 'registration/course.html')

def list(request):
    return render(request, 'registration/list_of_courses.html')

def bootstrap(request):
    return render(request, 'botstrap/index.html')