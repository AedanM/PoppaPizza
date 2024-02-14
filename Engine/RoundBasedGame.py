from typing import Any

import pygame

from Engine import Color, Utils


class RoundBasedGame:
    Rounds: int
    Screen = pygame.Surface
    BackgroundColor: Color.Color = Color.Color(hexstring="#000000")
    GameState: Any = 0
    ResultsList: list = []
    MaxRounds: int = 10
    CurrentRound: int = 1
    RoundResult: bool = False
    MasterSpriteGroup: pygame.sprite.Group = pygame.sprite.Group()

    DisplayedText: dict = {}

    def __init__(self, rounds, activeGame) -> None:
        self.Rounds = int(Utils.Bind(val=rounds, inRange=[0, self.MaxRounds]))
        self.Screen = activeGame.Screen

    def StartRound(self) -> None:
        self.DisplayedText["Round Text"].Text = (
            f"Round {self.CurrentRound}/{self.Rounds}"
        )
        self.MasterSpriteGroup.update()
        self.MasterSpriteGroup.draw(self.Screen)  # type: ignore

    def UpdateStateMachine(self, inputStr) -> None:
        pass

    def PlayGame(self) -> None:
        # Pylance rejects activeGame as param due to overloading
        self.StartRound()  # type: ignore
