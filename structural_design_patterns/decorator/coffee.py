"""Rolling my own decorator pattern implementation for fun and profit. Mostly fun."""


from abc import abstractmethod, ABC
from typing import List


class Beverage(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def cost(self) -> float:
        pass

    @property
    @abstractmethod
    def ingredients(self) -> str:
        pass


class Base(Beverage):
    def __init__(self, cost, base_ingredient):
        super().__init__()
        self._cost = cost
        self._ingredients = [base_ingredient]

    @property
    def cost(self) -> float:
        return self._cost

    @property
    def ingredients(self) -> List[str]:
        return self._ingredients

    def pretty_print_ingredients(self) -> str:
        return ", ".join(self._ingredients)


class Decorator(Beverage):
    @abstractmethod
    def __init__(self, beverage: Beverage):
        pass

    @property
    @abstractmethod
    def cost(self) -> float:
        pass

    @property
    @abstractmethod
    def ingredients(self) -> List[str]:
        pass


class MilkDecorator(Decorator):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    @property
    def cost(self) -> float:
        return self._beverage.cost + 0.5

    @property
    def ingredients(self) -> List[str]:
        return self._beverage.ingredients + ["Milk"]


class SugarDecorator(Decorator):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    @property
    def cost(self) -> float:
        return self._beverage.cost + 0.25

    @property
    def ingredients(self) -> List[str]:
        return self._beverage.ingredients + ["Sugar"]


class WhipDecorator(Decorator):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    @property
    def cost(self) -> float:
        return self._beverage.cost + 0.75

    @property
    def ingredients(self) -> List[str]:
        return self._beverage.ingredients + ["Whip"]
