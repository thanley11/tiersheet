from django.conf.urls import patterns, url

from tiersheet import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^toggleStar/$', views.toggleStar, name='toggleStar'),
    #url(r'^(?P<player_id>\d+)/$', views.detail, name='detail'),
]
