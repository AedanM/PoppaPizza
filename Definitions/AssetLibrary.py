"""Asset loading"""

from enum import Enum

from Definitions import ImagePaths

ImagePath = ImagePaths.ImagePaths()


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
        Button,
    ) = range(15)


CustomerOutfits = [ImageTypes.Customer]

WorkerOutfits = [
    ImageTypes.WorkerSuit,
    ImageTypes.WorkerCowboy,
    ImageTypes.WorkerLuau,
    ImageTypes.WorkerSafari,
    ImageTypes.WorkerCoffee,
]

LogoPaths = {
    ImageTypes.CoffeeLogo: ImagePath.CoffeePath,
    ImageTypes.CowboyLogo: ImagePath.CowboyPath,
    ImageTypes.LuauLogo: ImagePath.LuauPath,
    ImageTypes.SuitLogo: ImagePath.SuitPath,
    ImageTypes.SafariLogo: ImagePath.SafariPath,
}

People = WorkerOutfits + CustomerOutfits


def PathLookup(imageType) -> str | None:
    for key, value in PathToTypeDict.items():
        if value is imageType:
            return key
    return ImagePath.NonePath


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
    ImagePath.ButtonPath: ImageTypes.Button,
    ImagePath.NonePath: ImageTypes.Null,
}
