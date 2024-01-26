"""Handler for Worker Tasks"""
from Classes import Game
from Definitions import DefinedPaths as DL, LockerRooms


def ServeCustomer() -> None:
    pass


def FinishCustomer(ws, j) -> None:
    ws.DataObject.IsAssigned = False
    ws.DataObject.CurrentJobId = 0
    ws.MvmHandler.StartNewListedMotion(DL.DefinedPaths.BackToKitchen(sprite=ws))
    Game.MasterGame.UserInventory.GetPaid(amount=j.Price)


def GetChanged(ws, dest) -> None:
    ws.MvmHandler.StartNewListedMotion(
        DL.DefinedPaths.KitchenToLockerRoom(sprite=ws, dest=dest)
    )
    newOutfit = LockerRooms.LockerRoomOutfits[dest]
    ws.MvmHandler.OnComplete = lambda: (
        ws.ChangeOutfit(newOutfit),
        ws.CreatePersonTimerBar(
            completeTask=lambda: ReturnToKitchen(ws), offset=(-30, 150), width=150
        ),
    )


def ReturnToKitchen(ws) -> None:
    ws.MvmHandler.StartNewListedMotion(DL.DefinedPaths.BackToKitchen(sprite=ws))
