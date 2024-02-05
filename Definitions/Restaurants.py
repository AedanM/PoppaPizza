"""Def of all restaurants"""

from dataclasses import dataclass

import pygame

from Definitions import AssetLibrary, ColorTools, CustomEvents, DefinedLocations


@dataclass
class LockerRoom:
    Location: tuple
    Color: ColorTools.Color
    Unlocked: bool = False
    Price: float = 10000.0


@dataclass()
class Restaurant:
    Name: str
    Logo: AssetLibrary.ImageTypes
    CustomerImageTypes: list[AssetLibrary.ImageTypes]
    WorkerImageTypes: list[AssetLibrary.ImageTypes]
    LockerRoom: LockerRoom

    @property
    def LogoPath(self) -> str:
        return AssetLibrary.LogoPaths[self.Logo]


RestaurantList = [
    Restaurant(
        Name="Formal Dining",
        CustomerImageTypes=[AssetLibrary.ImageTypes.CustomerSuit],
        WorkerImageTypes=[AssetLibrary.ImageTypes.WorkerSuit],
        Logo=AssetLibrary.ImageTypes.LogoSuit,
        LockerRoom=LockerRoom(
            Location=DefinedLocations.LocationDefs.LockerRoom1,
            Color=ColorTools.Blue,
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
            Location=DefinedLocations.LocationDefs.LockerRoom2,
            Color=ColorTools.Yellow,
            Price=2500,
        ),
    ),
    Restaurant(
        Name="Sundown Luau",
        CustomerImageTypes=[AssetLibrary.ImageTypes.CustomerLuau],
        WorkerImageTypes=[AssetLibrary.ImageTypes.WorkerLuau],
        Logo=AssetLibrary.ImageTypes.LogoLuau,
        LockerRoom=LockerRoom(
            Location=DefinedLocations.LocationDefs.LockerRoom3,
            Color=ColorTools.Pink,
            Price=5000,
        ),
    ),
    Restaurant(
        Name="Cowboy Saloon",
        CustomerImageTypes=[AssetLibrary.ImageTypes.CustomerCowboy],
        WorkerImageTypes=[AssetLibrary.ImageTypes.WorkerCowboy],
        Logo=AssetLibrary.ImageTypes.LogoCowboy,
        LockerRoom=LockerRoom(
            Location=DefinedLocations.LocationDefs.LockerRoom4,
            Color=ColorTools.Brown,
            Price=7500,
        ),
    ),
    Restaurant(
        Name="Safari Party",
        CustomerImageTypes=[AssetLibrary.ImageTypes.CustomerSafari],
        WorkerImageTypes=[AssetLibrary.ImageTypes.WorkerSafari],
        Logo=AssetLibrary.ImageTypes.LogoSafari,
        LockerRoom=LockerRoom(
            Location=DefinedLocations.LocationDefs.LockerRoom5,
            Color=ColorTools.Green,
            Price=10000,
        ),
    ),
]


def FindRestaurant(imageType) -> Restaurant | None:
    potentialList = [None]
    if imageType in AssetLibrary.WorkerOutfits:
        potentialList = [x for x in RestaurantList if imageType in x.WorkerImageTypes]
    elif imageType in AssetLibrary.CustomerOutfits:
        potentialList = [x for x in RestaurantList if imageType in x.CustomerImageTypes]
    return potentialList[0]


def UnlockLockerRoom(currentCash, position) -> float:
    restaurant = [x for x in RestaurantList if position == x.LockerRoom.Location]
    lockerRoom = restaurant[0].LockerRoom
    if currentCash > lockerRoom.Price:
        lockerRoom.Unlocked = True
        pygame.event.post(CustomEvents.UpdateBackground)
        return lockerRoom.Price
    return 0
