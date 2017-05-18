from django.contrib.auth.models import User, Group
from django.forms import ModelForm, widgets, CharField, Form, PasswordInput, models
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Course, UserProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.type = Group.objects.get(name='student')
            user.save()
        return user



class LoginForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput())

class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
        )
class EditUserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'description',
            'phone',
            'city',
            'image'
        )

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'level', 'area', 'duration', 'start', 'end', 'number_of_people', 'programmes', 'professor')



#  fields = ('name', 'start', 'duration', 'level', 'area', 'end', 'number_of_people', 'programmes')

#class ProgrammeForm(ModelForm):
    #   class Meta:
    #   model = ModelForm.Programme
    #   fields = ('name')