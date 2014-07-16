from django.conf.urls import patterns, url

from tiersheet import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # eg: /entries/5/
    #url(r'^(?P<player_id>\d+)/$', views.detail, name='detail'),
)
