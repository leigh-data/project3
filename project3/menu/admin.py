from django.contrib import admin

from .models import (
    PizzaTopping,
    PizzaMenuItem,
    SandwichMenuItem,
    OneSizeMenuItem,
    PlatterMenuItem,
)


@admin.register(PizzaMenuItem)
class PizzaMenuItemAdmin(admin.ModelAdmin):
    ordering = ("toppings", "pizza_type")
    fields = (
        "pizza_type",
        "toppings",
        "menu_description",
        "cart_description",
        "small_price",
        "large_price",
    )


admin.site.register(PizzaTopping)
admin.site.register(SandwichMenuItem)
admin.site.register(OneSizeMenuItem)
admin.site.register(PlatterMenuItem)
