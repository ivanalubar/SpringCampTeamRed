from django.contrib import admin
from elearning.models import  Course, Content, UserProfile,Program


# Register your models here.

admin.site.register(Program)
admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Content)
