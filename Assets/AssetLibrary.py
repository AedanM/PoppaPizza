from dataclasses import dataclass
from enum import Enum


@dataclass
class ImagePaths:
    AssetFolder = r"Assets"
    WorkerSuitPath = AssetFolder + r"\waiter.png"
    CustomerPath = AssetFolder + r"\person.png"
    TablePath = AssetFolder + r"\table.png"
    BackgroundPath = AssetFolder + r"\background.png"
    CoffeePath = AssetFolder + r"\coffee.png"
    CowboyPath = AssetFolder + r"\cowboySaloon.png"
    LuauPath = AssetFolder + r"\Luau.png"
    SuitPath = AssetFolder + r"\suit.png"
    SafariPath = AssetFolder + r"\safari.png"


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
    ) = range(13)


WorkerOutfits = [
    ImageTypes.WorkerSuit,
    ImageTypes.WorkerCowboy,
    ImageTypes.WorkerLuau,
    ImageTypes.WorkerSafari,
    ImageTypes.WorkerCoffee,
]
CustomerOutfits = [ImageTypes.Customer]
People = WorkerOutfits + CustomerOutfits

ImagePath = ImagePaths()


PathToTypeDict = {
    ImagePath.WorkerSuitPath: ImageTypes.WorkerSuit,
    ImagePath.CustomerPath: ImageTypes.Customer,
    ImagePath.TablePath: ImageTypes.Table,
    ImagePath.CoffeePath: ImageTypes.CoffeeLogo,
    ImagePath.CowboyPath: ImageTypes.CowboyLogo,
    ImagePath.LuauPath: ImageTypes.LuauLogo,
    ImagePath.SuitPath: ImageTypes.SuitLogo,
    ImagePath.SafariPath: ImageTypes.SafariLogo,
}
