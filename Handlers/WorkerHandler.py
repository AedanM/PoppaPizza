"""Handler for Worker Tasks"""
from Classes import Game, DefinedLocations as DL, TimerBar as TB


def GoToCustomer(c, cs, w, ws) -> None:
    ws.MvmHandler.startNewListedMotion(
        DL.DefinedPaths.KitchenToCustomer(sprite=ws, dest=cs)
    )
    returnHome = lambda: FinishCustomer(w=w, ws=ws)
    ws.MvmHandler.OnComplete = lambda: TB.CreatePersonTimerBar(
        sprite=ws, completeTask=returnHome, length=c.desiredJob.Length
    )


def ServeCustomer() -> None:
    pass


def FinishCustomer(w, ws, j) -> None:
    w.IsAssigned = False
    w.CurrentJobId = 0
    ws.MvmHandler.StartNewListedMotion(DL.DefinedPaths.BackToKitchen(sprite=ws))
    Game.MasterGame.UserInventory.GetPaid(amount=j.Price)


def ReturnToKitchen() -> None:
    pass
