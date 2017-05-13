from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

app_name = 'elearning'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^', views.signup, name='signup'),
    url(r'^$', login, name='login'),
   ]