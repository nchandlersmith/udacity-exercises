"""Tests for the coffee decorator pattern example."""

from coffee import Base, MilkDecorator, SugarDecorator, WhipDecorator


import pytest


class TestCoffee:
    def test_base_should_have_cost_and_ingredients(self):
        coffee = Base(1.0, "Coffee")
        assert coffee.cost == 1.0
        assert coffee.ingredients == ["Coffee"]
        assert coffee.pretty_print_ingredients() == "Coffee"

    def test_milk_decorator_should_add_cost_and_ingredients(self):
        coffee = Base(1.0, "Coffee")

        milk_coffee = MilkDecorator(coffee)

        assert milk_coffee.cost == 1.5
        assert milk_coffee.ingredients == ["Coffee", "Milk"]

    def test_sugar_decorator_should_add_cost_and_ingredients(self):
        coffee = Base(1.0, "Coffee")

        sugar_coffee = SugarDecorator(coffee)

        assert sugar_coffee.cost == 1.25
        assert sugar_coffee.ingredients == ["Coffee", "Sugar"]

    def test_whip_decorator_should_add_cost_and_ingredients(self):
        coffee = Base(1.0, "Coffee")

        whip_coffee = WhipDecorator(coffee)

        assert  whip_coffee.cost == 1.75
        assert  whip_coffee.ingredients == ["Coffee", "Whip"]

    def test_multiple_decorators_should_do_all_the_things(self):
        coffee = Base(1.0, "Coffee")
        
        fancycoffee = WhipDecorator(SugarDecorator(MilkDecorator(coffee)))

        assert fancycoffee.cost == 2.5
        assert fancycoffee.ingredients == ["Coffee", "Milk", "Sugar", "Whip"]
