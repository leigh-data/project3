from django.db import models

class PizzaManager(models.Manager):
    def get_regular_pizzas(self):
        return self.filter(pizza_type=PizzaMenuItem.PizzaType.REGULAR).order_by('toppings')
    
    def get_sicilian_pizzas(self):
        return self.filter(pizza_type=PizzaMenuItem.PizzaType.SICILIAN).order_by('toppings')


class OnseSizeMenuItemManager(models.Manager):
    def get_salads(self):
        return self.filter(entree_type=OneSizeMenuItem.OneSizeType.SALAD)
    
    def get_pasta(self):
        return self.filter(entree_type=OneSizeMenuItem.OneSizeType.PASTA)


class PizzaTopping(models.Model):
    name = models.CharField("Name of Topping", max_length=126)


class MenuItem(models.Model):
    menu_description = models.CharField("Menu Description", max_length=126)
    large_price = models.DecimalField("Large Price", max_digits=5, decimal_places=2)
    small_price = models.DecimalField("Small Price", max_digits=5, decimal_places=2, blank=True, null=True)


class PizzaMenuItem(MenuItem):
    objects = PizzaManager()

    class PizzaType(models.TextChoices):
        REGULAR = ("Regular", "Regular")
        SICILIAN = ("Sicilian", "Sicilian")

    toppings = models.PositiveSmallIntegerField("Number of Toppings")
    pizza_type = models.CharField("Pizza Type", max_length=50, choices=PizzaType.choices, default=PizzaType.REGULAR)

    class Meta:
        unique_together = ['pizza_type', 'toppings']
        verbose_name = "Pizza"
        verbose_name_plural = "Pizzas"
    
    def __str__(self):
        return f"{self.menu_description} - {self.pizza_type}"

class SandwichMenuItem(MenuItem):
    extra_cheese = models.BooleanField("Extra Cheese")
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
    
    objects = OnseSizeMenuItemManager()

    entree_type = models.CharField("Entree Type", max_length=50, choices=OneSizeType.choices, default=OneSizeType.SALAD)
    
    class Meta:
        verbose_name = "One Size"
        verbose_name_plural = "One Size Entrees"
