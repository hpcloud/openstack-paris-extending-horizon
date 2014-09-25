from django.conf.urls import patterns, url
from wp import views

INDEX_URL = r'^$'
# CREATE_URL = r'^create'
# DELETE_URL = r'^(?P<instance_id>[^/]+)/%s$' % 'delete'
# DETAIL_URL = r'^(?P<instance_id>[^/]+)/$'

urlpatterns = patterns('horizon.dashboards.project.wordpress.views',
    url(INDEX_URL, views.IndexView.as_view(), name='index'),
    # url(CLUSTER_CREATE_URL, views.CreateClusterView.as_view(), name='create'),
    # url(CLUSTER_DELETE_URL, views.DeleteClusterView.as_view(), name='delete'),
    # url(CLUSTER_DETAIL_URL, views.DetailView.as_view(), name='detail'),
)
