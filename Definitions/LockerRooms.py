"""Definitions for LockerRooms"""
from dataclasses import dataclass

from Definitions import AssetLibrary, ColorTools, DefinedLocations


@dataclass
class LockerRoom:
    Name: str
    Logo: AssetLibrary.ImageTypes
    Location: tuple
    WorkerOutfits: list
    CustomerOutfits: list
    Color: ColorTools.Color
    Unlocked: bool = False

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
    ),
    LockerRoom(
        Name="Coffee Shop",
        Logo=AssetLibrary.ImageTypes.CoffeeLogo,
        Location=DefinedLocations.LocationDefs.LockerRoom2,
        WorkerOutfits=[AssetLibrary.ImagePaths.WorkerCoffeePath],
        CustomerOutfits=[],
        Color=ColorTools.Yellow,
    ),
    LockerRoom(
        Name="Cowboy Saloon",
        Logo=AssetLibrary.ImageTypes.CowboyLogo,
        Location=DefinedLocations.LocationDefs.LockerRoom3,
        WorkerOutfits=[AssetLibrary.ImagePaths.WorkerCowboyPath],
        CustomerOutfits=[],
        Color=ColorTools.Brown,
        Unlocked=True,
    ),
    LockerRoom(
        Name="Sundown Luau",
        Logo=AssetLibrary.ImageTypes.LuauLogo,
        Location=DefinedLocations.LocationDefs.LockerRoom4,
        WorkerOutfits=[AssetLibrary.ImagePaths.WorkerLuauPath],
        CustomerOutfits=[],
        Color=ColorTools.Pink,
    ),
    LockerRoom(
        Name="Safari Party",
        Logo=AssetLibrary.ImageTypes.SafariLogo,
        Location=DefinedLocations.LocationDefs.LockerRoom5,
        WorkerOutfits=[AssetLibrary.ImagePaths.WorkerSafariPath],
        CustomerOutfits=[],
        Color=ColorTools.Green,
    ),
]
