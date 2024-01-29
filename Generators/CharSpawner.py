"""Handler for Spawning Chars"""
import random
import numpy
from Classes import People, Game
from Definitions import DefinedLocations, Prices
from Handlers import CustomerHandler as CH

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
        _, customerSprite = People.Customer.CreateCustomer(startLocation=spawnLocation)
        CH.WalkIn(customerSprite)
        LastSpawnTime = currentTime


def BuyWorker(free=False) -> None:
    if Game.MasterGame.UserInventory.Money > Prices.CurrentWorkerPrice:
        spawnLocation = numpy.subtract(
            DefinedLocations.LocationDefs.KitchenLocation, (250, -50)
        )
        People.Worker.CreateWorker(startLocation=spawnLocation)
        if not free:
            Game.MasterGame.UserInventory.Money -= Prices.CurrentWorkerPrice
            Prices.CurrentWorkerPrice = round(
                Prices.CurrentWorkerPrice * random.uniform(1.0, 2.5), 2
            )


def SpawnHandler() -> None:
    CustomerSpawner()
