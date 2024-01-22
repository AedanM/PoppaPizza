"""Class for DefinedLocations"""

import pygame
from Classes import Game, ColorTools
from Utilities import Utils


class DefinedLocations:
    @property
    def KitchenLocation(self) -> tuple:
        return (100, 225)

    @property
    def KitchenDoorLocation(self) -> tuple:
        return (300, 225)

    @property
    def LockerRoomLocation(self) -> tuple:
        return (100, 700)

    @property
    def CustomerExit(self) -> tuple:
        return (1200, 1000)

    @property
    def CustomerEntrance(self) -> tuple:
        return (1150, 325)

    @property
    def CustomerSpawn(self) -> tuple:
        return (1300, 325)

    @property
    def TopRow(self) -> tuple:
        return (0, 0)


LocationDefs = DefinedLocations()


class DefinedPaths:
    @staticmethod
    def KitchenToCustomer(sprite, dest) -> list:
        path = [
            sprite.rect.center,
            LocationDefs.KitchenLocation,
            LocationDefs.KitchenDoorLocation,
            dest.rect.center,
        ]
        return path

    @staticmethod
    def BackToKitchen(sprite) -> list:
        path = [
            sprite.rect.center,
            LocationDefs.KitchenDoorLocation,
            LocationDefs.KitchenLocation,
            Utils.PositionRandomVariance(
                position=LocationDefs.KitchenLocation,
                percentVarianceTuple=(0.1, 0.5),
                screenSize=Game.MasterGame.ScreenSize,
            ),
        ]
        return path

    @staticmethod
    def CustomerToExit(sprite) -> list:
        path = [sprite.rect.center, LocationDefs.CustomerExit]
        return path

    @staticmethod
    def CustomerToEntrance(sprite) -> list:
        path = [sprite.rect.center, LocationDefs.CustomerEntrance]
        return path


class SeatingPlan:
    TableRows = [450, 650, 850, 1050]
    TableCols = [50, 250, 450, 650]


def DebugLocations() -> None:
    attrs = [x for x in dir(LocationDefs) if "__" not in x]
    for attr in attrs:
        pygame.draw.circle(
            surface=Game.MasterGame.Screen,
            color=ColorTools.blue.RGB,
            center=getattr(LocationDefs, attr),
            radius=25,
        )
