from django.conf.urls import url
from . import views

app_name = 'booktest'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^booklist/$', views.list, name='list'),
    url(r'^bookdetail/(\d+)/$', views.detail, name='detail'),
]
