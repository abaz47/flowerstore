from django.contrib.admin import ModelAdmin, register, site
from django.contrib.auth.models import Group, User

from .models import Flower


site.unregister((Group, User))


@register(Flower)
class FlowerAdmin(ModelAdmin):
    list_display = ('pk', 'name', 'buy_price', 'sell_price', 'is_visible')
