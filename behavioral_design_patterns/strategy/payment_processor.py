from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card"


class PayPal(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} using PayPal"


class Bitcoin(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} using Bitcoin"
    
    
class PaymentProcessor:
    def pay(self, amount, strategy):
        return strategy.pay(amount)
