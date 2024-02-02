"""Handler for Customer Tasks"""

import random

import Classes.Matching
from Classes import Game
from Definitions import ColorTools, CustomerDefs
from Definitions import DefinedPaths as DL
from Handlers import WorkerHandler as WH


def SetFirstInLine(target) -> None:
    if target.MvmHandler.IsFinished(target):
        target.DataObject.CurrentState = CustomerDefs.CustomerStates.FirstInLine


def WalkIn(target) -> None:
    target.MvmHandler.StartNewListedMotion(
        DL.DefinedPaths.CustomerToEntrance(sprite=target)
    )
    target.DataObject.CurrentState = CustomerDefs.CustomerStates.WalkingIn
    target.MvmHandler.OnComplete = lambda: (SetFirstInLine(target=target))


# TODO - Fix getting worker who is busy
def FindAvailableWorker(activeGame=Game.MasterGame) -> tuple:
    availWorkers = [x for x in activeGame.WorkerList if x.IsAssigned is False]
    if len(availWorkers) < 1:
        worker, workerSprite = None, None
    else:
        worker = random.choice(availWorkers)
        workerSprite = Classes.Matching.MatchIdToPerson(
            activeGame=activeGame, inputId=worker.IdNum, targetOutput="sprite"
        )

    return worker, workerSprite


# TODO - Stop 2 workers on 1 job
def AssignWorker(target) -> None:
    worker, workerSprite = FindAvailableWorker()
    if worker is None:
        AllWorkersBusy(target=target)
    else:
        target.DataObject.WorkerAssigned = True
        target.DataObject.DesiredJob.Assign(worker)
        workerSprite.MvmHandler.StartNewListedMotion(
            pointList=DL.DefinedPaths.KitchenToCustomer(
                sprite=workerSprite, dest=target
            )
        )
        target.DataObject.CurrentState = CustomerDefs.CustomerStates.Served
        returnHome = lambda: (
            GetUpAndGo(spriteImg=target),
            WH.FinishCustomer(ws=workerSprite, j=target.DataObject.DesiredJob),
        )
        workerSprite.MvmHandler.OnComplete = lambda: workerSprite.CreatePersonTimerBar(
            completeTask=returnHome,
            length=target.DataObject.DesiredJob.Length,
        )


def SitAtTable(target) -> None:
    target.DataObject.CurrentState = CustomerDefs.CustomerStates.Seated
    path = DL.DefinedPaths.CustomerToRandomSeat(sprite=target)
    if path is not None:
        target.MvmHandler.StartNewListedMotion(path)
        target.MvmHandler.OnComplete = lambda: BeginWait(target=target)
    else:
        target.DataObject.CurrentState = CustomerDefs.CustomerStates.LeavingAngry
        AllTablesBusy(target=target)


def AllTablesBusy(target) -> None:
    GetUpAndGo(spriteImg=target)


def BeginWait(target) -> None:
    target.DataObject.CurrentState = CustomerDefs.CustomerStates.WaitingForService
    taskComplete = lambda: GetUpAndGo(spriteImg=target)
    target.CreatePersonTimerBar(
        completeTask=taskComplete,
        length=(target.DataObject.DesiredJob.Urgency.value * 30.0),
        assocId=target.DataObject.IdNum,
        startingState=target.DataObject.CurrentState.value,
        fillColor=ColorTools.Red,
    )


def AllWorkersBusy(target) -> None:
    taskComplete = lambda: GetUpAndGo(spriteImg=target)
    target.DataObject.CurrentState = CustomerDefs.CustomerStates.WaitingForService
    target.CreatePersonTimerBar(completeTask=taskComplete, length=10)


def GetUpAndGo(spriteImg, activeGame=Game.MasterGame) -> None:
    if (
        not spriteImg.DataObject.WorkerAssigned
        or spriteImg.DataObject.CurrentState is CustomerDefs.CustomerStates.Served
    ):
        spriteImg.MvmHandler.StartNewListedMotion(
            DL.DefinedPaths.CustomerToExit(sprite=spriteImg)
            if spriteImg.DataObject.CurrentState == CustomerDefs.CustomerStates.Queuing
            else DL.DefinedPaths.TableToExit(sprite=spriteImg)
        )

        spriteImg.MvmHandler.OnComplete = lambda: Classes.Matching.RemoveObjFromSprite(
            activeGame=activeGame, targetSprite=spriteImg
        )
