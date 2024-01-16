import Classes.Game as Game
import Classes.Sprite as Sprite
import Classes.TimerBar as TB
import Classes.DefinedLocations as DL


def FindAvailableWorker() -> bool:
    availWorkers = [x for x in Game.MasterGame.WorkerList if x.isAssigned == False]
    if len(availWorkers) < 1:
        worker, workerSprite = None, None
    else:
        worker = availWorkers[0]
        workerSprites = [
            x
            for x in Game.MasterGame.CharSpriteGroup
            if (
                x.imageType == Sprite.ImageTypes.Worker
                and x.correspondingID == worker.idNum
            )
        ]
        workerSprite = None if len(workerSprites) < 1 else workerSprites[0]
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
            workerSprite, worker, returnHome, customer.desiredJob.Length
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



def CustomerStateMachine(customer, spriteImg):
    match customer.State:
        case 1:
            pass