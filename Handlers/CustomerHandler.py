import Classes.Game as Game
import Classes.Sprite as Sprite


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
    if worker is not None:
        customer.desiredJob.Assign(worker)
        workerSprite.MvmHandler.startNewMotion((target.rect.x, target.rect.y))
    else:
        AllCustomersBusy()


def AllCustomersBusy():
    pass
