"""Prices Definitions"""
class DefaultPrices:
    Rent: int = 100.00
    NewWorker: float = 500.00
    Salary: float = 80.00
    Table: float = 250.00

# pylint: disable=invalid-name
CurrentRent = DefaultPrices.Rent
CurrentWorkerPrice = DefaultPrices.NewWorker
