from django.conf.urls import patterns, url

from apuestas import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<usuario_id>\d+)/$', views.usuario, name='usuario'),
)