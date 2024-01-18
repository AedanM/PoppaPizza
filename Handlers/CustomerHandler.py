"""Handler for Customer Tasks"""
import random
from Classes import Game, Sprite, People, TimerBar as TB, DefinedLocations as DL
from Handlers import WorkerHandler as WH


def FindAvailableWorker() -> tuple[People.Worker, Sprite.CharImageSprite]:
    availWorkers = [x for x in Game.MasterGame.WorkerList if x.IsAssigned is False]
    if len(availWorkers) < 1:
        worker, workerSprite = None, None
    else:
        worker = random.choice(availWorkers)
        workerSprites = [
            x
            for x in Game.MasterGame.CharSpriteGroup
            if (
                x.ImageType == Sprite.ImageTypes.Worker
                and x.CorrespondingID == worker.IdNum
            )
        ]
        workerSprite = None if len(workerSprites) < 1 else workerSprites[0]
    return worker, workerSprite


def AssignWorker(target):
    customer = [
        x for x in Game.MasterGame.CustomerList if (x.IdNum == target.CorrespondingID)
    ][0]
    worker, workerSprite = FindAvailableWorker()
    if customer.WorkerAssigned is False and worker is None:
        AllWorkersBusy(target)
    elif worker is not None:
        customer.WorkerAssigned = True
        customer.DesiredJob.Assign(worker)
        workerSprite.MvmHandler.StartNewListedMotion(
            DL.DefinedPaths.KitchenToCustomer(workerSprite, target)
        )
        returnHome = lambda: (
            GetUpAndGo(target),
            WH.FinishCustomer(worker, workerSprite),
        )
        workerSprite.MvmHandler.OnComplete = lambda: TB.CreatePersonTimerBar(
            workerSprite, returnHome, customer.DesiredJob.Length
        )


def AllWorkersBusy(target):
    taskComplete = lambda: GetUpAndGo(target)
    TB.CreatePersonTimerBar(target, taskComplete, 10)


def GetUpAndGo(spriteImg):
    spriteImg.MvmHandler.StartNewListedMotion(DL.DefinedPaths.CustomerToExit(spriteImg))
    spriteImg.MvmHandler.OnComplete = lambda: Game.MasterGame.RemoveObj(spriteImg)
