from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.listing, name="item-listing"),
    url(r'^list$', views.lists, name="item-lists"),
    url(r'^add$', views.add, name="item-add"),
    url(r'^delete/(?P<id>\w{0,50})/$', views.delete, name="delete"),
    url(r'^update/(?P<itemId>\w{0,50})/$', views.update, name="update"),
]
