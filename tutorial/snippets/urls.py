#!/usr/bin/env python
# -*- coding: utf-8 -*-

# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# from django.conf.urls import patterns, url
# from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = patterns('snippets.views',
#     url(r'^snippets/$', 'snippet_list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
# )

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = patterns('',
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)