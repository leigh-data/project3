import pytest

pytestmark = pytest.mark.django_db

from project3.menu.models import PizzaMenuItem, OneSizeMenuItem


def test____str__():
    pizza = PizzaMenuItem.objects.create(
        menu_description="Cheese",
        pizza_type=PizzaMenuItem.PizzaType.SICILIAN,
        toppings=0,
        large_price=24.45,
        small_price=38.70
    )

    assert str(pizza) == "Cheese - Sicilian"

def test_get_sicilian_pizzas():
    PizzaMenuItem.objects.create(
        menu_description="Cheese",
        pizza_type=PizzaMenuItem.PizzaType.SICILIAN,
        toppings=0,
        large_price=24.45,
        small_price=38.70
    )

    PizzaMenuItem.objects.create(
        menu_description="1 topping",
        pizza_type=PizzaMenuItem.PizzaType.SICILIAN,
        toppings=1,
        large_price=26.45,
        small_price=40.70
    )

    PizzaMenuItem.objects.create(
        menu_description="THE SPECIAL",
        pizza_type=PizzaMenuItem.PizzaType.SICILIAN,
        toppings=100,
        large_price=30.45,
        small_price=45.70
    )

    pizzas = PizzaMenuItem.objects.get_sicilian_pizzas()

    assert len(pizzas) == 3
    
    current = -1
    for pizza in pizzas:
        assert pizza.toppings > current
        current = pizza.toppings


def test_get_regular_pizzas():
    PizzaMenuItem.objects.create(
        menu_description="Cheese",
        pizza_type=PizzaMenuItem.PizzaType.REGULAR,
        toppings=0,
        large_price=24.45,
        small_price=38.70
    )

    PizzaMenuItem.objects.create(
        menu_description="1 topping",
        pizza_type=PizzaMenuItem.PizzaType.REGULAR,
        toppings=1,
        large_price=26.45,
        small_price=40.70
    )

    PizzaMenuItem.objects.create(
        menu_description="THE SPECIAL",
        pizza_type=PizzaMenuItem.PizzaType.REGULAR,
        toppings=100,
        large_price=30.45,
        small_price=45.70
    )

    pizzas = PizzaMenuItem.objects.get_regular_pizzas()

    assert len(pizzas) == 3
    
    current = -1
    for pizza in pizzas:
        assert pizza.toppings > current
        current = pizza.toppings


def test_one_size_get_pasta():
    OneSizeMenuItem.objects.create(
        menu_description="Baked Ziti",
        entree_type=OneSizeMenuItem.OneSizeType.PASTA,
        large_price=24.45,
    )

    OneSizeMenuItem.objects.create(
        menu_description="Baked Ziti with Meatballs",
        entree_type=OneSizeMenuItem.OneSizeType.PASTA,
        large_price=8.75,
    )
    
    pasta = OneSizeMenuItem.objects.get_pasta()
    assert len(pasta) == 2


def test_one_size_get_salads():
    OneSizeMenuItem.objects.create(
        menu_description="Garden Salad",
        entree_type=OneSizeMenuItem.OneSizeType.SALAD,
        large_price=24.45,
    )

    OneSizeMenuItem.objects.create(
        menu_description="Greek Salad",
        entree_type=OneSizeMenuItem.OneSizeType.SALAD,
        large_price=8.75,
    )
    
    pasta = OneSizeMenuItem.objects.get_salads()
    assert len(pasta) == 2
