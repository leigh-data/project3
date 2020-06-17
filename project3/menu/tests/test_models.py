import pytest

from ..models import PizzaMenuItem, PizzaTopping

pytestmark = pytest.mark.django_db


def create_pizza(
    menu_description,
    cart_description,
    small_price,
    large_price,
    toppings,
    sicilian=False,
):
    if sicilian:
        pizza_type = PizzaMenuItem.PizzaType.SICILIAN
    else:
        pizza_type = PizzaMenuItem.PizzaType.REGULAR

    return PizzaMenuItem.objects.create(
        menu_description=menu_description,
        cart_description=cart_description,
        small_price=small_price,
        large_price=large_price,
        pizza_type=pizza_type,
        toppings=toppings,
    )


def test_menu_item___str__():
    pizza = create_pizza("Cheese", "Regular - Cheese", 15.00, 20.00, 0)
    assert str(pizza) == "Regular - Cheese"


def test_pizza_topping___str__():
    topping = PizzaTopping.objects.create(name="Pepperoni")
    assert str(topping) == "Pepperoni"
