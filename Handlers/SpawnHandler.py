import pygame
import random
import Classes.Game as Game
import Classes.People as People
lastSpawnTime = 0

def CustomerSpawner():
    global lastSpawnTime
    currentTime = Game.MasterGame.Clock.unixTime
    chanceOfSpawn = Game.MasterGame.Chances.customerSpawn * float(currentTime-lastSpawnTime)
    if(random.random() < chanceOfSpawn):
        People.Customer.CreateCustomer()
        lastSpawnTime = currentTime


def SpawnHandler():
    CustomerSpawner()