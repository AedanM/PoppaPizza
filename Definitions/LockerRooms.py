"""Definitions for LockerRooms"""

from dataclasses import dataclass

import pygame

from Definitions import AssetLibrary, ColorTools, CustomEvents, DefinedLocations


@dataclass
class LockerRoom:
    Name: str
    Logo: AssetLibrary.ImageTypes
    Location: tuple
    WorkerOutfits: list
    CustomerOutfits: list
    Color: ColorTools.Color
    Unlocked: bool = False
    Price: float = 10000.0

    @property
    def WorkerImageTypes(self) -> AssetLibrary.ImageTypes:
        return [AssetLibrary.PathToTypeDict[x] for x in self.WorkerOutfits]

    @property
    def Path(self) -> AssetLibrary.ImagePaths:
        return AssetLibrary.LockerRoomPaths[self.Logo]


LockerRooms = [
    LockerRoom(
        Name="Formal Dining",
        Logo=AssetLibrary.ImageTypes.SuitLogo,
        Location=DefinedLocations.LocationDefs.LockerRoom1,
        WorkerOutfits=[AssetLibrary.ImagePaths.WorkerSuitPath],
        CustomerOutfits=[],
        Color=ColorTools.Blue,
        Unlocked=True,
        Price=0,
    ),
    LockerRoom(
        Name="Coffee Shop",
        Logo=AssetLibrary.ImageTypes.CoffeeLogo,
        Location=DefinedLocations.LocationDefs.LockerRoom2,
        WorkerOutfits=[AssetLibrary.ImagePaths.WorkerCoffeePath],
        CustomerOutfits=[],
        Color=ColorTools.Yellow,
        Price=2500,
    ),
    LockerRoom(
        Name="Sundown Luau",
        Logo=AssetLibrary.ImageTypes.LuauLogo,
        Location=DefinedLocations.LocationDefs.LockerRoom3,
        WorkerOutfits=[AssetLibrary.ImagePaths.WorkerLuauPath],
        CustomerOutfits=[],
        Color=ColorTools.Pink,
        Price=5000,
    ),
    LockerRoom(
        Name="Cowboy Saloon",
        Logo=AssetLibrary.ImageTypes.CowboyLogo,
        Location=DefinedLocations.LocationDefs.LockerRoom4,
        WorkerOutfits=[AssetLibrary.ImagePaths.WorkerCowboyPath],
        CustomerOutfits=[],
        Color=ColorTools.Brown,
        Price=7500,
    ),
    LockerRoom(
        Name="Safari Party",
        Logo=AssetLibrary.ImageTypes.SafariLogo,
        Location=DefinedLocations.LocationDefs.LockerRoom5,
        WorkerOutfits=[AssetLibrary.ImagePaths.WorkerSafariPath],
        CustomerOutfits=[],
        Color=ColorTools.Green,
        Price=10000,
    ),
]


def UnlockLockerRoom(currentCash, position) -> float:
    lockerRoom = [x for x in LockerRooms if position == x.Location]
    if currentCash > lockerRoom[0].Price:
        lockerRoom[0].Unlocked = True
        pygame.event.post(CustomEvents.UpdateBackground)
        return lockerRoom[0].Price
    return 0
