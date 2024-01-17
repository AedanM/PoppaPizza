"""Handler for Customer Tasks"""
import Classes.Game as Game
import Classes.Sprite as Sprite
import Classes.TimerBar as TB
import Classes.DefinedLocations as DL


def FindAvailableWorker() -> bool:
    availWorkers = [x for x in Game.MasterGame.WorkerList if x.IsAssigned is False]
    if len(availWorkers) < 1:
        worker, workerSprite = None, None
    else:
        worker = availWorkers[0]
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
        returnHome = lambda: FinishCustomer(target, workerSprite)
        workerSprite.MvmHandler.OnComplete = lambda: TB.CreatePersonTimerBar(
            workerSprite, returnHome, customer.DesiredJob.Length
        )


def FinishCustomer(custSprite, workerSprite):
    workerSprite.MvmHandler.StartNewListedMotion(
        DL.DefinedPaths.BackToKitchen(workerSprite)
    )
    GetUpAndGo(custSprite)


def AllWorkersBusy(target):
    taskComplete = lambda: GetUpAndGo(target)
    TB.CreatePersonTimerBar(target, taskComplete, 10)


def GetUpAndGo(spriteImg):
    spriteImg.MvmHandler.StartNewListedMotion(DL.DefinedPaths.CustomerToExit(spriteImg))
    spriteImg.MvmHandler.OnComplete = lambda: Game.MasterGame.RemoveObj(spriteImg)
