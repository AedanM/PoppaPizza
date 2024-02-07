"""Prices Definitions"""


class DefaultPrices:
    """Default Prices for things in Shop"""

    Rent: int = 100.00
    NewWorker: float = 500.00
    Salary: float = 8.00
    Table: float = 250.00


# pylint: disable=invalid-name
CurrentRent = DefaultPrices.Rent
CurrentWorkerPrice = DefaultPrices.NewWorker
