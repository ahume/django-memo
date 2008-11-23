"""
URLConf for django-memo.

Recommended usage is a call to ``include()`` in your project's root
URLConf to include this URLConf for any URL beginning with
``/memos/``.
"""

from django.conf.urls.defaults import *
from memo import views

urlpatterns = patterns('',
                      (r'^$', views.user_inbox),
                      (r'^(?P<pk>[^/]+)/del/$', views.memo_delete),
                       )