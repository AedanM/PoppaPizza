"""Test Module for People Class"""

# pylint: disable=invalid-name

from Classes import Game, Matching, People


def test_PeopleIdTest() -> None:
    Game.MasterGame = Game.Game(activateScreen=True)
    worker1 = People.Worker.CreateWorker()[0]
    worker2 = People.Worker.CreateWorker()[0]
    customer1 = People.Customer.CreateCustomer()[0]
    customer2 = People.Customer.CreateCustomer()[0]
    assert worker1.IdNum != worker2.IdNum
    assert worker1.IdNum != customer1.IdNum
    assert worker1.IdNum != customer2.IdNum
    assert worker2.IdNum != customer1.IdNum
    assert worker2.IdNum != customer2.IdNum
    assert customer1.IdNum != customer2.IdNum


def test_PeopleNames() -> None:
    currentGame = Game.Game(activateScreen=True)
    currentGame.CustomerList = []
    currentGame.WorkerList = []
    for _ in range(10):
        worker, workerSprite = People.Worker.CreateWorker(activeGame=currentGame)
        customer, customerSprite = People.Customer.CreateCustomer(
            activeGame=currentGame
        )
        assert worker.FirstName != customer.FirstName
        assert worker.LastName != customer.LastName
        Matching.RemoveObjFromSprite(activeGame=currentGame, targetSprite=workerSprite)
        Matching.RemoveObjFromSprite(
            activeGame=currentGame, targetSprite=customerSprite
        )
    assert not currentGame.WorkerList
    assert not currentGame.CustomerList
