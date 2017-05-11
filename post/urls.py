from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', homepage),
    url(r'^post/list/$', post_list),
    url(r'^post/(?P<post_slug>[a-z0-9]+(?:-[a-z0-9]+)*)$', post_detail)
]
