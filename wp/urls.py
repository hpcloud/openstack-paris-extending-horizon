from django.conf.urls import patterns, url
from wp import views

INDEX_URL = r'^$'
CREATE_URL = r'^create'
# DELETE_URL = r'^(?P<post_id>[^/]+)/%s$' % 'delete'
# DETAIL_URL = r'^(?P<instance_id>[^/]+)/$'

urlpatterns = patterns('horizon.dashboards.project.wp.views',
    url(INDEX_URL, views.PostIndexView.as_view(), name='index'),
    url(CREATE_URL, views.PostCreateView.as_view(), name='create'),
    # url(DELETE_URL, views.PostDeleteView.as_view(), name='delete'),
    # url(CLUSTER_DETAIL_URL, views.DetailView.as_view(), name='detail'),
)
