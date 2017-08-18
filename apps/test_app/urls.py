from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^main$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^wish_items/(?P<id>\d+)$', views.show),
    url(r'^wish_items/create$', views.new),
    url(r'^wish_items/new/items$', views.create_item),
    url(r'^authentification$', views.authentification),
    url(r'^create$', views.create),
    url(r'^add_item/(?P<id>\d+)$', views.add_wish_item),
    url(r'^remove_item/(?P<id>\d+)$', views.remove_wish_item),
    url(r'^delete/(?P<id>\d+)$', views.delete_item),
    url(r'^logout$', views.logout)
]
