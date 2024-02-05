"""Handler for Spawning Chars"""

import random

import numpy

from Classes import Game, People
from Definitions import AssetLibrary, DefinedLocations, Prices
from Handlers import CustomerHandler
from Utilities import Utils

# pylint: disable=C0103
LastSpawnTime = 0


def CustomerSpawner(force=False) -> None:
    global LastSpawnTime
    currentTime = Game.MasterGame.GameClock.UnixTime
    chanceOfSpawn = Game.MasterGame.Chances.CustomerSpawn * float(
        currentTime - LastSpawnTime
    )
    if random.random() < chanceOfSpawn or force:
        spawnLocation = DefinedLocations.LocationDefs.CustomerSpawn
        customerType = random.choice(AssetLibrary.CustomerOutfits)
        _, customerSprite = People.Customer.CreateCustomer(
            startLocation=spawnLocation, imageType=customerType
        )
        CustomerHandler.WalkIn(target=customerSprite)
        LastSpawnTime = currentTime
        Game.MasterGame.UserInventory.Statistics.CustomersEntered += 1


def BuyWorker(free=False) -> None:
    if Game.MasterGame.UserInventory.Money > Prices.CurrentWorkerPrice:
        spawnLocation = numpy.subtract(
            DefinedLocations.LocationDefs.KitchenLocation,
            Utils.ScaleToSize(
                value=(250, -50), newSize=DefinedLocations.LocationDefs.ScreenSize
            ),
        )
        People.Worker.CreateWorker(startLocation=spawnLocation)
        if not free:
            Game.MasterGame.UserInventory.Money -= Prices.CurrentWorkerPrice
            Prices.CurrentWorkerPrice = round(
                Prices.CurrentWorkerPrice * random.uniform(1.0, 2.5), 2
            )


def SpawnHandler() -> None:
    CustomerSpawner()
