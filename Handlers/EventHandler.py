"""Handlers for all events"""
import sys

import pygame

from Classes import Game
from Definitions import AssetLibrary, CustomerDefs, CustomEvents, Prices
from Generators import BackgroundPopulator, CharSpawner, Menus
from Handlers import ClickHandler


def MainEventHandler(activeGame=Game.MasterGame) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT:
            match (event):
                case CustomEvents.UpdateBackground:
                    BackgroundPopulator.SetupBackground()
                case CustomEvents.NightCycle:
                    DayNightEvent()
                case CustomEvents.GameOver:
                    GameOver()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ClickHandler.MouseHandler(mousePos=event.pos)
        elif event.type == pygame.KEYDOWN:
            match (event.key):
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
                case pygame.K_d:
                    activeGame.ShowScreen = not activeGame.MasterGame.ShowScreen
                case pygame.K_ESCAPE:
                    Menus.OptionsMenu()
                case pygame.K_s:
                    Menus.ShopMenu()


def DebugSetup() -> None:
    CharSpawner.BuyWorker(free=True)
    CharSpawner.BuyWorker(free=True)


def RandomSpawnHandler() -> None:
    CharSpawner.CustomerSpawner()


def DayNightEvent() -> None:
    print("DAY CHANGE EVENT HERE")
    workerPay = 0.0
    for worker in Game.MasterGame.WorkerList:
        workerPay += worker.BasePay * Prices.DefaultPrices.Salary
    rent = Prices.CurrentRent
    Game.MasterGame.UserInventory.Money -= workerPay + rent
    if Game.MasterGame.UserInventory.Money < 0:
        pygame.event.post(CustomEvents.GameOver)
    for sprite in Game.MasterGame.CharSpriteGroup:
        if (
            sprite.ImageType in AssetLibrary.CustomerOutfits
            and sprite.DataObject.CurrentState
            is not CustomerDefs.CustomerStates.BeingServed
        ):
            Game.MasterGame.RemoveObjFromSprite(targetSprite=sprite)


def GameOver() -> None:
    Game.MasterGame.Running = False
    Menus.GameOverMenu()
