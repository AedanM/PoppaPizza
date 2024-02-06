"""Image Path Define"""

import sys
from dataclasses import dataclass


@dataclass
class ImagePaths:
    """Object to hold all image paths and handle packaging"""

    # pylint: disable=W0212, E1101
    AssetFolder = r"Assets" if not hasattr(sys, "_MEIPASS") else sys._MEIPASS
    BackgroundPath = AssetFolder + r"\background.png"
    ButtonPath = AssetFolder + r"\button.png"

    CustomerCoffeePath = AssetFolder + r"\customerCoffee.png"
    CustomerCowboyPath = AssetFolder + r"\customerCowboy.png"
    CustomerLuauPath = AssetFolder + r"\customerLuau.png"
    CustomerSafariPath = AssetFolder + r"\customerSafari.png"
    CustomerSuitPath = AssetFolder + r"\customerSuit.png"

    LogoLockedPath = AssetFolder + r"\LockedLockerRoom.png"

    LogoCoffeePath = AssetFolder + r"\coffee.png"
    LogoCowboyPath = AssetFolder + r"\cowboySaloon.png"
    LogoLuauPath = AssetFolder + r"\luau.png"
    LogoSafariPath = AssetFolder + r"\safari.png"
    LogoSuitPath = AssetFolder + r"\suit.png"

    NonePath = AssetFolder + r"\none.png"
    TablePath = AssetFolder + r"\table.png"

    WorkerCoffeePath = AssetFolder + r"\workerCoffee.png"
    WorkerCowboyPath = AssetFolder + r"\workerCowboy.png"
    WorkerLuauPath = AssetFolder + r"\workerLuau.png"
    WorkerSafariPath = AssetFolder + r"\workerSafari.png"
    WorkerSuitPath = AssetFolder + r"\workerSuit.png"
