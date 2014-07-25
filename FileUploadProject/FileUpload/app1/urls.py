from django.conf.urls import patterns, include, url
from app1 import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'))
