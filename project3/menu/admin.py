from django.contrib import admin

from .models import PizzaTopping, PizzaMenuItem, SandwichMenuItem, OneSizeMenuItem, PlatterMenuItem

admin.site.register(PizzaTopping)
admin.site.register(PizzaMenuItem)
admin.site.register(SandwichMenuItem)
admin.site.register(OneSizeMenuItem)
admin.site.register(PlatterMenuItem)
