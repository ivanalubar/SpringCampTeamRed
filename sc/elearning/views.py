from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, EditUserForm, EditUserProfileForm, EditCourseForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Course



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
    userprofile, created = UserProfile.objects.get_or_create(user=request.user, defaults={'user': request.user})
    if request.method == 'POST':
        print(request.__dict__)
        post = request.POST.copy()
        post['user_id'] = request.user.id
        form_user = EditUserForm(instance=request.user, data=post)
        form_userprofile = EditUserProfileForm(data=post, instance=userprofile)
        if form_user.is_valid():
            form_user.save()

            if form_userprofile.is_valid():

                print('I\'m valid!')

                form_userprofile.save()
                return redirect('/registration/profile')
        else:
            print('I\'m not valid!')
            form_user = EditUserForm(instance=request.user)
            form_userprofile = EditUserProfileForm(instance=request.user)
            args = {'form_user': form_user, 'form_userprofile': form_userprofile}
            return render(request, 'registration/edit_profile.html', args)

    else:
        form_user = EditUserForm(instance=request.user)
        form_userprofile=EditUserProfileForm(instance=userprofile)
        args = {'form_user': form_user, 'form_userprofile': form_userprofile}
        return render(request, 'registration/edit_profile.html', args)


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
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'registration/change_password.html', args)


def course(request):
    return render(request, 'registration/course.html')


def list(request):
    return render(request, 'registration/list_of_courses.html')


def bootstrap(request):
    return render(request, 'botstrap/index.html')


def redteam(request):
    return render(request, 'registration/redteam.html')


@login_required
def edit_course(request):
    if request.method == 'POST':
        form_user = EditCourseForm(instance=request.user)
        form_course = EditCourseForm(instance=request.user)
        if form_course.is_valid():
            form_course.save()
            return redirect('/registration/course')
        else:
            form_userprofile = EditCourseForm(instance=request.user)
            args = {'form_course': form_course}
            return render(request, 'registration/edit_course.html', args)

    else:
        form_course = EditCourseForm(instance=request.user)
        form_course = EditCourseForm(instance=request.user)
        args = {'form_course': form_course}
        return render(request, 'registration/edit_course.html', args)



