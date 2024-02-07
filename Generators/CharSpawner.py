"""Handler for Spawning Chars"""

import random

from Classes import Game, People
from Definitions import AssetLibrary, DefinedLocations, Prices, Restaurants
from Handlers import CustomerHandler
from Utilities import Utils

# pylint: disable=C0103
LastSpawnTime = 0


def SpawnLocationFree(spawnPoint=DefinedLocations.LocationDefs.EndOfLine) -> bool:
    """Determines if spawn location has another sprite on it

    Args:
        spawnPoint (tuple, optional): Spawn location as a tuple. Defaults to DefinedLocations.LocationDefs.EndOfLine.

    Returns:
        bool: Free status of Spawn Location
    """
    for sprite in Game.MasterGame.CharSpriteGroup:
        if sprite.rect.collidepoint(spawnPoint[0], spawnPoint[1]):
            return False
    return True


def CustomerSpawner(force=False) -> None:
    """Randomly Spawns Customers

    Args:
        force (bool, optional): Force a spawn on this run. Defaults to False.
    """
    global LastSpawnTime
    currentTime = Game.MasterGame.GameClock.UnixTime
    chanceOfSpawn = Game.MasterGame.Chances.CustomerSpawn * float(
        currentTime - LastSpawnTime
    )
    if (random.random() < chanceOfSpawn or force) and SpawnLocationFree():
        spawnLocation = DefinedLocations.LocationDefs.CustomerSpawn
        customerType = GetRandomCustomerType()
        _, customerSprite = People.Customer.CreateCustomer(
            startLocation=spawnLocation, imageType=customerType
        )
        CustomerHandler.WalkIn(target=customerSprite)
        LastSpawnTime = currentTime
        Game.MasterGame.UserInventory.Statistics.CustomersEntered += 1


def GetRandomCustomerType() -> AssetLibrary.ImageTypes:
    """Randomly Select a Customer Type for Spawn

        Weighting is based on the ActiveRestLuck number in the Chances object
        The random list is developed with an ActiveRestLuck number of active customers
        and 1 inactive customer. This is to not punish the player too severely

    Returns:
        AssetLibrary.ImageTypes: Image Type of Customer
    """
    activeClientTypes = [
        x.CustomerImageTypes
        for x in Restaurants.RestaurantList
        if x.LockerRoom.Unlocked
    ]
    inactiveClientTypes = [
        x.CustomerImageTypes
        for x in Restaurants.RestaurantList
        if not x.LockerRoom.Unlocked
    ]
    customerType = random.choice(
        random.choice(
            random.choice(
                [activeClientTypes] * Game.MasterGame.Chances.ActiveRestLuck
                + [inactiveClientTypes]
            )
        )
    )

    return customerType


def BuyWorker(free=False) -> None:
    """Buy Worker and Spawn Them In

    Args:
        free (bool, optional): Forces a free purchase. Defaults to False.
    """
    if Game.MasterGame.UserInventory.Money > Prices.CurrentWorkerPrice:
        spawnLocation = Utils.PositionRandomVariance(
            position=DefinedLocations.LocationDefs.WorkerSpawn,
            percentVarianceTuple=(0.05, 0.15),
            screenSize=DefinedLocations.LocationDefs.ScreenSize,
        )
        People.Worker.CreateWorker(startLocation=spawnLocation)
        if not free:
            Game.MasterGame.UserInventory.Money -= Prices.CurrentWorkerPrice
            Prices.CurrentWorkerPrice = round(
                Prices.CurrentWorkerPrice * random.uniform(1.0, 2.5), 2
            )
