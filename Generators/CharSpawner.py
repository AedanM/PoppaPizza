"""Handler for Spawning Elements"""
import random
import numpy
from Classes import People, Game, DefinedLocations

# pylint: disable=C0103
LastSpawnTime = 0


def CustomerSpawner(force=False) -> None:
    # pylint: disable=global-statement
    global LastSpawnTime
    currentTime = Game.MasterGame.Clock.UnixTime
    chanceOfSpawn = Game.MasterGame.Chances.CustomerSpawn * float(
        currentTime - LastSpawnTime
    )
    if random.random() < chanceOfSpawn or force:
        spawnLocation = DefinedLocations.LocationDefs.CustomerSpawn
        customer, customerSprite = People.Customer.CreateCustomer(
            startLocation=spawnLocation
        )
        customerSprite.MvmHandler.StartNewListedMotion(
            DefinedLocations.DefinedPaths.CustomerToEntrance(sprite=customerSprite)
        )
        LastSpawnTime = currentTime


def WorkerSpawner(force=False) -> None:
    spawnLocation = numpy.subtract(
        DefinedLocations.LocationDefs.KitchenLocation, (50, 0)
    )
    People.Worker.CreateWorker(startLocation=spawnLocation)


def SpawnHandler() -> None:
    CustomerSpawner()
