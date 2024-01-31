"""Asset loading"""
import sys
from dataclasses import dataclass
from enum import Enum


@dataclass
class ImagePaths:
    # pylint: disable=W0212, E1101
    AssetFolder = r"Assets" if not hasattr(sys, "_MEIPASS") else sys._MEIPASS
    WorkerSuitPath = AssetFolder + r"\workerSuit.png"
    WorkerCoffeePath = AssetFolder + r"\workerCoffee.png"
    WorkerLuauPath = AssetFolder + r"\workerLuau.png"
    WorkerSafariPath = AssetFolder + r"\workerSafari.png"
    WorkerCowboyPath = AssetFolder + r"\workerCowboy.png"
    CustomerPath = AssetFolder + r"\person.png"
    TablePath = AssetFolder + r"\table.png"
    BackgroundPath = AssetFolder + r"\background.png"
    GameOverPath = AssetFolder + r"\gameOver.png"
    CoffeePath = AssetFolder + r"\coffee.png"
    CowboyPath = AssetFolder + r"\cowboySaloon.png"
    LuauPath = AssetFolder + r"\luau.png"
    SuitPath = AssetFolder + r"\suit.png"
    SafariPath = AssetFolder + r"\safari.png"
    LockedLockerRoomPath = AssetFolder + r"\LockedLockerRoom.png"


class ImageTypes(Enum):
    (
        Null,
        WorkerSuit,
        WorkerCowboy,
        WorkerLuau,
        WorkerSafari,
        WorkerCoffee,
        Customer,
        Table,
        CoffeeLogo,
        CowboyLogo,
        LuauLogo,
        SuitLogo,
        SafariLogo,
        LockedLockerRoomLogo,
    ) = range(14)


CustomerOutfits = [ImageTypes.Customer]
WorkerOutfits = [
    ImageTypes.WorkerSuit,
    ImageTypes.WorkerCowboy,
    ImageTypes.WorkerLuau,
    ImageTypes.WorkerSafari,
    ImageTypes.WorkerCoffee,
]

LockerRoomPaths = {
    ImageTypes.CoffeeLogo: ImagePaths.CoffeePath,
    ImageTypes.CowboyLogo: ImagePaths.CowboyPath,
    ImageTypes.LuauLogo: ImagePaths.LuauPath,
    ImageTypes.SuitLogo: ImagePaths.SuitPath,
    ImageTypes.SafariLogo: ImagePaths.SafariPath,
}

People = WorkerOutfits + CustomerOutfits

ImagePath = ImagePaths()

PathToTypeDict = {
    ImagePath.WorkerCoffeePath: ImageTypes.WorkerCoffee,
    ImagePath.WorkerCowboyPath: ImageTypes.WorkerCowboy,
    ImagePath.WorkerLuauPath: ImageTypes.WorkerLuau,
    ImagePath.WorkerSafariPath: ImageTypes.WorkerSafari,
    ImagePath.WorkerSuitPath: ImageTypes.WorkerSuit,
    ImagePath.CustomerPath: ImageTypes.Customer,
    ImagePath.TablePath: ImageTypes.Table,
    ImagePath.CoffeePath: ImageTypes.CoffeeLogo,
    ImagePath.CowboyPath: ImageTypes.CowboyLogo,
    ImagePath.LuauPath: ImageTypes.LuauLogo,
    ImagePath.SuitPath: ImageTypes.SuitLogo,
    ImagePath.SafariPath: ImageTypes.SafariLogo,
    ImagePath.LockedLockerRoomPath: ImageTypes.LockedLockerRoomLogo,
}
