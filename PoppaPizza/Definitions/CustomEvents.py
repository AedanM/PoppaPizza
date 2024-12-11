"""Defined Custom Events"""

import pygame

from Classes import Stats
from Generators import BackgroundPopulator, Menus
from Handlers import Matching, ShopHandler

NightCycle = pygame.event.Event(pygame.USEREVENT, attr1="NightCycle")
GameOver = pygame.event.Event(pygame.USEREVENT, attr1="GameOver")
UpdateBackground = pygame.event.Event(pygame.USEREVENT, attr1="UpdateBackground")


def DayNightEvent(activeGame) -> None:
    """Logic behind a day transition

    Pays Rent
    Loads DayTransition Menu
    Resets Sprites
    Updates Stats
    Resets Background

    """
    ShopHandler.PayUpkeep(activeGame=activeGame)
    (
        GameOverEvent(activeGame=activeGame)
        if activeGame.HasGameOver
        else Menus.DayTransistion(activeGame=activeGame)
    )
    Matching.ResetSprites(activeGame=activeGame)
    Stats.UpdateStats(activeGame=activeGame)
    UpdateBackgroundEvent(activeGame=activeGame)


def GameOverEvent(activeGame) -> None:
    """Logic for End of Game"""
    activeGame.Running = False
    Menus.GameOverMenu(activeGame=activeGame)


def UpdateBackgroundEvent(activeGame) -> None:
    """Regenerates the Background Elements

    Args-
        activeGame (Game, optional): Current Game Class being used. Defaults to Game.MasterGame.
    """
    activeGame.BackgroundSpriteGroup.empty()
    BackgroundPopulator.AddTables(activeGame=activeGame)
    BackgroundPopulator.AddLockerRooms(activeGame=activeGame)
    BackgroundPopulator.UnlockLockerRooms(activeGame=activeGame)
