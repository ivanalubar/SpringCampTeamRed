from django.contrib import admin
from elearning.models import NasUser, Program, Course, Content


# Register your models here.


admin.site.register(NasUser)
admin.site.register(Program)
admin.site.register(Course)
admin.site.register(Content)
