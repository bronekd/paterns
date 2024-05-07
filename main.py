# task 1 z Module 12. Design Patterns. Parts2

#uchovat data a vnitřní strategie zda uložit nebo vypsat. to budou 2 strategie

#Create a class that performs the following operations on a array: display data in a file or on the screen, flip data, find min max.
# the class can get a set of values from a keyboard or a file. Use the strategy pattern and other necessary pattern.

from typing import List


class OperatorFile:
    def sum(self, my_num: List[int]) -> float:
        pass


class MinStrategy(OperatorFile):
    def sum(self, my_num: List[int]) -> float:
        return min(my_num)


class MaxStrategy(OperatorFile):
    def sum(self, my_num: List[int]) -> float:
        return max(my_num)

# File Operator (Context)
class CashDesk:
    def __init__(self):
        self.my_num = []
        self.strategy = MinStrategy()

    def add(self, price):
        self.my_num.append(price)

    def print_bill(self):
        total_price = self.strategy.sum(self.my_num)
        print(f"Celkem k zaplaceni: {total_price}")
        print("Dekujeme za navstevu, vratte se znovu!")
        self.my_num = []

    def set_strategy(self, strategy):
        self.strategy = strategy


if __name__ == "__main__":
    cash_desk = CashDesk()

    # Happy Hour
    cash_desk.set_strategy(MinStrategy())
    cash_desk.add(20)
    cash_desk.add(80)
    cash_desk.print_bill()

    # Koniec Happy Hour

    # Normálna stratégia
    cash_desk.set_strategy(MaxStrategy())
    cash_desk.add(20)
    cash_desk.add(80)
    cash_desk.print_bill()



