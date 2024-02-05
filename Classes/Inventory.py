"""Inventory Object"""

import pygame

from Classes import Stats
from Definitions import CustomEvents


class Inventory:
    Money: float = 2000.0
    AdvertisingBonus: float = 0.0
    Statistics: Stats.GameStats = Stats.GameStats()

    def GetPaid(self, amount) -> None:
        self.Money += amount
        self.Statistics.MoneyEarned += amount
        pygame.event.post(CustomEvents.UpdateBackground)

    def PayMoney(self, amount) -> None:
        self.Money -= amount
        self.Statistics.MoneySpent -= amount
        pygame.event.post(CustomEvents.UpdateBackground)
        if self.Money < 0:
            pygame.event.post(CustomEvents.GameOver)
