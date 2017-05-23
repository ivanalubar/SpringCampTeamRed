"""sc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from sc import views
from django.conf import settings
from django.conf.urls.static import static

#rest_framework
from rest_framework.urlpatterns import format_suffix_patterns
import elearning.views
from elearning import views

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^elearning/', include('elearning.urls')),
    url(r'^registration/', include('elearning.urls')),
    #url(r'^basic_example/', include('elearning.urls')),
    url(r'^elearning/login/$', auth_views.login, name='login'),
    url(r'^elearning/logout/$', auth_views.logout, name='logout'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #r_f
    url(r'^courses/', views.CourseList.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#rest_framework
#urlpatterns = format_suffix_patterns((urlpatterns))