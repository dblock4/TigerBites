from django.conf.urls import patterns, url
from menus import views

urlpatterns = patterns('', 
                       url(r'^$', views.index, name = 'index'),
                       url(r'^suggestion', views.suggestion, name = 'suggestion')
                       )
