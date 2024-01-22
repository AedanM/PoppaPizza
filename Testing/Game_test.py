from Classes import Game, People


def test_ScreenSize() -> None:
    for key, size in Game.std_dimensions.items():
        currentGame = Game.Game(activateScreen=True, size=size)
        assert currentGame.ScreenSize == size


def test_Matching() -> None:
    currentGame = Game.Game()
    for i in range(200):
        worker, workerSprite = People.Worker.CreateWorker(activeGame=currentGame)
        customer, customerSprite = People.Customer.CreateCustomer(
            activeGame=currentGame
        )
        assert {
            "worker": worker,
            "sprite": workerSprite,
        } == currentGame.MatchSpriteToPerson(inputId=workerSprite.CorrespondingID)
        assert {
            "customer": customer,
            "sprite": customerSprite,
        } == currentGame.MatchSpriteToPerson(inputId=customerSprite.CorrespondingID)
