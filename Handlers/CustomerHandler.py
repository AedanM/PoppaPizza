"""Handler for Customer Tasks"""

import random

from Classes import GameBase, Matching
from Definitions import ColorDefines, CustomerDefs
from Definitions import DefinedPaths as DL
from Handlers import WorkerHandler as WH


# TODO - Make actual state machine and stop using lamda members
# TODO - Examine this with Queueing
def SetFirstInLine(target) -> None:
    """Function for setting Queuing

        After Motion, the customer is set first if

    Args-
        target (_type_): _description_
    """
    if target.MvmHandler.IsFinished(target):
        target.DataObject.CurrentState = CustomerDefs.CustomerStates.FirstInLine


def WalkIn(target) -> None:
    """Initial Operations of a Customer

    Args-
        target (Sprite): Target Customer
    """
    target.MvmHandler.StartNewListedMotion(
        DL.DefinedPaths.CustomerToEntrance(sprite=target)
    )
    target.DataObject.CurrentState = CustomerDefs.CustomerStates.WalkingIn
    target.MvmHandler.OnComplete = lambda: (SetFirstInLine(target=target))


def FindAvailableWorker(customerSprite, activeGame=GameBase.MasterGame) -> tuple:
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
        if Matching.CostumeMatch(
            workerSprite=workerSprite, customerSprite=customerSprite
        ):
            return worker, workerSprite

    return None, None


# TODO - Stop the workers going on strike
# TODO - Stop 2 workers on 1 job
def AssignWorker(target) -> None:
    """Finds an availbale worker for a job and assigns them

        Starts the Worker Handler flow

    Args-
        target (CharImageSprite): Customer Sprite requesting Job
    """
    worker, workerSprite = FindAvailableWorker(customerSprite=target)
    if worker is not None and target.MvmHandler.InMotion is False:
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
            WH.FinishCustomer(
                workerSprite=workerSprite, job=target.DataObject.DesiredJob
            ),
        )
        workerSprite.MvmHandler.OnComplete = lambda: workerSprite.CreatePersonTimerBar(
            activeGame=GameBase.MasterGame,
            completeTask=returnHome,
            length=target.DataObject.DesiredJob.Length,
        )


def SitAtTable(target) -> None:
    """Logic for a Queuing Customer to sit down

    Args-
        target (CharImageSprite): Sprite of Target Customer
    """
    target.DataObject.CurrentState = CustomerDefs.CustomerStates.Seated
    path = DL.DefinedPaths.CustomerToRandomSeat(sprite=target)
    if path is not None:
        target.MvmHandler.StartNewListedMotion(path)
        target.MvmHandler.OnComplete = lambda: BeginWait(target=target)
    else:
        target.DataObject.CurrentState = CustomerDefs.CustomerStates.LeavingAngry
        GetUpAndGo(spriteImg=target)


def BeginWait(target) -> None:
    """Starts the timer for a customer waiting for service

    Args-
        target (CharImageSprite): Sprite of Target Customer
    """
    target.DataObject.CurrentState = CustomerDefs.CustomerStates.WaitingForService
    taskComplete = lambda: GetUpAndGo(spriteImg=target)
    target.CreatePersonTimerBar(
        activeGame=GameBase.MasterGame,
        completeTask=taskComplete,
        length=(target.DataObject.DesiredJob.Urgency.value * 30.0),
        assocId=target.DataObject.IdNum,
        startingState=target.DataObject.CurrentState.value,
        fillColor=ColorDefines.DarkRed,
    )


def AllWorkersBusy(target) -> None:
    """Routine for when all workers are busy

    Args-
        target (CharImageSprite): Sprite of Target Customer
    """
    taskComplete = lambda: GetUpAndGo(spriteImg=target)
    target.DataObject.CurrentState = CustomerDefs.CustomerStates.WaitingForService
    target.CreatePersonTimerBar(
        activeGame=GameBase.MasterGame, completeTask=taskComplete, length=10
    )


def GetUpAndGo(spriteImg, activeGame=GameBase.MasterGame) -> None:
    """Logic for a Customer to leave the restaurant

    Args-
        spriteImg (CharImageSprite): Sprite of Target Customer
        activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.
    """
    if (
        not spriteImg.DataObject.WorkerAssigned
        or spriteImg.DataObject.CurrentState is CustomerDefs.CustomerStates.Served
    ):
        spriteImg.MvmHandler.StartNewListedMotion(
            DL.DefinedPaths.CustomerToExit(sprite=spriteImg)
            if spriteImg.DataObject.CurrentState == CustomerDefs.CustomerStates.Queuing
            else DL.DefinedPaths.TableToExit(sprite=spriteImg)
        )

        spriteImg.MvmHandler.OnComplete = lambda: Matching.RemoveObjFromSprite(
            activeGame=activeGame, targetSprite=spriteImg
        )
