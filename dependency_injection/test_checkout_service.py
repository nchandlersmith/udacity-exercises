from checkout_service import CreditCardPayment, PayPalPayment, BitcoinPayment


class TestCheckoutService():
    def test_credit_card_payment(self):
        card = CreditCardPayment()
        result = card.pay(491.55)
        assert result == "Processing credit card payment of $491.55."

    def test_paypal_payment(self):
        card = PayPalPayment()
        result = card.pay(67.42)
        assert result == "Processing PayPal payment of $67.42."

    def test_bitcoin_payment(self):
        card = BitcoinPayment()
        result = card.pay(1197.01)
        assert result == "Processing Bitcoin payment of $1197.01."
