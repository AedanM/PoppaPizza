"""Handler for Worker Tasks"""

import random

from Classes import Game
from Definitions import AssetLibrary
from Definitions import DefinedPaths as DL


def ServeCustomer() -> None:
    pass


def FinishCustomer(ws, j) -> None:
    ws.DataObject.IsAssigned = False
    ws.DataObject.CurrentJobId = 0
    ws.MvmHandler.StartNewListedMotion(DL.DefinedPaths.BackToKitchen(sprite=ws))
    Game.MasterGame.UserInventory.GetPaid(amount=j.Price)
    Game.MasterGame.UserInventory.Statistics.CustomersServed += 1


def GetChanged(ws, restaurant) -> None:
    ws.MvmHandler.StartNewListedMotion(
        DL.DefinedPaths.KitchenToLockerRoom(
            sprite=ws, dest=restaurant.LockerRoom.Location
        )
    )
    newOutfit = AssetLibrary.PathLookup(random.choice(restaurant.WorkerImageTypes))
    ws.MvmHandler.OnComplete = lambda: (
        ws.ChangeOutfit(newOutfit),
        ws.CreatePersonTimerBar(
            completeTask=lambda: ReturnToKitchen(ws=ws), offset=(-30, 150), width=150
        ),
    )


def ReturnToKitchen(ws) -> None:
    ws.MvmHandler.StartNewListedMotion(DL.DefinedPaths.BackToKitchen(sprite=ws))
