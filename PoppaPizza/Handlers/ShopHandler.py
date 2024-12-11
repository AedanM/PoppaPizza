"""Purchase Handler"""

import pygame

from Definitions import CustomEvents, Prices, Restaurants
from Definitions.DefinedLocations import SeatingPlan
from Generators import CharSpawner


def BuyLockerRoom(position, activeGame) -> None:
    """Unlocks and Pays for a Locker Room

    Args-
        position (tuple): Position Tuple
    """
    price = Restaurants.UnlockLockerRoom(
        currentCash=activeGame.UserInventory.Money,
        position=position,
    )
    activeGame.UserInventory.PayMoney(amount=price)


def BuyTables(selectedRow, activeGame) -> None:
    """Buys a new row or column of tables

    Args-
        selectedRow (bool): is Row selected? else Col is seleceted
    """
    if selectedRow:
        price = Prices.DefaultPrices.Table * SeatingPlan.NumCols
        SeatingPlan.NumRows += 1
    else:
        price = Prices.DefaultPrices.Table * SeatingPlan.NumRows
        SeatingPlan.NumCols += 1
    activeGame.UserInventory.PayMoney(amount=price)
    pygame.event.post(CustomEvents.UpdateBackground)


def BuyNumWorkers(num, activeGame) -> None:
    """Buys a number of workers

    Args-
        num (int): Number of Workers
    """
    for _ in range(num):
        CharSpawner.BuyWorker(activeGame=activeGame)


def PayUpkeep(activeGame) -> None:
    """Pay Daily Rent Amount and Wages"""
    workerPay = 0.0
    for worker in activeGame.WorkerList:
        workerPay += worker.BasePay * Prices.DefaultPrices.Salary
    rent = Prices.CurrentRent
    activeGame.UserInventory.PayMoney(amount=workerPay + rent, update=True)
