from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    number_of_people = models.CharField(max_length=50)


class Content(models.Model):
    type = models.CharField(max_length=50)


class User(models.Model):
    type = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Groups(models.Model):
    type = models.CharField(max_length=50)


class Program(models.Model):
    name = models.CharField(max_length=50)


