from django import template
from wmenu.models import Menu

register = template.Library()

@register.simple_tag(takes_context=True)
def get_menu(context, menu_title):
    return Menu.objects.filter(title=menu_title).first()
