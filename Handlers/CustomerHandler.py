"""Handler for Customer Tasks"""
import random
import pygame
from Classes import Game, People
from Definitions import CustomEvents, DefinedPaths as DL
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
def AssignWorker(target, targetObj, activeGame=Game.MasterGame) -> None:
    worker, workerSprite = FindAvailableWorker()
    if worker is None:
        AllWorkersBusy(target=target)
    else:
        targetObj.WorkerAssigned = True
        targetObj.DesiredJob.Assign(worker)
        workerSprite.MvmHandler.StartNewListedMotion(
            pointList=DL.DefinedPaths.KitchenToCustomer(
                sprite=workerSprite, dest=target
            )
        )
        targetObj.CurrentState = People.CustomerStates.Served
        returnHome = lambda: (
            GetUpAndGo(spriteImg=target),
            WH.FinishCustomer(w=worker, ws=workerSprite, j=targetObj.DesiredJob),
        )
        workerSprite.MvmHandler.OnComplete = lambda: workerSprite.CreatePersonTimerBar(
            completeTask=returnHome,
            length=targetObj.DesiredJob.Length,
        )


def SitAtTable(target, customer) -> None:
    path = DL.DefinedPaths.CustomerToRandomSeat(sprite=target)
    if path is not None:
        target.MvmHandler.StartNewListedMotion(path)
        customer.CurrentState = People.CustomerStates.Seated
        target.MvmHandler.OnComplete = lambda: BeginWait(
            target=target, customer=customer
        )
    else:
        customer.CurrentState = People.CustomerStates.LeavingAngry
        AllTablesBusy(target=target)


def AllTablesBusy(target) -> None:
    GetUpAndGo(spriteImg=target)


def BeginWait(target, customer) -> None:
    customer.CurrentState = People.CustomerStates.WaitingForService
    taskComplete = lambda: GetUpAndGo(spriteImg=target)
    target.CreatePersonTimerBar(
        completeTask=taskComplete,
        length=(customer.DesiredJob.Urgency.value * 30.0),
        assocId=customer.IdNum,
        startingState=customer.CurrentState.value,
    )


def AllWorkersBusy(target) -> None:
    customer = Game.MasterGame.MatchIdToPerson(
        inputId=target.CorrespondingID, targetOutput="customer"
    )
    taskComplete = lambda: GetUpAndGo(spriteImg=target)
    customer.CurrentState = People.CustomerStates.Waiting
    target.CreatePersonTimerBar(completeTask=taskComplete, length=10)


def GetUpAndGo(spriteImg, activeGame=Game.MasterGame) -> None:
    customer = activeGame.MatchIdToPerson(
        inputId=spriteImg.CorrespondingID, targetOutput="customer"
    )
    if (
        not customer.WorkerAssigned
        or customer.CurrentState is People.CustomerStates.Served
    ):
        spriteImg.MvmHandler.StartNewListedMotion(
            DL.DefinedPaths.CustomerToExit(sprite=spriteImg)
            if customer.CurrentState == People.CustomerStates.Queuing
            else DL.DefinedPaths.TableToExit(sprite=spriteImg)
        )

        spriteImg.MvmHandler.OnComplete = lambda: activeGame.RemoveObjFromSprite(
            targetSprite=spriteImg
        )
    # Game.MasterGame.UserInventory.GetPaid(customer.DesiredJob.Price)
