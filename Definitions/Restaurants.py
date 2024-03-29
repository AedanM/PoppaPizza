"""Def of all restaurants"""

from dataclasses import dataclass

import pygame

from Definitions import AssetLibrary, ColorDefines, CustomEvents
from Definitions.DefinedLocations import LocationDefs
from Engine import Color, Utils


@dataclass
class LockerRoom:
    """Locker Room Parameters"""

    Location: tuple
    Color: Color.Color
    Unlocked: bool = False
    Price: float = 10000.0


@dataclass()
class Restaurant:
    """Restaurant Class"""

    Name: str
    Logo: AssetLibrary.ImageTypes | None
    CustomerImageTypes: list[AssetLibrary.ImageTypes]
    WorkerImageTypes: list[AssetLibrary.ImageTypes]
    LockerRoom: LockerRoom
    Size: tuple = (180, 150)

    @property
    def LogoPath(self) -> str | None:
        return AssetLibrary.LogoPaths[self.Logo] if self.Logo else None

    def RequiresChange(self, mousePos, target) -> bool:
        return (
            Utils.PositionInTolerance(pos1=mousePos, pos2=self.LockerRoom.Location, tolerance=75)
            and self.LockerRoom.Unlocked
            and target not in restaurant.WorkerImageTypes  # type: ignore
            and self.WorkerImageTypes
        )


RestaurantList = [
    Restaurant(
        Name="Kitchen",
        CustomerImageTypes=[],
        WorkerImageTypes=[],
        Logo=None,
        LockerRoom=LockerRoom(
            Location=LocationDefs.LockerRoom0,
            Color=ColorDefines.DarkRed,
            Price=0,
            Unlocked=True,
        ),
        Size=(250, 150),
    ),
    Restaurant(
        Name="Formal Dining",
        CustomerImageTypes=[AssetLibrary.ImageTypes.CustomerSuit],
        WorkerImageTypes=[AssetLibrary.ImageTypes.WorkerSuit],
        Logo=AssetLibrary.ImageTypes.LogoSuit,
        LockerRoom=LockerRoom(
            Location=LocationDefs.LockerRoom1,
            Color=ColorDefines.Blue,
            Price=0,
            Unlocked=True,
        ),
    ),
    Restaurant(
        Name="Coffee Shop",
        CustomerImageTypes=[AssetLibrary.ImageTypes.CustomerCoffee],
        WorkerImageTypes=[AssetLibrary.ImageTypes.WorkerCoffee],
        Logo=AssetLibrary.ImageTypes.LogoCoffee,
        LockerRoom=LockerRoom(
            Location=LocationDefs.LockerRoom2,
            Color=ColorDefines.Yellow,
            Price=2500,
        ),
    ),
    Restaurant(
        Name="Sundown Luau",
        CustomerImageTypes=[AssetLibrary.ImageTypes.CustomerLuau],
        WorkerImageTypes=[AssetLibrary.ImageTypes.WorkerLuau],
        Logo=AssetLibrary.ImageTypes.LogoLuau,
        LockerRoom=LockerRoom(
            Location=LocationDefs.LockerRoom3,
            Color=ColorDefines.Pink,
            Price=5000,
        ),
    ),
    Restaurant(
        Name="Cowboy Saloon",
        CustomerImageTypes=[AssetLibrary.ImageTypes.CustomerCowboy],
        WorkerImageTypes=[AssetLibrary.ImageTypes.WorkerCowboy],
        Logo=AssetLibrary.ImageTypes.LogoCowboy,
        LockerRoom=LockerRoom(
            Location=LocationDefs.LockerRoom4,
            Color=ColorDefines.Brown,
            Price=7500,
        ),
    ),
    Restaurant(
        Name="Safari Party",
        CustomerImageTypes=[AssetLibrary.ImageTypes.CustomerSafari],
        WorkerImageTypes=[AssetLibrary.ImageTypes.WorkerSafari],
        Logo=AssetLibrary.ImageTypes.LogoSafari,
        LockerRoom=LockerRoom(
            Location=LocationDefs.LockerRoom5,
            Color=ColorDefines.Green,
            Price=10000,
        ),
    ),
]


def UnlockLockerRoom(currentCash, position) -> float:
    """Unlocks a locker room from position
        Returns 0 if too expensive
    Args-
        currentCash (float): Current Money Reserves
        position (int): Locker Room Position

    Returns-
        float: Price Paid for Locker Room
    """
    restaurant = [x for x in RestaurantList if position == x.LockerRoom.Location]
    lockerRoom = restaurant[0].LockerRoom
    if currentCash > lockerRoom.Price:
        lockerRoom.Unlocked = True
        pygame.event.post(CustomEvents.UpdateBackground)
        return lockerRoom.Price
    return 0
