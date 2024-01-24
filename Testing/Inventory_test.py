from Classes import Inventory
from Definitions import Prices


def test_Rent() -> None:
    i = Inventory.Inventory(Money=5000)
    i.GetPaid(amount=2000.00)
    i.PayRent()
    assert i.Money == 7000 - Prices.CurrentRent


def RunAllInventoryTests() -> bool:
    test_Rent()
    return True
