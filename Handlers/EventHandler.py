"""Handlers for all events"""

import copy
import sys

import pygame

from Classes import Matching, MiniGames, Stats
from Definitions import AssetLibrary, CustomEvents
from Generators import BackgroundPopulator, CharSpawner, Menus
from Handlers import ClickHandler, ShopHandler, WorkerHandler


def MainEventHandler(activeGame) -> None:
    """Giant Case Handler for Events

    Args-
        activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.
    """
    RandomSpawnHandler(activeGame=activeGame)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT:
            match (event):
                case CustomEvents.UpdateBackground:
                    BackgroundPopulator.SetupBackground(activeGame=activeGame)
                case CustomEvents.NightCycle:
                    DayNightEvent(activeGame=activeGame)
                case CustomEvents.GameOver:
                    GameOver(activeGame=activeGame)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ClickHandler.MainMouseHandler(
                mousePos=event.pos, isLeftClick=(event.button == 1), activeGame=activeGame
            )
        elif event.type == pygame.KEYDOWN:
            match (event.key):
                case pygame.K_a:
                    activeGame.Mode = MiniGames.GameMode.TriviaGame
                    MiniGames.MakeTriviaGame(activeGame=activeGame)
                case pygame.K_m:
                    activeGame.UserInventory.GetPaid(amount=1000.0)
                case pygame.K_t:
                    activeGame.Settings.ChangeClockMul(value=-1)
                case pygame.K_y:
                    activeGame.Settings.ChangeClockMul(value=1)
                case pygame.K_w:
                    CharSpawner.BuyWorker(activeGame=activeGame)
                case pygame.K_c:
                    CharSpawner.CustomerSpawner(activeGame=activeGame, force=True)
                case pygame.K_2:
                    activeGame.Settings.ToggleClock24()
                case pygame.K_p:
                    activeGame.GameClock.SetRunning(not activeGame.GameClock.Running)
                case pygame.K_ESCAPE:
                    Menus.OptionsMenu(activeGame=activeGame)
                case pygame.K_s:
                    Menus.ShopMenu(activeGame=activeGame)
                case pygame.K_b:
                    ShopHandler.BuyTables(selectedRow=True, activeGame=activeGame)
                case pygame.K_v:
                    ShopHandler.BuyTables(selectedRow=False, activeGame=activeGame)


def DebugSetup(activeGame) -> None:
    """Sets up game in Debug Mode"""
    CharSpawner.BuyWorker(free=True, activeGame=activeGame)
    CharSpawner.BuyWorker(free=True, activeGame=activeGame)


def RandomSpawnHandler(activeGame) -> None:
    """Handles Randomly Spawning Elements"""
    CharSpawner.CustomerSpawner(activeGame=activeGame)


def DayNightEvent(activeGame) -> None:
    """Logic behind a day transition

    Pays Rent
    Loads DayTransition Menu
    Resets Sprites
    Updates Stats
    Resets Background

    """
    ShopHandler.PayUpkeep(activeGame=activeGame)
    if activeGame.UserInventory.Money > 0:
        Menus.DayTransistion(activeGame=activeGame)
    else:
        GameOver(activeGame=activeGame)
    ResetSprites(activeGame=activeGame)
    Stats.AllStats[f"Day {activeGame.GameClock.Day}"] = copy.deepcopy(
        activeGame.UserInventory.Statistics
    )
    Stats.PrevDay = copy.deepcopy(activeGame.UserInventory.Statistics)
    BackgroundPopulator.SetupBackground(activeGame=activeGame)


def ResetSprites(activeGame) -> None:
    """Reset all Sprites

        Kill Customer Sprites
        Reset Workers to Kitchen

    Args-
        activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.
    """
    for sprite in activeGame.CharSpriteGroup:
        if sprite.ImageType in AssetLibrary.CustomerOutfits:
            Matching.RemoveObjFromSprite(activeGame=activeGame, targetSprite=sprite)
        elif sprite.ImageType in AssetLibrary.WorkerOutfits:
            WorkerHandler.DailyReset(sprite=sprite)


def GameOver(activeGame) -> None:
    """Logic for End of Game"""
    activeGame.Running = False
    Menus.GameOverMenu(activeGame=activeGame)


def TriviaEventHandler(activeGame) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ClickHandler.TriviaMouseHandler(mousePos=event.pos, activeGame=activeGame)
        elif event.type == pygame.KEYDOWN:
            match (event.key):
                case pygame.K_a:
                    activeGame.Mode = MiniGames.GameMode.Base
                    activeGame.MiniGame = None
                    activeGame.GameClock.SetRunning(True)
