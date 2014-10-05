from django.conf.urls import patterns, url
from wp import views

INDEX_URL = r'^$'
CREATE_URL = r'^create'

urlpatterns = patterns('horizon.dashboards.project.wp.views',
    url(INDEX_URL, views.PostIndexView.as_view(), name='index'),
    url(CREATE_URL, views.PostCreateView.as_view(), name='create'),
)
