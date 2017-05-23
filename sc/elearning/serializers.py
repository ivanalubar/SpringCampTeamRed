from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Course

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('name', 'level', 'area', 'duration', 'start', 'end',
                  'number_of_people', 'description', 'professor', 'content')
        #fields = '__all__'