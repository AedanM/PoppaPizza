"""Asset loading"""

from enum import Enum

import pygame

from Definitions import ImagePaths

ImagePath = ImagePaths.ImagePaths()


class ImageTypes(Enum):
    """Types of Images"""

    (
        Null,
        LogoCoffee,
        LogoCowboy,
        CustomerCoffee,
        CustomerCowboy,
        CustomerLuau,
        CustomerSafari,
        CustomerSuit,
        LogoLockedRoom,
        LogoLuau,
        LogoSafari,
        LogoSuit,
        Table,
        WorkerCoffee,
        WorkerCowboy,
        WorkerLuau,
        WorkerSafari,
        WorkerSuit,
        *_,
    ) = range(50)


CustomerOutfits = [
    ImageTypes.CustomerCoffee,
    ImageTypes.CustomerCowboy,
    ImageTypes.CustomerLuau,
    ImageTypes.CustomerSafari,
    ImageTypes.CustomerSuit,
]

WorkerOutfits = [
    ImageTypes.WorkerSuit,
    ImageTypes.WorkerCowboy,
    ImageTypes.WorkerLuau,
    ImageTypes.WorkerSafari,
    ImageTypes.WorkerCoffee,
]

LogoPaths = {
    ImageTypes.LogoCoffee: ImagePath.LogoCoffeePath,
    ImageTypes.LogoCowboy: ImagePath.LogoCowboyPath,
    ImageTypes.LogoLuau: ImagePath.LogoLuauPath,
    ImageTypes.LogoSuit: ImagePath.LogoSuitPath,
    ImageTypes.LogoSafari: ImagePath.LogoSafariPath,
}


def PathLookup(imageType) -> str | None:
    """Looks up path for image type

    Args:
        imageType (ImageType): Image Type to Find Path for

    Returns:
        str: Image Path
    """
    for key, value in PathToTypeDict.items():
        if value == imageType:
            return key
    return ImagePath.NonePath


PathToTypeDict = {
    ImagePath.CustomerCoffeePath: ImageTypes.CustomerCoffee,
    ImagePath.CustomerCowboyPath: ImageTypes.CustomerCowboy,
    ImagePath.CustomerLuauPath: ImageTypes.CustomerLuau,
    ImagePath.CustomerSafariPath: ImageTypes.CustomerSafari,
    ImagePath.CustomerSuitPath: ImageTypes.CustomerSuit,
    ImagePath.LogoCoffeePath: ImageTypes.LogoCoffee,
    ImagePath.LogoCowboyPath: ImageTypes.LogoCowboy,
    ImagePath.LogoLockedPath: ImageTypes.LogoLockedRoom,
    ImagePath.LogoLuauPath: ImageTypes.LogoLuau,
    ImagePath.LogoSafariPath: ImageTypes.LogoSafari,
    ImagePath.LogoSuitPath: ImageTypes.LogoSuit,
    ImagePath.NonePath: ImageTypes.Null,
    ImagePath.TablePath: ImageTypes.Table,
    ImagePath.WorkerCoffeePath: ImageTypes.WorkerCoffee,
    ImagePath.WorkerCowboyPath: ImageTypes.WorkerCowboy,
    ImagePath.WorkerLuauPath: ImageTypes.WorkerLuau,
    ImagePath.WorkerSafariPath: ImageTypes.WorkerSafari,
    ImagePath.WorkerSuitPath: ImageTypes.WorkerSuit,
}
Background = pygame.image.load(ImagePath.BackgroundPath)
TriviaBackground = pygame.image.load(ImagePath.TriviaBackgroundPath)
