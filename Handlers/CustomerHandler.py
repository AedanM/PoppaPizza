"""Handler for Customer Tasks"""
import random
from Classes import Game, People, TimerBar as TB, DefinedLocations as DL
from Handlers import WorkerHandler as WH


# TODO - Fix getting worker who is busy
def FindAvailableWorker(activeGame=Game.MasterGame) -> tuple:
    availWorkers = [x for x in activeGame.WorkerList if x.IsAssigned is False]
    if len(availWorkers) < 1:
        worker, workerSprite = None, None
    else:
        worker = random.choice(availWorkers)
        workerSprites = [
            x
            for x in activeGame.CharSpriteGroup
            if (
                x.ImageType == activeGame.ImageTypes.Worker
                and x.CorrespondingID == worker.IdNum
            )
        ]
        workerSprite = None if len(workerSprites) < 1 else workerSprites[0]
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
        workerSprite.MvmHandler.OnComplete = lambda: TB.CreatePersonTimerBar(
            sprite=workerSprite,
            completeTask=returnHome,
            length=targetObj.DesiredJob.Length,
        )


def SitAtTable(target, customer) -> None:
    target.MvmHandler.StartNewListedMotion(
        DL.DefinedPaths.CustomerToRandomSeat(sprite=target)
    )
    customer.CurrentState = People.CustomerStates.Seated
    target.MvmHandler.OnComplete = lambda: BeginWait(target=target, customer=customer)


def BeginWait(target, customer) -> None:
    customer.CurrentState = People.CustomerStates.WaitingForService
    taskComplete = lambda: GetUpAndGo(spriteImg=target)
    TB.CreatePersonTimerBar(
        sprite=target,
        completeTask=taskComplete,
        length=(customer.DesiredJob.Urgency.value * 30.0),
    )


def AllWorkersBusy(target) -> None:
    customer = Game.MasterGame.MatchSpriteToPerson(
        inputId=target.CorrespondingID, targetOutput="customer"
    )
    taskComplete = lambda: GetUpAndGo(spriteImg=target)
    customer.CurrentState = People.CustomerStates.Waiting
    TB.CreatePersonTimerBar(sprite=target, completeTask=taskComplete, length=10)


def GetUpAndGo(spriteImg, activeGame=Game.MasterGame) -> None:
    customer = activeGame.MatchSpriteToPerson(
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
