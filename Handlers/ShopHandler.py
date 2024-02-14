"""Purchase Handler"""

import pygame

from Classes import GameBase
from Definitions import CustomEvents, DefinedLocations, Prices, Restaurants
from Generators import CharSpawner


def BuyLockerRoom(position) -> None:
    """Unlocks and Pays for a Locker Room

    Args-
        position (tuple): Position Tuple
    """
    price = Restaurants.UnlockLockerRoom(
        currentCash=GameBase.MasterGame.UserInventory.Money,
        position=position,
    )
    GameBase.MasterGame.UserInventory.PayMoney(amount=price)


def BuyTables(selectedRow) -> None:
    """Buys a new row or column of tables

    Args-
        selectedRow (bool): is Row selected? else Col is seleceted
    """
    if selectedRow:
        price = Prices.DefaultPrices.Table * DefinedLocations.SeatingPlan.NumCols
        DefinedLocations.SeatingPlan.NumRows += 1
    else:
        price = Prices.DefaultPrices.Table * DefinedLocations.SeatingPlan.NumRows
        DefinedLocations.SeatingPlan.NumCols += 1
    DefinedLocations.TablePlaces = []
    GameBase.MasterGame.UserInventory.PayMoney(amount=price)
    pygame.event.post(CustomEvents.UpdateBackground)


def BuyNumWorkers(num) -> None:
    """Buys a number of workers

    Args-
        num (int): Number of Workers
    """
    for _ in range(num):
        CharSpawner.BuyWorker()


def PayUpkeep() -> None:
    """Pay Daily Rent Amount and Wages"""
    workerPay = 0.0
    for worker in GameBase.MasterGame.WorkerList:
        workerPay += worker.BasePay * Prices.DefaultPrices.Salary
    rent = Prices.CurrentRent
    GameBase.MasterGame.UserInventory.PayMoney(amount=workerPay + rent, update=True)
