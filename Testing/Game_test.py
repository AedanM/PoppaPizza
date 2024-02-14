"""Test Module for Game Functions"""

# pylint: disable=invalid-name
import Definitions.DefinedLocations
from Classes import GameBase, Matching, People


def test_ScreenSize() -> None:
    for _, size in Definitions.DefinedLocations.StandardDimensions.items():
        currentGame = GameBase.MainGame(activateScreen=True, size=size)
        assert currentGame.ScreenSize == size


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
