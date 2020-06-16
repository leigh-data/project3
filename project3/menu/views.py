from django.views.generic import View
from django.shortcuts import render

from .models import PizzaMenuItem, SandwichMenuItem


class MenuDisplayView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "sicilian_pizzas": PizzaMenuItem.objects.get_sicilian_pizzas(),
            "regular_pizzas": PizzaMenuItem.objects.get_regular_pizzas(),
            "sandwiches": SandwichMenuItem.objects.all(),
        }
        return render(request, "menu/index.html", context)
