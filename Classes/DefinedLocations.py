"""Class for DefinedLocations"""

import pygame
from Classes import Game, ColorTools
from Utilities import Utils


class DefinedLocations:
    @property
    def KitchenLocation(self):
        return (100, 225)

    @property
    def KitchenDoorLocation(self):
        return (300, 225)

    @property
    def LockerRoomLocation(self):
        return (100, 700)

    @property
    def CustomerExit(self):
        return (1200, 1000)

    @property
    def CustomerEntrance(self):
        return (1150, 325)


LocationDefs = DefinedLocations()


class DefinedPaths:
    @staticmethod
    def KitchenToCustomer(sprite, dest):
        return [
            sprite.rect.center,
            LocationDefs.KitchenLocation,
            LocationDefs.KitchenDoorLocation,
            dest.rect.center,
        ]

    @staticmethod
    def BackToKitchen(sprite):
        return [
            sprite.rect.center,
            LocationDefs.KitchenDoorLocation,
            LocationDefs.KitchenLocation,
            Utils.PositionRandomVariance(
                LocationDefs.KitchenLocation, (0.1, 0.5), Game.MasterGame.ScreenSize
            ),
        ]

    @staticmethod
    def CustomerToExit(sprite):
        return [sprite.rect.center, LocationDefs.CustomerExit]


def DebugLocations():
    attrs = [x for x in dir(LocationDefs) if "__" not in x]
    for attr in attrs:
        pygame.draw.circle(
            Game.MasterGame.Screen, ColorTools.blue.RGB, getattr(LocationDefs, attr), 25
        )
