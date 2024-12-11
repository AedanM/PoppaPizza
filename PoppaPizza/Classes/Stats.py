"""Game statistics"""

import copy
from dataclasses import dataclass

AllStats = {}


@dataclass
class GameStats:
    """Object for Monitoring Game Statistics"""

    CustomersEntered: int = 0
    CustomersServed: int = 0
    MoneyEarned: float = 0.0
    MoneySpent: float = 0.0
    WorkerChanges: int = 0

    def ServeCustomer(self) -> None:
        """Update Customers Served Metric"""
        self.CustomersServed += 1

    def WorkerChanged(self) -> None:
        """Update Worker Changes Metric"""
        self.WorkerChanges += 1

    def UpdateMoney(self, amount) -> None:
        """Update Current Cash, sorting by spend or earning

        Args-
            amount (int | float): Amount Spent or Earned
        """
        if amount > 0:
            self.MoneyEarned += amount
        else:
            self.MoneySpent += amount

    def GetDailyCostumeChanges(self) -> int:
        """Return Costume Chages Metric since yesterday

        Returns-
            int: Costume Chages Metric since yesterday
        """
        return self.WorkerChanges - PrevDay.WorkerChanges

    def GetDailyEarnings(self) -> float:
        """Return Earnings Metric since yesterday

        Returns-
            float: Earnings Metric since yesterday
        """
        return max(self.MoneyEarned + PrevDay.MoneyEarned, 0.0)

    def GetDailySpend(self) -> float:
        """Return Spending Metric since yesterday

        Returns-
            float: Spending Metric since yesterday
        """
        return min(self.MoneySpent - PrevDay.MoneySpent, 0.0)

    def GetDailyProfit(self) -> float:
        """Return Profit Metric since yesterday

        Returns-
            float: Profit Metric since yesterday
        """
        return self.GetDailyEarnings() - abs(self.GetDailySpend())

    def GetDailyServedCustomers(self) -> float:
        """Return Number of customers served since yesterday

        Returns-
            float: Number of customers served since yesterday
        """
        return self.CustomersServed - PrevDay.CustomersServed

    def GetDailyTotalCustomers(self) -> float:
        """Return Number of customers that entered the shop since yesterday

        Returns-
            float: Number of customers that entered the shop since yesterday
        """
        return self.CustomersEntered - PrevDay.CustomersEntered


PrevDay = GameStats()


def UpdateStats(activeGame) -> None:
    global AllStats, PrevDay
    AllStats[f"Day {activeGame.GameClock.Day}"] = copy.deepcopy(activeGame.UserInventory.Statistics)
    PrevDay = copy.deepcopy(activeGame.UserInventory.Statistics)
