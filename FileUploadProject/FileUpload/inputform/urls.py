from django.conf.urls import patterns, include, url
from inputform import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_username/$', views.add_username, name='add_username'),)
