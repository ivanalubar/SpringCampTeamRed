from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

app_name = 'elearning'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login, {'template_name': 'registration/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'registration/logout.html'}),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),

    url(r'^reset-password/$', password_reset, {'template_name': 'registration/reset_password.html'}, name='reset-password'),
    url(r'^password_reset/done/$', password_reset_done, {'template_name': 'registration/reset_password_done.html'}, name='password_reset_done'),
    url(r'^reset-password/confirm/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),

]