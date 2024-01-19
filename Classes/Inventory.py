from dataclasses import dataclass


@dataclass
class Inventory():
    Money: float = 0.0
    
    def GetPaid(self, amount):
        self.Money += amount
        print(self.Money)