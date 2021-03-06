from django.db import models


class PizzaTopping(models.Model):
    name = models.CharField("Name of Topping", max_length=126)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu_description = models.CharField("Menu Description", max_length=126)
    cart_description = models.CharField("Cart Description", max_length=126)
    large_price = models.DecimalField("Large Price", max_digits=5, decimal_places=2)
    small_price = models.DecimalField(
        "Small Price", max_digits=5, decimal_places=2, blank=True, null=True
    )

    def __str__(self):
        return self.cart_description


class PizzaMenuItem(MenuItem):
    class PizzaType(models.TextChoices):
        REGULAR = ("Regular", "Regular")
        SICILIAN = ("Sicilian", "Sicilian")

    toppings = models.PositiveSmallIntegerField("Number of Toppings")
    pizza_type = models.CharField(
        "Pizza Type",
        max_length=50,
        choices=PizzaType.choices,
        default=PizzaType.REGULAR,
    )

    class Meta:
        unique_together = ["pizza_type", "toppings"]
        verbose_name = "Pizza"
        verbose_name_plural = "Pizzas"


class SandwichMenuItem(MenuItem):
    extra_cheese = models.BooleanField("Extra Cheese", default=True)
    wit = models.BooleanField("Wit")
    mushrooms = models.BooleanField("Mushrooms")
    peppers = models.BooleanField("Peppers")

    class Meta:
        verbose_name_plural = "Steaks and Hoagies"


class PlatterMenuItem(MenuItem):
    class Meta:
        verbose_name = "Platter"
        verbose_name_plural = "Platters"


class OneSizeMenuItem(MenuItem):
    class OneSizeType(models.TextChoices):
        PASTA = ("pasta", "Pasta")
        SALAD = ("salad", "Salad")

    entree_type = models.CharField(
        "Entree Type",
        max_length=50,
        choices=OneSizeType.choices,
        default=OneSizeType.SALAD,
    )

    class Meta:
        verbose_name = "One Size"
        verbose_name_plural = "One Size Entrees"
