"""Defined Motion Paths"""

import random

from Classes import Game
from Definitions import AssetLibrary, DefinedLocations
from Utilities import Utils

RECURDEPTH = 0


def IsSeatTaken(seatLocation) -> bool:
    for sprite in Game.MasterGame.CharSpriteGroup:
        if sprite.ImageType in AssetLibrary.CustomerOutfits:
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
    # pylint: disable=global-statement
    global RECURDEPTH
    seatingPlan = DefinedLocations.SeatingPlan
    yPos = random.choice(seatingPlan.TableCols())
    xPos = random.choice(seatingPlan.TableRows())
    coords = (xPos, yPos)
    if IsSeatTaken(seatLocation=(xPos, yPos)):
        RECURDEPTH += 1
        if RECURDEPTH < 10:
            coords = GetRandomSeatPosition()
        else:
            return None
    else:
        RECURDEPTH = 0
    return coords


class DefinedPaths:
    @staticmethod
    def KitchenToLockerRoom(sprite, dest) -> list:
        path = [
            sprite.rect.center,
            DefinedLocations.LocationDefs.KitchenLocation,
            (dest[0], DefinedLocations.LocationDefs.KitchenLocation[1]),
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
                (randomSeatPosition[0], randomSeatPosition[1] + 50),
            ]
            return path

    @staticmethod
    def KitchenToCustomer(sprite, dest) -> list:
        path = [
            sprite.rect.center,
            DefinedLocations.LocationDefs.KitchenLocation,
            (
                DefinedLocations.LocationDefs.KitchenLocation[0] + 100,
                DefinedLocations.LocationDefs.KitchenLocation[1],
            ),
            (
                dest.rect.center[0] - 100,
                DefinedLocations.LocationDefs.KitchenLocation[1],
            ),
            dest.rect.center,
        ]
        return path

    @staticmethod
    def BackToKitchen(sprite, activeGame=Game.MasterGame) -> list:
        path = [
            sprite.rect.center,
            (sprite.rect.center[0], DefinedLocations.LocationDefs.KitchenLocation[1]),
            DefinedLocations.LocationDefs.KitchenLocation,
            Utils.PositionRandomVariance(
                position=(
                    DefinedLocations.LocationDefs.KitchenLocation[0] - 50,
                    DefinedLocations.LocationDefs.KitchenLocation[1],
                ),
                percentVarianceTuple=(0.05, 0.1),
                screenSize=activeGame.ScreenSize,
            ),
        ]
        return path

    @staticmethod
    def CustomerToExit(sprite) -> list:
        path = [sprite.rect.center, DefinedLocations.LocationDefs.CustomerExit]
        return path

    @staticmethod
    def TableToExit(sprite) -> list:
        path = [
            sprite.rect.center,
            (sprite.rect.centerx, sprite.rect.centery - 100),
            (
                DefinedLocations.LocationDefs.CustomerEntrance[0],
                sprite.rect.centery - 100,
            ),
            DefinedLocations.LocationDefs.CustomerExit,
        ]
        return path

    @staticmethod
    def CustomerToEntrance(sprite) -> list:
        path = [sprite.rect.center, DefinedLocations.LocationDefs.CustomerEntrance]
        return path
