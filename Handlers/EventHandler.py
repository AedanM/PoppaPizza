"""Handlers for all events"""

import copy
import sys

import pygame

from Classes import Game, Matching, Stats
from Definitions import AssetLibrary, CustomerDefs, CustomEvents, Prices
from Generators import BackgroundPopulator, CharSpawner, Menus
from Handlers import ClickHandler, ShopHandler, WorkerHandler


def MainEventHandler(activeGame=Game.MasterGame) -> None:
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
            ClickHandler.MouseHandler(mousePos=event.pos, lClick=(event.button == 1))
        elif event.type == pygame.KEYDOWN:
            match (event.key):
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
    CharSpawner.BuyWorker(free=True)
    CharSpawner.BuyWorker(free=True)


def RandomSpawnHandler() -> None:
    CharSpawner.CustomerSpawner()


def DayNightEvent() -> None:
    workerPay = 0.0
    for worker in Game.MasterGame.WorkerList:
        workerPay += worker.BasePay * Prices.DefaultPrices.Salary
    rent = Prices.CurrentRent
    Game.MasterGame.UserInventory.PayMoney(amount=workerPay + rent, update=False)
    if Game.MasterGame.UserInventory.Money > 0:
        Menus.DayTransistion()
    else:
        GameOver()
    for sprite in Game.MasterGame.CharSpriteGroup:
        if sprite.ImageType in AssetLibrary.CustomerOutfits:
            Matching.RemoveObjFromSprite(
                activeGame=Game.MasterGame, targetSprite=sprite
            )
        elif sprite.ImageType in AssetLibrary.WorkerOutfits:
            WorkerHandler.DailyReset(sprite=sprite)

    Stats.PrevDay = copy.deepcopy(Game.MasterGame.UserInventory.Statistics)
    BackgroundPopulator.SetupBackground()


def GameOver() -> None:
    Game.MasterGame.Running = False
    Menus.GameOverMenu()
