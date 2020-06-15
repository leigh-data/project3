import pytest

pytestmark = pytest.mark.django_db

from project3.menu.models import PizzaMenuItem


def test____str__():
    pizza = PizzaMenuItem.objects.create(
        menu_description="Cheese",
        pizza_type=PizzaMenuItem.PizzaType.SICILIAN,
        toppings=0,
        large_price=24.45,
        small_price=38.70
    )

    assert str(pizza) == "Cheese - Sicilian"