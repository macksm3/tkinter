# test project code
# create coin class
class Coin:
    def __init__(self, name, value):
        self.name = name
        self.value = float(value)
        self.qty = 0
        self.stackval = 0.00

    def get_subtotal(self, qty_str):
        """ get quantity of each coin and calculate total value """
        self.qty = int(qty_str or 0)    # default input value set to 0
        self.stackval = self.value * self.qty
        return f"Total of {self.name}: {self.value} x {self.qty} = ${'{:,.2f}'.format(self.stackval)}"


