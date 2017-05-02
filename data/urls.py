from django.conf.urls import url
from . import views

app_name = 'data'

urlpatterns = [
    # /data/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /data/12/
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
    # /data/12/mark/
    url(r'^flip_win/$', views.flip_win, name='flip_win'),
    # /data/add/
    url(r'^add/$', views.MatchCreate.as_view(),name='match-add'),
    # /data/update/2/
    url(r'^update/(?P<pk>[0-9]+)/$', views.MatchUpdate.as_view(),name='match-update'),
    # /data/add/
    url(r'^(?P<pk>[0-9]+)/delete/$', views.MatchDelete.as_view(),name='match-delete'),
]