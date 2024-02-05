"""Game statistics"""

from dataclasses import dataclass


@dataclass
class GameStats:
    CustomersEntered: int = 0
    CustomersServed: int = 0
    MoneyEarned: float = 0.0
    MoneySpent: float = 0.0
    WorkerChanges: int = 0

    def ServeCustomer(self) -> None:
        self.CustomersServed += 1

    def WorkerChanged(self) -> None:
        self.WorkerChanges += 1

    def UpdateMoney(self, amount) -> None:
        if amount > 0:
            self.MoneyEarned += amount
        else:
            self.MoneySpent += amount

    def GetEarnings(self) -> float:
        return max(self.MoneyEarned + PrevDay.MoneyEarned, 0.0)

    def GetSpend(self) -> float:
        return min(self.MoneySpent - PrevDay.MoneySpent, 0.0)

    def GetProfit(self) -> float:
        return self.GetEarnings() - abs(self.GetSpend())

    def GetServedCustomers(self) -> float:
        return self.CustomersServed - PrevDay.CustomersServed

    def GetTotalCustomers(self) -> float:
        return self.CustomersEntered - PrevDay.CustomersEntered


PrevDay = GameStats()
