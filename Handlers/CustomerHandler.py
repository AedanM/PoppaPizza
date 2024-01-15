import Classes.Game as Game
import Classes.Sprite as Sprite
import Classes.TimerBar as TB
import Classes.DefinedLocations as DL


def FindAvailableWorker() -> bool:
    try:
        worker = Game.MasterGame.WorkerList[0]
        while worker.isAssigned and worker is not None:
            worker = next(Game.MasterGame.WorkerList, None)
    except:
        worker = None
    try:
        workerSprite = [
            x
            for x in Game.MasterGame.CharSpriteGroup
            if (
                x.imageType == Sprite.ImageTypes.Worker
                and x.correspondingID == worker.idNum
            )
        ][0]
    except:
        workerSprite = None
    return worker, workerSprite


def AssignWorker(target):
    customer = [
        x for x in Game.MasterGame.CustomerList if (x.idNum == target.correspondingID)
    ][0]
    worker, workerSprite = FindAvailableWorker()
    if customer.workerAssigned == False and worker is None:
        AllWorkersBusy(customer, target)
    elif worker is not None:
        customer.workerAssigned = True
        customer.desiredJob.Assign(worker)
        workerSprite.MvmHandler.startNewListedMotion(
            DL.DefinedPaths.KitchenToCustomer(workerSprite, target)
        )
        returnHome = lambda: FinishCustomer(customer, target, worker, workerSprite)
        workerSprite.MvmHandler.OnComplete = lambda: TB.CreatePersonTimerBar(
            workerSprite, worker, returnHome, 5
        )

def FinishCustomer(customer, custSprite, worker, workerSprite):
    workerSprite.MvmHandler.startNewListedMotion(
            DL.DefinedPaths.BackToKitchen(workerSprite)
    )
    GetUpAndGo(customer, custSprite)

def AllWorkersBusy(customer, target):
    taskComplete = lambda: GetUpAndGo(customer, target)
    TB.CreatePersonTimerBar(target, customer, taskComplete, 10)


def GetUpAndGo(customer, spriteImg):
    spriteImg.MvmHandler.startNewListedMotion(DL.DefinedPaths.CustomerToExit(spriteImg))
    spriteImg.MvmHandler.OnComplete = lambda: Game.MasterGame.RemoveObj(spriteImg)
