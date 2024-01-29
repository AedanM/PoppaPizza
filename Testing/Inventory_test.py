"""Test Module for Inventory Functions"""
# pylint: disable=invalid-name

from Classes import Inventory
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
    i = Inventory.Inventory(Money=5000)
    i.GetPaid(amount=2000.00)
    i.PayRent()
    assert i.Money == 7000 - Prices.CurrentRent
