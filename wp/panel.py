from django.utils.translation import ugettext_lazy as _

import horizon

class PostsPanel(horizon.Panel):
    name = _("Posts")
    slug = 'wp'
