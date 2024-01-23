"""Class for DefinedLocations"""
import random
import pygame
from Classes.Game import MasterGame
from Utilities import Utils


class DefinedLocations:
    @property
    def YellowLockerRoom(self) -> tuple:
        return (350, 75)

    @property
    def GreenLockerRoom(self) -> tuple:
        return (530, 75)

    @property
    def BlueLockerRoom(self) -> tuple:
        return (710, 75)

    @property
    def PinkLockerRoom(self) -> tuple:
        return (890, 75)

    @property
    def GreyLockerRoom(self) -> tuple:
        return (1070, 75)

    @property
    def KitchenLocation(self) -> tuple:
        return (200, 225)

    @property
    def CustomerExit(self) -> tuple:
        return (1200, 1000)

    @property
    def CustomerEntrance(self) -> tuple:
        return (1150, 325)

    @property
    def CustomerSpawn(self) -> tuple:
        return (1150, 1000)


LocationDefs = DefinedLocations()


def GetRandomSeatPosition() -> tuple:
    yPos = random.choice(SeatingPlan.TableCols)
    xPos = random.choice(SeatingPlan.TableRows)
    return (xPos, yPos)


class DefinedPaths:
    @staticmethod
    def CustomerToRandomSeat(sprite) -> list:
        randomSeatPosition = GetRandomSeatPosition()
        path = [
            (sprite.rect.centerx, randomSeatPosition[1]),
            (randomSeatPosition[0], randomSeatPosition[1]),
            randomSeatPosition,
        ]
        print(path)
        return path

    @staticmethod
    def KitchenToCustomer(sprite, dest) -> list:
        path = [
            sprite.rect.center,
            LocationDefs.KitchenLocation,
            (LocationDefs.KitchenLocation[0] + 100, LocationDefs.KitchenLocation[1]),
            (dest.rect.center[0] - 100, LocationDefs.KitchenLocation[1]),
            dest.rect.center,
        ]
        return path

    @staticmethod
    def BackToKitchen(sprite, activeGame=MasterGame) -> list:
        path = [
            sprite.rect.center,
            (LocationDefs.KitchenLocation[0], LocationDefs.KitchenLocation[1]),
            LocationDefs.KitchenLocation,
            Utils.PositionRandomVariance(
                position=LocationDefs.KitchenLocation,
                percentVarianceTuple=(0.1, 0.5),
                screenSize=activeGame.ScreenSize,
            ),
        ]
        return path

    @staticmethod
    def CustomerToExit(sprite) -> list:
        path = [sprite.rect.center, LocationDefs.CustomerExit]
        return path

    @staticmethod
    def TableToExit(sprite) -> list:
        path = [
            sprite.rect.center,
            (sprite.rect.centerx, sprite.rect.centery - 50),
            (LocationDefs.CustomerEntrance[0], sprite.rect.centery - 50),
            LocationDefs.CustomerExit,
        ]
        return path

    @staticmethod
    def CustomerToEntrance(sprite) -> list:
        path = [sprite.rect.center, LocationDefs.CustomerEntrance]
        return path


class SeatingPlan:
    TableRows = [350, 500, 650, 800, 950]
    TableCols = [400, 500, 600, 700]


def DebugLocations(activateGame=MasterGame) -> None:
    attrs = [x for x in dir(LocationDefs) if "__" not in x]
    for attr in attrs:
        pygame.draw.circle(
            surface=activateGame.Screen,
            color=(0, 200, 255),
            center=getattr(LocationDefs, attr),
            radius=25,
        )
