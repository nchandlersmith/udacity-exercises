from checkout_service import CreditCardPayment


class TestCheckoutService():
    def test_credit_card_payment(self):
        card = CreditCardPayment()
        result = card.pay(491.55)
        assert result == "Processing credit card payment of $491.55"
