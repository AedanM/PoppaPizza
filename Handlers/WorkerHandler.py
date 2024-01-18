"""Handler for Worker Tasks"""
import Classes.DefinedLocations as DL
import Classes.TimerBar as TB


def GoToCustomer(c, cs, w, ws):
    ws.MvmHandler.startNewListedMotion(DL.DefinedPaths.KitchenToCustomer(ws, cs))
    returnHome = lambda: FinishCustomer(w, ws)
    ws.MvmHandler.OnComplete = lambda: TB.CreatePersonTimerBar(
        ws, returnHome, c.desiredJob.Length
    )


def ServeCustomer():
    pass


def FinishCustomer(w, ws):
    w.IsAssigned = False
    w.CurrentJobId = 0
    ws.MvmHandler.StartNewListedMotion(DL.DefinedPaths.BackToKitchen(ws))


def ReturnToKitchen():
    pass
