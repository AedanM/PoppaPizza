"""Defined Motion Paths"""

import copy
import random

from Classes import Game
from Definitions import AssetLibrary, DefinedLocations
from Utilities import Utils


def IsSeatTaken(seatLocation) -> bool:
    """Checks if Customer Sat in Seat

    Args:
        seatLocation (tuple): Location of Seat

    Returns:
        bool: Is Seat Free
    """
    for sprite in Game.MasterGame.CharSpriteGroup:
        if sprite.ImageType in AssetLibrary.CustomerOutfits:
            xCheck = Utils.InTolerance(
                num1=sprite.rect.centerx, num2=seatLocation[0], tolerance=15
            )
            yCheck = Utils.InTolerance(
                num1=sprite.rect.centery, num2=seatLocation[1], tolerance=15
            )
            dstCheck = (
                sprite.MvmHandler.PointsList[-1] == seatLocation
                if sprite.MvmHandler.PointsList != []
                else False
            )
            print(sprite.rect.center)
            if xCheck and yCheck and dstCheck:
                return True
    return False


def GetRandomSeatPosition() -> tuple | None:
    """Picks a random seat position or returns None if None free

    Returns:
        tuple | None: Seat position
    """
    seatingPlan = DefinedLocations.SeatingPlan
    seats = copy.deepcopy(seatingPlan.GenerateTablePlaces())
    random.shuffle(seats)
    for seat in seats:
        if not IsSeatTaken(seatLocation=(seat[0], seat[1])):
            return seat
    return None


class DefinedPaths:
    """Lists of Defined Locations to Generate Motion Paths"""

    @staticmethod
    def KitchenToLockerRoom(sprite, dest) -> list:
        """Kitchen to a desired changing room

        Args:
            sprite (Sprite): Worker To Change
            dest (tuple): Destination Position

        Returns:
            list: List of Points for Path
        """
        path = [
            sprite.rect.center,
            DefinedLocations.LocationDefs.KitchenLocation,
            (dest[0], DefinedLocations.LocationDefs.KitchenLocation[1]),
            dest,
        ]
        return path

    @staticmethod
    def CustomerToRandomSeat(sprite) -> list:
        """Picks a random seat and generates a path to it

        sprite (Sprite): Active Customer

        Returns:
            list: List of Points for Path
        """
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
        """Path for kitchen to customer's seat

        Args:
            sprite (Sprite): Active Worker
            dest (tuple): Customer's Seat

        Returns:
            list: List of Points for Path
        """
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
        """From Current Location to Kitchen

        Args:
            sprite (Sprite): Active Worker
            activeGame (Game, optional): Current Game. Defaults to Game.MasterGame

        Returns:
            list: List of Points for Path
        """
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
        """Queued Customer to Leave the Restaurant

        Args:
            sprite (Sprite): Active Customer

        Returns:
            list: List of Points for Path
        """
        path = [sprite.rect.center, DefinedLocations.LocationDefs.CustomerExit]
        return path

    @staticmethod
    def TableToExit(sprite) -> list:
        """Seated Customer to Exit

        Args:
            sprite (Sprite): Active Customer

        Returns:
            list: List of Points for Path
        """
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
        """Walk In Logic Path

        Args:
            sprite (Sprite): Active Customer

        Returns:
            list: List of Points for Path
        """
        path = [sprite.rect.center, DefinedLocations.LocationDefs.CustomerEntrance]
        return path
