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
    name = models.CharField(max_length=256)
    level = models.ForeignKey(Group, related_name='level')
    area = models.ForeignKey(Group, related_name='area')
    duration = models.IntegerField(default=0)
    start = models.DateField()
    end = models.DateField()
    number_of_people = models.IntegerField(default=0)
    programmes = models.ManyToManyField(Program)


class Content(models.Model):
    type = models.ForeignKey(Group, on_delete=models.CASCADE)








