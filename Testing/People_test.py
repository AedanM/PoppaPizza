"""Test Module for People Class"""

# pylint: disable=invalid-name

from Classes import GameBase, People
from Handlers import Matching


def test_PeopleIdTest() -> None:
    currentGame = GameBase.MainGame(activateScreen=True)
    worker1 = People.Worker.CreateWorker(activeGame=currentGame)[0]
    worker2 = People.Worker.CreateWorker(activeGame=currentGame)[0]
    customer1 = People.Customer.CreateCustomer(activeGame=currentGame)[0]
    customer2 = People.Customer.CreateCustomer(activeGame=currentGame)[0]
    assert worker1.IdNum != worker2.IdNum
    assert worker1.IdNum != customer1.IdNum
    assert worker1.IdNum != customer2.IdNum
    assert worker2.IdNum != customer1.IdNum
    assert worker2.IdNum != customer2.IdNum
    assert customer1.IdNum != customer2.IdNum


def test_PeopleNames() -> None:
    currentGame = GameBase.MainGame(activateScreen=True)
    currentGame.CustomerList = []
    currentGame.WorkerList = []
    for _ in range(100):
        worker, workerSprite = People.Worker.CreateWorker(activeGame=currentGame)
        customer, customerSprite = People.Customer.CreateCustomer(activeGame=currentGame)
        assert worker.FirstName != customer.FirstName
        assert worker.LastName != customer.LastName
