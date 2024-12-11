"""Test Module for Inventory Functions"""

# pylint: disable=invalid-name

from Classes import GameBase, Inventory
from Definitions import Prices


def test_GetPaid() -> None:
    i = Inventory.Inventory()
    i.Money = 0
    i.GetPaid(amount=2000)
    assert i.Money == 2000
    i.GetPaid(amount=1.0)
    assert i.Money == 2001
    i.GetPaid(amount=-2000)
    assert i.Money == 2001
    i.GetPaid(amount=0)
    assert i.Money == 2001


def test_Rent() -> None:
    currentGame = GameBase.MainGame()
    i = currentGame.UserInventory
    i.GetPaid(amount=2000.00)
    i.PayMoney(amount=Prices.CurrentRent)
    assert i.Money == 4000 - Prices.CurrentRent
