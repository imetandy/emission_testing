class ClimateFund:
    def __init__(self):
        self.fund = 0

    def deposit(self, amount: float):
        self.fund += amount

    def get_fund(self):
        return self.fund