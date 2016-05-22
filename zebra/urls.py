from django.conf.urls import patterns, url

from zebra import views

urlpatterns = [
    url(r'webhooks/$',    views.webhooks,    name='webhooks'),
    url(r'webhooks/v2/$', views.webhooks_v2, name='webhooks_v2'),
]
