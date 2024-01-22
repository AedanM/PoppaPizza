from Classes import People, Game
from Utilities import Utils


def test_PeopleIdTest() -> None:
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
    for i in range(10):
        worker, workerSprite = People.Worker.CreateWorker()
        customer, customerSprite = People.Customer.CreateCustomer()
        if Utils.CheckInternet():
            assert worker.FirstName != customer.FirstName
            assert worker.LastName != customer.LastName
        Game.MasterGame.RemoveObjFromSprite(workerSprite)
        Game.MasterGame.RemoveObjFromSprite(customerSprite)
    assert Game.MasterGame.WorkerList == []
    assert Game.MasterGame.CustomerList == []


def RunAllPeopleTests() -> bool:
    Game.MasterGame = Game.Game(activateScreen=True)
    test_PeopleNames()
    test_PeopleIdTest()
    return True
