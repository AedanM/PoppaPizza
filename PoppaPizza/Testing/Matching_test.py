from Classes import GameBase, People
from Handlers import Matching


def test_Matching() -> None:
    currentGame = GameBase.MainGame()
    for _ in range(15):
        worker, workerSprite = People.Worker.CreateWorker(activeGame=currentGame)
        customer, customerSprite = People.Customer.CreateCustomer(
            activeGame=currentGame
        )
        assert {
            "worker": worker,
            "sprite": workerSprite,
        } == Matching.MatchIdToPerson(
            activeGame=currentGame, inputId=workerSprite.CorrespondingID
        )
        assert worker == Matching.MatchIdToPerson(
            activeGame=currentGame,
            inputId=workerSprite.CorrespondingID,
            targetOutput="worker",
        )
        assert {
            "customer": customer,
            "sprite": customerSprite,
        } == Matching.MatchIdToPerson(
            activeGame=currentGame, inputId=customerSprite.CorrespondingID
        )
        assert customer == Matching.MatchIdToPerson(
            activeGame=currentGame,
            inputId=customerSprite.CorrespondingID,
            targetOutput="customer",
        )