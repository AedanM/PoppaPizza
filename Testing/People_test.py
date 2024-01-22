from Classes import People, Game
from Utilities import Utils


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
    Game.MasterGame = Game.Game(activateScreen=True)
    for i in range(10):
        worker, workerSprite = People.Worker.CreateWorker()
        customer, customerSprite = People.Customer.CreateCustomer()
        if Utils.CheckInternet():
            assert worker.FirstName != customer.FirstName
            assert worker.LastName != customer.LastName
        Game.MasterGame.RemoveObjFromSprite(targetSprite=workerSprite)
        Game.MasterGame.RemoveObjFromSprite(targetSprite=customerSprite)
    assert Game.MasterGame.WorkerList == []
    assert Game.MasterGame.CustomerList == []


def RunAllPeopleTests() -> bool:
    Game.MasterGame = None
    test_PeopleNames()
    Game.MasterGame = None
    test_PeopleIdTest()
    return True
