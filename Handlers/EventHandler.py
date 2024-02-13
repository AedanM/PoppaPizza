"""Handlers for all events"""

import copy
import sys

import pygame

from Classes import Game, Matching, MiniGames, Stats
from Definitions import AssetLibrary, CustomEvents
from Generators import BackgroundPopulator, CharSpawner, Menus
from Handlers import ClickHandler, ShopHandler, WorkerHandler


def MainEventHandler(activeGame=Game.MasterGame) -> None:
    """Giant Case Handler for Events

    Args:
        activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.
    """
    RandomSpawnHandler()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT:
            match (event):
                case CustomEvents.UpdateBackground:
                    BackgroundPopulator.SetupBackground(Game.MasterGame)
                case CustomEvents.NightCycle:
                    DayNightEvent()
                case CustomEvents.GameOver:
                    GameOver()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ClickHandler.MainMouseHandler(
                mousePos=event.pos, lClick=(event.button == 1)
            )
        elif event.type == pygame.KEYDOWN:
            match (event.key):
                case pygame.K_a:
                    Game.MasterGame.Mode = MiniGames.GameMode.TriviaGame
                    MiniGames.MakeTriviaGame(activeGame=Game.MasterGame)
                case pygame.K_m:
                    Game.MasterGame.UserInventory.GetPaid(amount=1000.0)
                case pygame.K_t:
                    activeGame.Settings.ChangeClockMul(value=-1)
                case pygame.K_y:
                    activeGame.Settings.ChangeClockMul(value=1)
                case pygame.K_w:
                    CharSpawner.BuyWorker()
                case pygame.K_c:
                    CharSpawner.CustomerSpawner(force=True)
                case pygame.K_2:
                    activeGame.Settings.ToggleClock24()
                case pygame.K_p:
                    activeGame.GameClock.SetRunning(not activeGame.GameClock.Running)
                case pygame.K_ESCAPE:
                    Menus.OptionsMenu()
                case pygame.K_s:
                    Menus.ShopMenu()
                case pygame.K_b:
                    ShopHandler.BuyTables(selectedRow=True)
                case pygame.K_v:
                    ShopHandler.BuyTables(selectedRow=False)


def DebugSetup() -> None:
    """Sets up game in Debug Mode"""
    CharSpawner.BuyWorker(free=True)
    CharSpawner.BuyWorker(free=True)


def RandomSpawnHandler() -> None:
    """Handles Randomly Spawning Elements"""
    CharSpawner.CustomerSpawner()


def DayNightEvent() -> None:
    """Logic behind a day transition

    Pays Rent
    Loads DayTransition Menu
    Resets Sprites
    Updates Stats
    Resets Background

    """
    ShopHandler.PayUpkeep()
    if Game.MasterGame.UserInventory.Money > 0:
        Menus.DayTransistion()
    else:
        GameOver()
    ResetSprites(activeGame=Game.MasterGame)
    Stats.AllStats[f"Day {Game.MasterGame.GameClock.Day}"] = copy.deepcopy(
        Game.MasterGame.UserInventory.Statistics
    )
    Stats.PrevDay = copy.deepcopy(Game.MasterGame.UserInventory.Statistics)
    BackgroundPopulator.SetupBackground()


def ResetSprites(activeGame) -> None:
    """Reset all Sprites

        Kill Customer Sprites
        Reset Workers to Kitchen

    Args:
        activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.
    """
    for sprite in activeGame.CharSpriteGroup:
        if sprite.ImageType in AssetLibrary.CustomerOutfits:
            Matching.RemoveObjFromSprite(activeGame=activeGame, targetSprite=sprite)
        elif sprite.ImageType in AssetLibrary.WorkerOutfits:
            WorkerHandler.DailyReset(sprite=sprite)


def GameOver() -> None:
    """Logic for End of Game"""
    Game.MasterGame.Running = False
    Menus.GameOverMenu()


def TriviaEventHandler(activeGame) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ClickHandler.TriviaMouseHandler(mousePos=event.pos)
        elif event.type == pygame.KEYDOWN:
            match (event.key):
                case pygame.K_a:
                    activeGame.Mode = MiniGames.GameMode.Base
                    activeGame.MiniGame = None
                    activeGame.GameClock.SetRunning(True)
