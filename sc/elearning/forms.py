from django.contrib.auth.models import User
from django.forms import ModelForm, widgets, CharField, Form, PasswordInput, models
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

#class UserForm(ModelForm):

   # class Meta:
      #  model = forms.NasUser
      #  fields = ('username', 'email', 'password','first_name', 'last_name','group')

class LoginForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput())

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )
        # moze ici i preko ovog - > exclude = ()


#class CourseForm(ModelForm):
    #class Meta:
    # model = forms.Course


#  fields = ('name', 'start', 'duration', 'level', 'area', 'end', 'number_of_people', 'programmes')

#class ProgrammeForm(ModelForm):
    #   class Meta:
    #   model = ModelForm.Programme
    #   fields = ('name')