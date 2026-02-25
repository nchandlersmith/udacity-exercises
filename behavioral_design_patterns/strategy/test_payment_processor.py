from payment_processor import CreditCard, PayPal, Bitcoin, PaymentProcessor


class TestPaymentProcessor:
    def test_credit_card_returns_amount_and_method(self):
        card = CreditCard()
        result = card.pay(12.34)
        assert result == "Paid 12.34 using Credit Card"

    def test_paypal_returns_amount_and_method(self):
        paypal = PayPal()
        result = paypal.pay(12.34)
        assert result == "Paid 12.34 using PayPal"

    def test_bitcoin_returns_amount_and_method(self):
        bitcoin = Bitcoin()
        result = bitcoin.pay(12.34)
        assert result == "Paid 12.34 using Bitcoin"

    def test_payment_processor_uses_strategy_to_pay(self):
        processor = PaymentProcessor()
        result = processor.pay(12.34, CreditCard())
        assert result == "Paid 12.34 using Credit Card"
