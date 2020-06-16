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
    ordering = ("pizza_type", "toppings")
    fields = (
        "pizza_type",
        "toppings",
        "menu_description",
        "cart_description",
        "small_price",
        "large_price",
    )


@admin.register(SandwichMenuItem)
class SandwichMenuItemAdmin(admin.ModelAdmin):
    ordering = ("id",)
    fields = (
        "menu_description",
        "cart_description",
        "small_price",
        "large_price",
        "extra_cheese",
        "wit",
        "mushrooms",
        "peppers",
    )


admin.site.register(PizzaTopping)
admin.site.register(OneSizeMenuItem)
admin.site.register(PlatterMenuItem)
