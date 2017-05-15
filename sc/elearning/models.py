from django.db import models
from django.contrib.auth.models import User, Group
from datetime import date
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


class Program(models.Model):
    name = models.CharField(max_length=256, default='')

class Course(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    level = models.ForeignKey(Group, related_name='level', blank=False, null=False)
    area = models.ForeignKey(Group, related_name='area', blank=False, null=False)
    duration = models.IntegerField(default=0, blank=False, null=False)
    start = models.DateField(blank=False, null=False)
    end = models.DateField(blank=False, null=False)
    number_of_people = models.IntegerField(default=0, blank=False, null=True)
    programmes = models.ManyToManyField(Program, blank=False, null=False)
    professor=models.ManyToManyField(User)


class UserIndex(models.Model):
    user=models.ForeignKey(User)
    grade=models.IntegerField()
    course=models.ForeignKey(Course)
    date = models.DateField()

post_save.connect(create_profile, sender = User)



class Content(models.Model):
    type = models.ForeignKey(Group, on_delete=models.CASCADE)
    data = models.TextField(default='')









