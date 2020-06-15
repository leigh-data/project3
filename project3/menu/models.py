from django.db import models

class PizzaTopping(models.Model):
    name = models.CharField("Name of Topping", max_length=126)


class MenuItem(models.Model):
    menu_description = models.CharField("Menu Description", max_length=126)
    large_price = models.DecimalField("Large Price", max_digits=5, decimal_places=2)
    small_price = models.DecimalField("Small Price", max_digits=5, decimal_places=2, blank=True, null=True)


class PizzaMenuItem(MenuItem):
    class PizzaType(models.TextChoices):
        REGULAR = ("Regular", "Regular")
        SICILIAN = ("Sicilian", "Sicilian")

    toppings = models.PositiveSmallIntegerField("Number of Toppings")
    pizza_type = models.CharField("Pizza Type", max_length=50, choices=PizzaType.choices, default=PizzaType.REGULAR)

    class Meta:
        unique_together = ['pizza_type', 'toppings']
    
    def __str__(self):
        return f"{self.menu_description} - {self.pizza_type}"

class SandwichMenuItem(MenuItem):
    extra_cheese = models.BooleanField("Extra Cheese")
    wit = models.BooleanField("Wit")
    mushrooms = models.BooleanField("Mushrooms")
    peppers = models.BooleanField("Peppers")


class PlatterMenuItem(MenuItem):
    pass

class OneSizeMenuItem(MenuItem):
    class OneSizeType(models.TextChoices):
        PASTA = ("pasta", "Pasta")
        SALAD = ("salad", "Salad")
