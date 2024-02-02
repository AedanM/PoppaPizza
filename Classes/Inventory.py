"""Inventory Object"""

from dataclasses import dataclass

import pygame

from Definitions import CustomEvents


@dataclass
class Inventory:
    Money: float = 2000.0
    AdvertisingBonus: float = 0.0

    def GetPaid(self, amount) -> None:
        self.Money += amount
        pygame.event.post(CustomEvents.UpdateBackground)

    def PayMoney(self, amount) -> None:
        self.Money -= amount
        pygame.event.post(CustomEvents.UpdateBackground)
        if self.Money < 0:
            pygame.event.post(CustomEvents.GameOver)
