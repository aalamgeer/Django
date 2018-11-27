from django.conf.urls import url
from .import views
app_name = 'myapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #movie/ a.id
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    #movie/id/favorite
    url(r'^(?P<movie_id>[0-9]+)/favorite/', views.favorite, name='favorite'),
]
