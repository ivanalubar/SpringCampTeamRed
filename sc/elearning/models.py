from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.

class Groups(models.Model):
    type = models.CharField(max_length=50)

class NasUser(User):
    type = models.ForeignKey(Groups, on_delete=models.CASCADE)


class Program(models.Model):
    name = models.ForeignKey(Groups, on_delete=models.CASCADE)


class Course(models.Model):
    name = models.CharField(max_length=256)
    level = models.ForeignKey(Groups, related_name='level')
    area = models.ForeignKey(Groups, related_name='area')
    duration = models.IntegerField(default=0)
    start = models.DateField()
    end = models.DateField()
    number_of_people = models.IntegerField(default=0)
    programmes = models.ManyToManyField(Program)


class Content(models.Model):
    type = models.ForeignKey(Groups, on_delete=models.CASCADE)








