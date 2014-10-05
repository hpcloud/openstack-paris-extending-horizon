import traceback

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render

from horizon import exceptions, tables, workflows, forms, tabs

from wp.tables import PostsTable
from wp.post.post import Post
from wp import utils
from wp.workflows.create_post import CreatePost

class PostIndexView(tables.DataTableView):
    table_class = PostsTable
    template_name = 'wp/index.html'

    def get_data(self):
        return utils.get_posts(self)

class PostCreateView(workflows.WorkflowView):
    workflow_class = CreatePost

    def get_initial(self):
        print "=== INSIDE PostCreateView get_initial ==="
        initial = super(PostCreateView, self).get_initial()
        return initial
