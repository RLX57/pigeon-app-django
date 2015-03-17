from django.conf.urls import patterns, include, url
from django.contrib import admin
from feed import views

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^tweet/$', views.tweet, name='tweet'),
)
