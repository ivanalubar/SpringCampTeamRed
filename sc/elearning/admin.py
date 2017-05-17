from django.contrib import admin
from .models import  Course, Content, UserProfile, Program, UserIndex


# Register your models here.
#admin.site.site_header='Administration'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'phone','description')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('phone')
        return queryset

     #user_info.short_description = 'Info'


class IndexUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'grade', 'course', 'date']
    def get_queryset(self, request):
        queryset = super(IndexUserAdmin, self).get_queryset(request)
        queryset = queryset.order_by('grade')
        return queryset


admin.site.register(Program)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Course)
admin.site.register(Content)
admin.site.register(UserIndex)