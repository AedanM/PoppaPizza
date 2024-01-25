"""Handler for Customer Tasks"""
import random
import pygame
from Classes import Game
from Definitions import CustomEvents, CustomerStates, DefinedPaths as DL
from Handlers import WorkerHandler as WH


# TODO - Fix getting worker who is busy
def FindAvailableWorker(activeGame=Game.MasterGame) -> tuple:
    availWorkers = [x for x in activeGame.WorkerList if x.IsAssigned is False]
    if len(availWorkers) < 1:
        worker, workerSprite = None, None
    else:
        worker = random.choice(availWorkers)
        workerSprite = activeGame.MatchIdToPerson(
            inputId=worker.IdNum, targetOutput="sprite"
        )

    return worker, workerSprite


# TODO - Stop 2 workers on 1 job
def AssignWorker(target, activeGame=Game.MasterGame) -> None:
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
        target.DataObject.CurrentState = CustomerStates.CustomerStates.Served
        returnHome = lambda: (
            GetUpAndGo(spriteImg=target),
            WH.FinishCustomer(ws=workerSprite, j=target.DataObject.DesiredJob),
        )
        workerSprite.MvmHandler.OnComplete = lambda: workerSprite.CreatePersonTimerBar(
            completeTask=returnHome,
            length=target.DataObject.DesiredJob.Length,
        )


def SitAtTable(target) -> None:
    path = DL.DefinedPaths.CustomerToRandomSeat(sprite=target)
    if path is not None:
        target.MvmHandler.StartNewListedMotion(path)
        target.DataObject.CurrentState = CustomerStates.CustomerStates.Seated
        target.MvmHandler.OnComplete = lambda: BeginWait(target=target)
    else:
        target.DataObject.CurrentState = CustomerStates.CustomerStates.LeavingAngry
        AllTablesBusy(target=target)


def AllTablesBusy(target) -> None:
    GetUpAndGo(spriteImg=target)


def BeginWait(target) -> None:
    target.DataObject.CurrentState = CustomerStates.CustomerStates.WaitingForService
    taskComplete = lambda: GetUpAndGo(spriteImg=target)
    target.CreatePersonTimerBar(
        completeTask=taskComplete,
        length=(target.DataObject.DesiredJob.Urgency.value * 30.0),
        assocId=target.DataObject.IdNum,
        startingState=target.DataObject.CurrentState.value,
    )


def AllWorkersBusy(target) -> None:
    taskComplete = lambda: GetUpAndGo(spriteImg=target)
    target.DataObject.CurrentState = CustomerStates.CustomerStates.Waiting
    target.CreatePersonTimerBar(completeTask=taskComplete, length=10)


def GetUpAndGo(spriteImg, activeGame=Game.MasterGame) -> None:
    if (
        not spriteImg.DataObject.WorkerAssigned
        or spriteImg.DataObject.CurrentState is CustomerStates.CustomerStates.Served
    ):
        spriteImg.MvmHandler.StartNewListedMotion(
            DL.DefinedPaths.CustomerToExit(sprite=spriteImg)
            if spriteImg.DataObject.CurrentState
            == CustomerStates.CustomerStates.Queuing
            else DL.DefinedPaths.TableToExit(sprite=spriteImg)
        )

        spriteImg.MvmHandler.OnComplete = lambda: activeGame.RemoveObjFromSprite(
            targetSprite=spriteImg
        )
