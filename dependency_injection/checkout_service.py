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


class BitcoinPayment:
    def pay(self, amount):
        return f"Processing Bitcoin payment of ${amount}."


class ShippingStrategy(ABC):
    @abstractmethod
    def ship(self, order_id):
        pass


class StandardShipping(ShippingStrategy):
    def ship(self, order_id):
        return f"Order {order_id} shipped via standard shipping."


class ExpressShipping(ShippingStrategy):
    def ship(self, order_id):
        return f"Order {order_id} shipped via express shipping."


class NotificationStrategy(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class EmailNotification(NotificationStrategy):
    def notify(self, message):
        return f"Emailed the following message: {message}"


class SMSNotification(NotificationStrategy):
    def notify(self, message):
        return f"Sent the following SMS message: {message}"


class CheckOutService():
    def __init__(self, payment_type, shipping_type, notification_type):
        self._payment_type = payment_type
        self._shipping_type = shipping_type
        self._notification_type = notification_type

    def checkout(self, order_id, amount):
        message = self._payment_type.pay(
            amount) + " " + self._shipping_type.ship(order_id)
        return self._notification_type.notify(message)


if "__main__" == __name__:
    service = CheckOutService(
        CreditCardPayment(), StandardShipping(), EmailNotification())
    print(service.checkout("KQ90227-77F", 88.29))
    service = CheckOutService(
        BitcoinPayment(), ExpressShipping(), SMSNotification())
    print(service.checkout("XZ00927-38E", 18933))
