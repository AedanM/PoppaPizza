"""Game statistics"""

from dataclasses import dataclass


@dataclass
class GameStats:
    CustomersEntered: int = 0
    CustomersServed: int = 0
    MoneyEarned: float = 0.0
    MoneySpent: float = 0.0

    def GetEarnings(self) -> float:
        return max(self.MoneyEarned + PrevDay.MoneyEarned, 0.0)

    def GetSpend(self) -> float:
        return min(self.MoneySpent - PrevDay.MoneySpent, 0.0)

    def GetServedCustomers(self) -> float:
        return self.CustomersServed - PrevDay.CustomersServed

    def GetTotalCustomers(self) -> float:
        return self.CustomersEntered - PrevDay.CustomersEntered


PrevDay = GameStats()
