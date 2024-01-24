"""Class for DefinedLocations"""
import random
import pygame
from Classes import Game
from Utilities import Utils
from Assets import AssetLibrary


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
RecurDepth = 0


def IsSeatTaken(seatLocation) -> bool:
    for sprite in Game.MasterGame.CharSpriteGroup:
        if sprite.ImageType == AssetLibrary.ImageTypes.Customer:
            xCheck = Utils.InTolerance(
                num1=sprite.rect.centerx, num2=seatLocation[0], tolerance=15
            )
            yCheck = Utils.InTolerance(
                num1=sprite.rect.centery, num2=seatLocation[1], tolerance=15
            )
            if xCheck or yCheck:
                return True
    return False


def GetRandomSeatPosition() -> tuple | None:
    global RecurDepth
    yPos = random.choice(SeatingPlan.TableCols)
    xPos = random.choice(SeatingPlan.TableRows)
    coords = (xPos, yPos)
    if IsSeatTaken(seatLocation=(xPos, yPos)):
        RecurDepth += 1
        if RecurDepth < 10:
            coords = GetRandomSeatPosition()
        else:
            return None
    else:
        RecurDepth = 0
    return coords


class DefinedPaths:
    @staticmethod
    def KitchenToLockerRoom(sprite, dest) -> list:
        path = [
            sprite.rect.center,
            LocationDefs.KitchenLocation,
            (dest[0], LocationDefs.KitchenLocation[1]),
            dest,
        ]
        return path

    @staticmethod
    def CustomerToRandomSeat(sprite) -> list:
        randomSeatPosition = GetRandomSeatPosition()
        if randomSeatPosition is not None:
            path = [
                (sprite.rect.centerx, randomSeatPosition[1]),
                (randomSeatPosition[0], randomSeatPosition[1]),
                randomSeatPosition,
            ]
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
    def BackToKitchen(sprite, activeGame=Game.MasterGame) -> list:
        path = [
            sprite.rect.center,
            (sprite.rect.center[0], LocationDefs.KitchenLocation[1]),
            LocationDefs.KitchenLocation,
            Utils.PositionRandomVariance(
                position=(
                    LocationDefs.KitchenLocation[0] - 50,
                    LocationDefs.KitchenLocation[1],
                ),
                percentVarianceTuple=(0.05, 0.1),
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


def DebugLocations(activateGame=Game.MasterGame) -> None:
    attrs = [x for x in dir(LocationDefs) if "__" not in x]
    for attr in attrs:
        pygame.draw.circle(
            surface=activateGame.Screen,
            color=(0, 200, 255),
            center=getattr(LocationDefs, attr),
            radius=25,
        )
