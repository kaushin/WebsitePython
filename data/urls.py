from django.conf.urls import url
from . import views

app_name = 'data'

urlpatterns = [
    # /data/
    url(r'^$', views.index, name='index'),

    # /data/12/
    url(r'^(?P<matchid>[0-9]+)$', views.detail, name='detail'),

    # /data/12/mark/
    url(r'^flip_win/$', views.flip_win, name='flip_win'),

    url(r'^data/add/$', views.MatchCreate.as_view(),name='match-add'),
]