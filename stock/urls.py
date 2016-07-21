from django.conf.urls import url
from stock import views

urlpatterns = [
    url(r'^stocks/$', views.stock_list),
    url(r'^stocks/(?P<pk>[0-9]+)/$', views.stock_detail),
]