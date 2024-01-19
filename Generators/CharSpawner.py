"""Handler for Spawning Elements"""
import random
from Classes import People, Game

# pylint: disable=C0103
LastSpawnTime = 0


def CustomerSpawner() -> None:
    # pylint: disable=global-statement
    global LastSpawnTime
    currentTime = Game.MasterGame.Clock.UnixTime
    chanceOfSpawn = Game.MasterGame.Chances.CustomerSpawn * float(
        currentTime - LastSpawnTime
    )
    if random.random() < chanceOfSpawn:
        People.Customer.CreateCustomer()
        LastSpawnTime = currentTime


def SpawnHandler() -> None:
    CustomerSpawner()
