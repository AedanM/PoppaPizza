"""Handler for Worker Tasks"""
import random

from Classes import Game
from Definitions import DefinedPaths as DL


def ServeCustomer() -> None:
    pass


def FinishCustomer(ws, j) -> None:
    ws.DataObject.IsAssigned = False
    ws.DataObject.CurrentJobId = 0
    ws.MvmHandler.StartNewListedMotion(DL.DefinedPaths.BackToKitchen(sprite=ws))
    Game.MasterGame.UserInventory.GetPaid(amount=j.Price)


def GetChanged(ws, lockerRoom) -> None:
    ws.MvmHandler.StartNewListedMotion(
        DL.DefinedPaths.KitchenToLockerRoom(sprite=ws, dest=lockerRoom.Location)
    )
    newOutfit = random.choice(lockerRoom.WorkerOutfits)
    ws.MvmHandler.OnComplete = lambda: (
        ws.ChangeOutfit(newOutfit),
        ws.CreatePersonTimerBar(
            completeTask=lambda: ReturnToKitchen(ws=ws), offset=(-30, 150), width=150
        ),
    )


def ReturnToKitchen(ws) -> None:
    ws.MvmHandler.StartNewListedMotion(DL.DefinedPaths.BackToKitchen(sprite=ws))
