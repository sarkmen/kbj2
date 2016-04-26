from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', 'blog.views.post_detail', name='post_detail'),
    url(r'^new/$', 'blog.views.post_new', name='post_new'),
    url(r'^(?P<pk>\d+)/edit/$', 'blog.views.post_edit', name='post_edit'),

]