"""Test Module for Inventory Functions"""

# pylint: disable=invalid-name

from Classes import Game, Inventory
from Definitions import Prices


def test_GetPaid() -> None:
    i = Inventory.Inventory(Money=100)
    i.GetPaid(amount=2000)
    assert i.Money == 2100
    i.GetPaid(amount=1.0)
    assert i.Money == 2101
    i.GetPaid(amount=-2000)
    assert i.Money == 101
    i.GetPaid(amount=-200)
    assert i.Money == -99


def test_Rent() -> None:
    currentGame = Game.MasterGame
    i = currentGame.UserInventory
    i.GetPaid(amount=2000.00)
    i.PayMoney(amount=Prices.CurrentRent)
    assert i.Money == 4000 - Prices.CurrentRent
