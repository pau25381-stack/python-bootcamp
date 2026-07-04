class CashPayment:
    def __init__(self, amount):
        self.amount = amount

    def total(self):
        return self.amount

    def __add__(self, other):
        return self.total() + other.total()


class CreditPayment:
    def __init__(self, amount, limit):
        """Set attributes here"""
        self.amount = amount
        self.limit = limit

    def total(self):
        """Raise error if amount is beyond limit"""
        if self.amount > self.limit:
            raise ValueError ("Beyond limit")
        return self.amount

    def __add__(self, other):
        return self.total() + other.total()

class OnlinePayment:
    def __init__(self, amount, fee):
        """Set attributes here"""
        self.amount = amount
        self.fee = fee

    def total(self):
        """Return amount + fee"""
        return self.amount + self.fee

    def __add__(self, other):
        return self.total() + other.total()


class DiscountedPayment:
    def __init__(self, amount, discount):
        """Set attributes here"""
        self.amount = amount
        self.discount = discount

    def total(self):
        """Return amount - discount"""
        return max(0, self.amount - self.discount)

    def __add__(self, other):
        return self.total() + other.total()

payments = [
    CashPayment(1000),
    CreditPayment(500, limit=1000),
    OnlinePayment(800, fee=50),
    DiscountedPayment(600, discount=100)
]

total = 0
for payment in payments:
    total += payment.total()

print("Total:", total)
