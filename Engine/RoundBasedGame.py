import pygame

from Engine import Color, Utils


class RoundBasedGame:
    Rounds: int
    Screen = pygame.Surface
    BackgroundColor: Color.Color = Color.Color(hexstring="#000000")
    GameState: any = 0
    ResultsList: list = []
    MaxRounds: int = 10
    CurrentRound: int = 1
    OnRoundWin: callable = lambda self: None
    OnRoundLoss: callable = lambda self: None
    RoundResult: bool = False
    MasterSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()

    DisplayedText: dict = {}

    def __init__(self, rounds, activeGame) -> None:
        self.Rounds = Utils.Bind(val=rounds, inRange=[0, self.MaxRounds])
        self.Screen = activeGame.Screen

    def StartRound(self) -> None:
        self.DisplayedText[
            "Round Text"
        ].Text = f"Round {self.CurrentRound}/{self.Rounds}"
        self.MasterSpriteGroup.update()
        self.MasterSpriteGroup.draw(self.Screen)

    def UpdateStateMachine(self, input) -> None:
        pass

    def PlayGame(self, activeGame) -> None:
        self.StartRound(activeGame=activeGame)
