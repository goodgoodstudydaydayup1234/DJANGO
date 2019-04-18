from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.list),
    url(r'^detail/(\d+)/$', views.detail),
    url(r'^result/$', views.result),

]


