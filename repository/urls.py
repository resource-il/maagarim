from django.conf.urls import url, include
from . import views

owner_patterns = [
    url(r'^$', views.owner_index, name='index'),
    url(r'^(?P<owner_id>\d+)/$', views.owner_view, name='view'),
]

urlpatterns = [
    url(r'^$', views.repository_index, name='index'),
    url(r'^(?P<repository_id>\d+)/$', views.repository_view, name='view'),
    url(r'^owner/', include(owner_patterns, namespace='owner')),
]
