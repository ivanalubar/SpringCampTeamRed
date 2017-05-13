from django.db import models
from django.contrib.auth.models import User, Group
from datetime import date


# Create your models here.

#class Groups(Group):
    #type = models.CharField(max_length=50)

class NasUser(User):
    type = models.ForeignKey(Group, on_delete=models.CASCADE)


class Program(models.Model):
    name = models.ForeignKey(Group, on_delete=models.CASCADE)


class Course(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    level = models.ForeignKey(Group, related_name='level', blank=False, null=False)
    area = models.ForeignKey(Group, related_name='area', blank=False, null=False)
    duration = models.IntegerField(default=0, blank=False, null=False)
    start = models.DateField(blank=False, null=False)
    end = models.DateField(blank=False, null=False)
    number_of_people = models.IntegerField(default=0, blank=False, null=True)
    programmes = models.ManyToManyField(Program, blank=False, null=False)


class Content(models.Model):
    type = models.ForeignKey(Group, on_delete=models.CASCADE)








