"""Handler for Worker Tasks"""

import random

from Classes import Game
from Definitions import AssetLibrary, DefinedLocations, DefinedPaths
from Utilities import Utils


def DailyReset(sprite) -> None:
    sprite.MvmHandler.Reset()
    spawnLocation = Utils.PositionRandomVariance(
        position=DefinedLocations.LocationDefs.WorkerSpawn,
        percentVarianceTuple=(0.05, 0.25),
        screenSize=DefinedLocations.LocationDefs.ScreenSize,
    )
    sprite.rect.center = spawnLocation


def ServeCustomer() -> None:
    pass


def FinishCustomer(ws, j) -> None:
    ws.DataObject.IsAssigned = False
    ws.DataObject.CurrentJobId = 0
    ws.MvmHandler.StartNewListedMotion(
        DefinedPaths.DefinedPaths.BackToKitchen(sprite=ws)
    )
    Game.MasterGame.UserInventory.GetPaid(amount=j.Price)
    Game.MasterGame.UserInventory.Statistics.ServeCustomer()


def GetChanged(ws, restaurant) -> None:
    ws.MvmHandler.StartNewListedMotion(
        DefinedPaths.DefinedPaths.KitchenToLockerRoom(
            sprite=ws, dest=restaurant.LockerRoom.Location
        )
    )
    newOutfit = AssetLibrary.PathLookup(random.choice(restaurant.WorkerImageTypes))
    ws.MvmHandler.OnComplete = lambda: (
        ws.ChangeOutfit(newOutfit),
        Game.MasterGame.UserInventory.Statistics.WorkerChanged(),
        ws.CreatePersonTimerBar(
            completeTask=lambda: ReturnToKitchen(ws=ws), offset=(-30, 150), width=150
        ),
    )


def ReturnToKitchen(ws) -> None:
    ws.MvmHandler.StartNewListedMotion(
        DefinedPaths.DefinedPaths.BackToKitchen(sprite=ws)
    )
