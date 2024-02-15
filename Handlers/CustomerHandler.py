"""Handler for Customer Tasks"""

import random

from Classes import Matching
from Definitions import ColorDefines
from Definitions.CustomerDefs import CustomerStates
from Definitions.DefinedPaths import DefinedPaths
from Handlers import WorkerHandler as WH


# TODO - Examine this with Queueing
def SetFirstInLine(target) -> None:
    """Function for setting Queuing

        After Motion, the customer is set first if

    Args-
        target (_type_): _description_
    """
    if target.MvmHandler.IsFinished(target):
        target.DataObject.CurrentState = CustomerStates.FirstInLine


def WalkIn(target) -> None:
    """Initial Operations of a Customer

    Args-
        target (Sprite): Target Customer
    """
    target.MvmHandler.StartNewListedMotion(DefinedPaths.CustomerToEntrance(sprite=target))
    target.DataObject.CurrentState = CustomerStates.WalkingIn
    target.MvmHandler.OnComplete = lambda: (SetFirstInLine(target=target))


def FindAvailableWorker(customerSprite, activeGame) -> tuple:
    """Check if there are available workers and returns None if not

    Args-
        customerSprite (CharImageSprite): Customer Sprite requesting Job
        activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.

    Returns-
        tuple: (Worker, Sprite Object of Worker)
    """
    availWorkers = [x for x in activeGame.WorkerList if x.IsAssigned is False]
    random.shuffle(availWorkers)
    for worker in availWorkers:
        workerSprite = Matching.MatchIdToPerson(
            activeGame=activeGame, inputId=worker.IdNum, targetOutput="sprite"
        )
        if Matching.CostumeMatch(workerSprite=workerSprite, customerSprite=customerSprite):
            return worker, workerSprite

    return None, None


# BUG - Stop the workers going on strike
def AssignWorker(target, activeGame) -> None:
    """Finds an availbale worker for a job and assigns them

        Starts the Worker Handler flow

    Args-
        target (CharImageSprite): Customer Sprite requesting Job
    """
    worker, workerSprite = FindAvailableWorker(customerSprite=target, activeGame=activeGame)
    if worker is not None and target.MvmHandler.InMotion is False:
        target.DataObject.WorkerAssigned = True
        target.DataObject.DesiredJob.Assign(worker)
        workerSprite.MvmHandler.StartNewListedMotion(
            pointList=DefinedPaths.KitchenToCustomer(sprite=workerSprite, dest=target)
        )
        target.DataObject.CurrentState = CustomerStates.Served
        returnHome = lambda: (
            GetUpAndGo(spriteImg=target, activeGame=activeGame),
            WH.FinishCustomer(
                workerSprite=workerSprite, job=target.DataObject.DesiredJob, activeGame=activeGame
            ),
        )
        workerSprite.MvmHandler.OnComplete = lambda: workerSprite.CreatePersonTimerBar(
            activeGame=activeGame,
            completeTask=returnHome,
            length=target.DataObject.DesiredJob.Length,
        )


def SitAtTable(target, activeGame) -> None:
    """Logic for a Queuing Customer to sit down

    Args-
        target (CharImageSprite): Sprite of Target Customer
    """
    target.DataObject.CurrentState = CustomerStates.Seated
    path = DefinedPaths.CustomerToRandomSeat(sprite=target)
    if path is not None:
        target.MvmHandler.StartNewListedMotion(path)
        target.MvmHandler.OnComplete = lambda: BeginWait(target=target, activeGame=activeGame)
    else:
        target.DataObject.CurrentState = CustomerStates.LeavingAngry
        GetUpAndGo(spriteImg=target, activeGame=activeGame)


def BeginWait(target, activeGame) -> None:
    """Starts the timer for a customer waiting for service

    Args-
        target (CharImageSprite): Sprite of Target Customer
    """
    target.DataObject.CurrentState = CustomerStates.WaitingForService
    taskComplete = lambda: GetUpAndGo(spriteImg=target, activeGame=activeGame)
    target.CreatePersonTimerBar(
        activeGame=activeGame,
        completeTask=taskComplete,
        length=(target.DataObject.DesiredJob.Urgency.value * 30.0),
        assocId=target.DataObject.IdNum,
        startingState=target.DataObject.CurrentState.value,
        fillColor=ColorDefines.DarkRed,
    )


def AllWorkersBusy(target, activeGame) -> None:
    """Routine for when all workers are busy

    Args-
        target (CharImageSprite): Sprite of Target Customer
    """
    taskComplete = lambda: GetUpAndGo(spriteImg=target, activeGame=activeGame)
    target.DataObject.CurrentState = CustomerStates.WaitingForService
    target.CreatePersonTimerBar(activeGame=activeGame, completeTask=taskComplete, length=10)


def GetUpAndGo(spriteImg, activeGame) -> None:
    """Logic for a Customer to leave the restaurant

    Args-
        spriteImg (CharImageSprite): Sprite of Target Customer
        activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.
    """
    if (
        not spriteImg.DataObject.WorkerAssigned
        or spriteImg.DataObject.CurrentState is CustomerStates.Served
    ):
        spriteImg.MvmHandler.StartNewListedMotion(
            DefinedPaths.CustomerToExit(sprite=spriteImg)
            if spriteImg.DataObject.CurrentState == CustomerStates.Queuing
            else DefinedPaths.TableToExit(sprite=spriteImg)
        )

        spriteImg.MvmHandler.OnComplete = lambda: Matching.RemoveObjFromSprite(
            activeGame=activeGame, targetSprite=spriteImg
        )
