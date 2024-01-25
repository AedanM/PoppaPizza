from dataclasses import dataclass
from Definitions import Prices


@dataclass
class Inventory:
    Money: float = 2000.0

    def GetPaid(self, amount) -> None:
        self.Money += amount

    def PayRent(self, amount=Prices.CurrentRent) -> None:
        self.Money -= amount
