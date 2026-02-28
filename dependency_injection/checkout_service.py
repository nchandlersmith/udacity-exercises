from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Processing credit card payment of ${amount}."


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Processing PayPal payment of ${amount}."


class ShippingStrategy(ABC):
    @abstractmethod
    def ship(self, order_id):
        pass


class NotificationStrategy(ABC):
    @abstractmethod
    def notify(self, message):
        pass
