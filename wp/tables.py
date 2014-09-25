from django import template
from django.template.defaultfilters import filesizeformat
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import tables  #, workflows, forms


class PostsTable(tables.DataTable):
    pass

    class Meta:
        name = "wp"
        verbose_name = _("Posts")
