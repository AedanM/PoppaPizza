"""Class for DefinedLocations"""
import pygame
from Classes import Game


class DefinedLocations:
    @property
    def YellowLockerRoom(self) -> tuple:
        return (350, 65)

    @property
    def GreenLockerRoom(self) -> tuple:
        return (530, 65)

    @property
    def BlueLockerRoom(self) -> tuple:
        return (710, 65)

    @property
    def PinkLockerRoom(self) -> tuple:
        return (890, 65)

    @property
    def GreyLockerRoom(self) -> tuple:
        return (1070, 65)

    @property
    def KitchenLocation(self) -> tuple:
        return (200, 225)

    @property
    def CustomerExit(self) -> tuple:
        return (1200, 1000)

    @property
    def CustomerEntrance(self) -> tuple:
        return (1150, 325)

    @property
    def CustomerSpawn(self) -> tuple:
        return (1150, 1000)


LocationDefs = DefinedLocations()


class SeatingPlan:
    TableRows = [350, 500, 650, 800, 950]
    TableCols = [300, 400, 500, 600, 700]


""" def DebugLocations(activateGame=Game.MasterGame) -> None:
    attrs = [x for x in dir(LocationDefs) if "__" not in x]
    for attr in attrs:
        pygame.draw.circle(
            surface=activateGame.Screen,
            color=(0, 200, 255),
            center=getattr(LocationDefs, attr),
            radius=25,
        )
 """
