"""Inventory Object"""

import pygame

from Classes import Stats
from Definitions import CustomEvents


class Inventory:
    Money: float = 2000.0
    AdvertisingBonus: float = 0.0
    Statistics: Stats.GameStats = Stats.GameStats()

    def GetPaid(self, amount) -> None:
        amount = max(amount, 0)
        self.Money += amount
        self.Statistics.UpdateMoney(amount=amount)
        pygame.event.post(CustomEvents.UpdateBackground)

    def PayMoney(self, amount) -> None:
        amount = min(-(abs(amount)), 0)
        self.Money += amount
        self.Statistics.UpdateMoney(amount=amount)
        pygame.event.post(CustomEvents.UpdateBackground)
        if self.Money < 0:
            pygame.event.post(CustomEvents.GameOver)
