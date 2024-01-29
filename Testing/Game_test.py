"""Test Module for Game Functions"""
# pylint: disable=invalid-name
from Classes import Game, People


def test_ScreenSize() -> None:
    for _, size in Game.std_dimensions.items():
        currentGame = Game.Game(activateScreen=True, size=size)
        assert currentGame.ScreenSize == size


def test_Matching() -> None:
    currentGame = Game.Game()
    for _ in range(15):
        worker, workerSprite = People.Worker.CreateWorker(activeGame=currentGame)
        customer, customerSprite = People.Customer.CreateCustomer(
            activeGame=currentGame
        )
        assert {
            "worker": worker,
            "sprite": workerSprite,
        } == currentGame.MatchIdToPerson(inputId=workerSprite.CorrespondingID)
        assert worker == currentGame.MatchIdToPerson(
            inputId=workerSprite.CorrespondingID, targetOutput="worker"
        )
        assert {
            "customer": customer,
            "sprite": customerSprite,
        } == currentGame.MatchIdToPerson(inputId=customerSprite.CorrespondingID)
        assert customer == currentGame.MatchIdToPerson(
            inputId=customerSprite.CorrespondingID, targetOutput="customer"
        )
