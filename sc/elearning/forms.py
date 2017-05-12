from django.contrib.auth.models import User
from django.forms import ModelForm, widgets, CharField, Form, PasswordInput, models


class UserForm(ModelForm):

    class Meta:
        model = models.NasUser
        fields = ('username', 'email', 'password','first_name', 'last_name','group')

class LoginForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput())

class CourseForm(ModelForm):
    class Meta:
        model = models.Course
        fields = ('name', 'start', 'duration', 'level', 'area', 'end', 'number_of_people', 'programmes')

class ProgrammeForm(ModelForm):
    class Meta:
        model = models.Programme
        fields = ('name')