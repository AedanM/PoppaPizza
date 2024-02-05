"""Purchase Handler"""

import pygame

from Classes import Game
from Definitions import CustomEvents, DefinedLocations, Prices, Restaurants


def BuyLockerRoom(position) -> None:
    price = Restaurants.UnlockLockerRoom(
        currentCash=Game.MasterGame.UserInventory.Money,
        position=position,
    )
    Game.MasterGame.UserInventory.PayMoney(amount=price)


def BuyTables(selectedRow) -> None:
    if selectedRow:
        price = Prices.DefaultPrices.Table * DefinedLocations.SeatingPlan.NumCols
        DefinedLocations.SeatingPlan.NumRows += 1
    else:
        price = Prices.DefaultPrices.Table * DefinedLocations.SeatingPlan.NumRows
        DefinedLocations.SeatingPlan.NumCols += 1

    Game.MasterGame.UserInventory.PayMoney(amount=price)
    pygame.event.post(CustomEvents.UpdateBackground)
