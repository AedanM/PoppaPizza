"""Handler for Worker Tasks"""
from Classes import Game, TimerBar as TB
from Definitions import DefinedLocations as DL


def ServeCustomer() -> None:
    pass


def FinishCustomer(w, ws, j) -> None:
    w.IsAssigned = False
    w.CurrentJobId = 0
    ws.MvmHandler.StartNewListedMotion(DL.DefinedPaths.BackToKitchen(sprite=ws))
    Game.MasterGame.UserInventory.GetPaid(amount=j.Price)


def GetChanged(ws, dest) -> None:
    ws.MvmHandler.StartNewListedMotion(
        DL.DefinedPaths.KitchenToLockerRoom(sprite=ws, dest=dest)
    )


def ReturnToKitchen() -> None:
    pass
