"""Image Path Define"""

import sys
from dataclasses import dataclass


@dataclass
class ImagePaths:
    """Object to hold all image paths and handle packaging"""

    # pylint: disable=W0212, E1101
    AssetFolder = r"Assets" if not hasattr(sys, "_MEIPASS") else sys._MEIPASS  # type: ignore
    BackgroundPath = AssetFolder + r"\Backgrounds\background.png"
    TriviaBackgroundPath = AssetFolder + r"\Backgrounds\triviaBackground.png"
    LightMaskPath = AssetFolder + r"\Backgrounds\lightMask.png"

    CustomerCoffeePath = AssetFolder + r"\Customers\customerCoffee.png"
    CustomerCowboyPath = AssetFolder + r"\Customers\customerCowboy.png"
    CustomerLuauPath = AssetFolder + r"\Customers\customerLuau.png"
    CustomerSafariPath = AssetFolder + r"\Customers\customerSafari.png"
    CustomerSuitPath = AssetFolder + r"\Customers\customerSuit.png"

    LogoLockedPath = AssetFolder + r"\Other\LockedLockerRoom.png"

    LogoCoffeePath = AssetFolder + r"\Logos\coffee.png"
    LogoCowboyPath = AssetFolder + r"\Logos\cowboySaloon.png"
    LogoLuauPath = AssetFolder + r"\Logos\luau.png"
    LogoSafariPath = AssetFolder + r"\Logos\safari.png"
    LogoSuitPath = AssetFolder + r"\Logos\suit.png"

    NonePath = AssetFolder + r"\Other\none.png"
    TablePath = AssetFolder + r"\Other\table.png"

    WorkerCoffeePath = AssetFolder + r"\Workers\workerCoffee.png"
    WorkerCowboyPath = AssetFolder + r"\Workers\workerCowboy.png"
    WorkerLuauPath = AssetFolder + r"\Workers\workerLuau.png"
    WorkerSafariPath = AssetFolder + r"\Workers\workerSafari.png"
    WorkerSuitPath = AssetFolder + r"\Workers\workerSuit.png"
