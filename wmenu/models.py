from django.db import models
from modelcluster.models import ClusterableModel

from modelcluster.fields import ParentalKey
from wagtail.models import Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet

@register_snippet
class Menu(ClusterableModel):
    title = models.CharField(max_length=255, help_text='Enter "Main" for the primary menu.')

    panels = [
        FieldPanel('title'),
        InlinePanel('menu_items', label="Menu Items"),
    ]

    def __str__(self):
        return self.title

class MenuItem(Orderable):
    link_title = models.CharField(max_length=255, blank=True)
    link_url = models.CharField(max_length=500, blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE
    )
    menu = ParentalKey('wmenu.Menu', related_name='menu_items')

    panels = [
        FieldPanel('link_title'),
        FieldPanel('link_url'),
        FieldPanel('link_page'),
    ]

    def __str__(self):
        return self.link_title
