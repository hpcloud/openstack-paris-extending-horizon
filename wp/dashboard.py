from django.utils.translation import ugettext_lazy as _

import horizon

class WordpressPanels(horizon.PanelGroup):
    name = _("Wordpress")
    slug = "wordpress"
    panels = ('wp', )

# class Wordpress(horizon.Dashboard):
#     name = _("Wordpress")
#     slug = "wordpress"
#     panels = (WordpressPanels)
#     default_panel = '???'
