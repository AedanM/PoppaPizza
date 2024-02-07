"""Inventory Object"""

import pygame

from Classes import Stats
from Definitions import CustomEvents


class Inventory:
    """Holding Class for all User assets"""

    Money: float = 2000.0
    AdvertisingBonus: float = 0.0
    Statistics: Stats.GameStats = Stats.GameStats()

    def GetPaid(self, amount) -> None:
        """Get paid an amount of cash

        Args:
            amount (int | float): Amount Paid
        """
        amount = round(max(amount, 0), 2)
        self.Money += amount
        self.Statistics.UpdateMoney(amount=amount)
        pygame.event.post(CustomEvents.UpdateBackground)

    def PayMoney(self, amount, update=True) -> None:
        """Pay an Amount of Money and Update the Stats

        Args:
            amount (int | float): Amount spent
            update (bool, optional): To Update the Game Over ticker or not. Defaults to True.
        """
        amount = round(min(-(abs(amount)), 0), 2)
        self.Money += amount
        self.Statistics.UpdateMoney(amount=amount)
        pygame.event.post(CustomEvents.UpdateBackground)
        if self.Money < 0 and update:
            pygame.event.post(CustomEvents.GameOver)
