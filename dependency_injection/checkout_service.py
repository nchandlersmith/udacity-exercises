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
