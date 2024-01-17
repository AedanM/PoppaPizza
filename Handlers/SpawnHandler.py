"""Handler for Spawning Elements"""
import random
import pygame
import Classes.Game as Game
import Classes.People as People

LastSpawnTime = 0


def CustomerSpawner():
    global LastSpawnTime
    currentTime = Game.MasterGame.Clock.UnixTime
    chanceOfSpawn = Game.MasterGame.Chances.CustomerSpawn * float(
        currentTime - LastSpawnTime
    )
    if random.random() < chanceOfSpawn:
        People.Customer.CreateCustomer()
        LastSpawnTime = currentTime


def SpawnHandler():
    CustomerSpawner()
