from django.shortcuts import render

from horizon import exceptions, tables #, forms, tabs, workflows

from wp.tables import PostsTable

class IndexView(tables.DataTableView):
    table_class = PostsTable
    template_name = 'wp/index.html'
