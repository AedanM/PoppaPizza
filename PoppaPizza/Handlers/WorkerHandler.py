"""Handler for Worker Tasks"""

import random

from Definitions import AssetLibrary
from Definitions.DefinedLocations import LocationDefs
from Definitions.DefinedPaths import DefinedPaths
from Engine import Utils


def DailyReset(sprite) -> None:
    """Reset worker to Kitchen
        Unassigns the worker from any task as well
    Args-
        sprite (Sprite): Worker Sprite
    """
    sprite.MvmHandler.Reset()
    sprite.DataObject.IsAssigned = False
    spawnLocation = Utils.PositionRandomVariance(
        position=LocationDefs.WorkerSpawn,
        percentVariance=(0.05, 0.15),
        screenSize=LocationDefs.ScreenSize,
    )
    sprite.rect.center = spawnLocation


def ServeCustomer() -> None:
    """Logic for serving Customer"""
    pass


def FinishCustomer(workerSprite, job, activeGame) -> None:
    """Finish a customer and get paid

    Args-
        workerSprite (Sprite): Active Worker
        job (Job): Active Job
    """
    workerSprite.DataObject.IsAssigned = False
    workerSprite.DataObject.CurrentJobId = 0
    workerSprite.MvmHandler.StartNewListedMotion(DefinedPaths.BackToKitchen(sprite=workerSprite))
    activeGame.UserInventory.GetPaid(amount=job.Price)
    activeGame.UserInventory.Statistics.ServeCustomer()


def GetChanged(workerSprite, restaurant, activeGame) -> None:
    """Change the outfit of a worker

    Args-
        workerSprite (Sprite): Active Worker
        restaurant (Restaurant): Restaurant whos apparel to change into
    """
    workerSprite.MvmHandler.StartNewListedMotion(
        DefinedPaths.KitchenToLockerRoom(sprite=workerSprite, dest=restaurant.LockerRoom.Location)
    )
    newOutfit = AssetLibrary.PathLookup(random.choice(restaurant.WorkerImageTypes))
    workerSprite.MvmHandler.OnComplete = lambda: (
        workerSprite.ChangeOutfit(newOutfit),
        activeGame.UserInventory.Statistics.WorkerChanged(),
        workerSprite.CreatePersonTimerBar(
            completeTask=lambda: ReturnToKitchen(workerSprite=workerSprite),
            offset=(-30, 150),
            width=150,
        ),
    )


def ReturnToKitchen(workerSprite) -> None:
    """Go back to Kitchen

    Args-
        workerSprite (Sprite): Active Worker
    """
    workerSprite.MvmHandler.StartNewListedMotion(DefinedPaths.BackToKitchen(sprite=workerSprite))


def EnterWork(workerSprite) -> None:
    workerSprite.MvmHandler.StartNewListedMotion(DefinedPaths.BackToKitchen(sprite=workerSprite))
