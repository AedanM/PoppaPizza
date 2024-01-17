"""Handler for Worker Tasks"""
import pygame


def GoToCustomer(c, cs, w, ws):
    ws.MvmHandler.startNewListedMotion(DL.DefinedPaths.KitchenToCustomer(ws, cs))
    returnHome = lambda: FinishCustomer(c, cs, w, ws)
    ws.MvmHandler.OnComplete = lambda: TB.CreatePersonTimerBar(
        ws, returnHome, c.desiredJob.Length
    )


def ServeCustomer(ws):
    pass


def FinishCustomer(c, cs, w, ws):
    pass


def ReturnToKitchen():
    pass
