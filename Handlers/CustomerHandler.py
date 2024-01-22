"""Handler for Customer Tasks"""
import random
from Classes import Game, TimerBar as TB, DefinedLocations as DL
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
def AssignWorker(target, activeGame=Game.MasterGame) -> None:
    customer = [
        x for x in activeGame.CustomerList if (x.IdNum == target.CorrespondingID)
    ][0]
    worker, workerSprite = FindAvailableWorker()
    if customer.WorkerAssigned is False and worker is None:
        AllWorkersBusy(target=target)
    elif worker is not None:
        customer.WorkerAssigned = True
        customer.DesiredJob.Assign(worker)
        workerSprite.MvmHandler.StartNewListedMotion(
            pointList=DL.DefinedPaths.KitchenToCustomer(
                sprite=workerSprite, dest=target
            )
        )
        returnHome = lambda: (
            GetUpAndGo(spriteImg=target),
            WH.FinishCustomer(w=worker, ws=workerSprite),
        )
        workerSprite.MvmHandler.OnComplete = lambda: TB.CreatePersonTimerBar(
            sprite=workerSprite,
            completeTask=returnHome,
            length=customer.DesiredJob.Length,
        )


def AllWorkersBusy(target) -> None:
    taskComplete = lambda: GetUpAndGo(spriteImg=target)
    TB.CreatePersonTimerBar(sprite=target, completeTask=taskComplete, length=10)


def GetUpAndGo(spriteImg, activeGame=Game.MasterGame) -> None:
    spriteImg.MvmHandler.StartNewListedMotion(
        DL.DefinedPaths.CustomerToExit(sprite=spriteImg)
    )

    spriteImg.MvmHandler.OnComplete = lambda: activeGame.RemoveObjFromSprite(spriteImg)
    customer = activeGame.MatchSpriteToPerson(spriteImg.CorrespondingID)["customer"]
    Game.MasterGame.UserInventory.GetPaid(customer.DesiredJob.Price)
