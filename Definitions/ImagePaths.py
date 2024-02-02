"""Image Path Define"""

import sys
from dataclasses import dataclass


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
    ButtonPath = AssetFolder + r"\button.png"
    NonePath = AssetFolder + r"\none.png"
