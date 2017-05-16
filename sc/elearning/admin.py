from django.contrib import admin
from elearning.models import  Course, Content, UserProfile,Program


# Register your models here.



#admin.site.site_header='Administration'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info','city','phone')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('phone')
        return queryset

    user_info.short_description = 'Info'

admin.site.register(Program)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Course)
admin.site.register(Content)