"""Handler for Spawning Chars"""

import random

from Classes import People
from Definitions import AssetLibrary, Prices, Restaurants
from Definitions.DefinedLocations import LocationDefs
from Handlers import CustomerHandler, WorkerHandler

# pylint: disable=C0103
LastSpawnTime = 0


def SpawnLocationFree(activeGame, spawnPoint=LocationDefs.EndOfLine) -> bool:
    """Determines if spawn location has another sprite on it

    Args-
        spawnPoint (tuple, optional): Spawn location as a tuple. Defaults to DefinedLocations.LocationDefs.EndOfLine.

    Returns-
        bool: Free status of Spawn Location
    """
    for sprite in activeGame.CharSpriteGroup:
        if sprite.rect.collidepoint(spawnPoint[0], spawnPoint[1]):
            return False
    return True


def CustomerSpawner(activeGame, force=False) -> None:
    """Randomly Spawns Customers

    Args-
        force (bool, optional): Force a spawn on this run. Defaults to False.
    """
    global LastSpawnTime
    currentTime = activeGame.GameClock.UnixTime
    chanceOfSpawn = activeGame.Chances.CustomerSpawn * float(currentTime - LastSpawnTime) * 0.0005
    if (random.random() < chanceOfSpawn or force) and SpawnLocationFree(activeGame=activeGame):
        spawnLocation = LocationDefs.CustomerSpawn
        customerType = GetRandomCustomerType(activeGame=activeGame)
        _, customerSprite = People.Customer.CreateCustomer(
            startLocation=spawnLocation, imageType=customerType, activeGame=activeGame
        )
        CustomerHandler.WalkIn(target=customerSprite)
        LastSpawnTime = currentTime
        activeGame.UserInventory.Statistics.CustomersEntered += 1


def GetRandomCustomerType(activeGame) -> AssetLibrary.ImageTypes:
    """Randomly Select a Customer Type for Spawn

        Weighting is based on the ActiveRestLuck number in the Chances object
        The random list is developed with an ActiveRestLuck number of active customers
        and 1 inactive customer. This is to not punish the player too severely

    Returns-
        AssetLibrary.ImageTypes: Image Type of Customer
    """
    activeClientTypes = [
        x.CustomerImageTypes
        for x in Restaurants.RestaurantList
        if x.LockerRoom.Unlocked and x.CustomerImageTypes
    ]
    inactiveClientTypes = [
        x.CustomerImageTypes
        for x in Restaurants.RestaurantList
        if not x.LockerRoom.Unlocked and x.CustomerImageTypes
    ]
    customerType = random.choice(
        random.choice(
            random.choice(
                [activeClientTypes] * activeGame.Chances.ActiveRestLuck
                + [inactiveClientTypes]  # type:ignore
            )
        )
    )

    return customerType


def BuyWorker(activeGame, free=False) -> None:
    """Buy Worker and Spawn Them In

    Args-
        free (bool, optional): Forces a free purchase. Defaults to False.
    """
    if activeGame.UserInventory.Money > Prices.CurrentWorkerPrice:
        spawnLocation = LocationDefs.WorkerSpawn
        _, workerSprite = People.Worker.CreateWorker(
            startLocation=spawnLocation, activeGame=activeGame
        )
        if not free:
            activeGame.UserInventory.Money -= Prices.CurrentWorkerPrice
            Prices.CurrentWorkerPrice = round(
                Prices.CurrentWorkerPrice * random.uniform(1.0, 2.5), 2
            )
        WorkerHandler.EnterWork(workerSprite=workerSprite)
