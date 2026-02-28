from checkout_service import CreditCardPayment, PayPalPayment, BitcoinPayment, StandardShipping, ExpressShipping, EmailNotification, SMSNotification


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

    def test_standard_shipping(self):
        shipping = StandardShipping()
        result = shipping.ship("AA18903-45K")
        assert result == "Order AA18903-45K shipped via standard shipping."

    def test_express_shipping(self):
        shipping = ExpressShipping()
        result = shipping.ship("AB88230-11J")
        assert result == "Order AB88230-11J shipped via express shipping."

    def test_email_notification(self):
        notification = EmailNotification()
        result = notification.notify("order shipped.")
        assert result == "Emailed the following message: order shipped."

    def test_sms_notification(self):
        notification = SMSNotification()
        result = notification.notify("order shipped.")
        assert result == "Sent the following SMS message: order shipped."
