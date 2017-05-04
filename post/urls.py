from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', homepage),
    url(r'^post/list/$', post_list),
    url(r'^post/(?P<post_id>\d+)$', post_detail)
]
