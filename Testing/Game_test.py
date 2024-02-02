"""Test Module for Game Functions"""

# pylint: disable=invalid-name
from Classes import Game, Matching, People


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
