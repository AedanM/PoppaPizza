"""Handlers for all events"""
import sys
import pygame
from Classes import Game
from Definitions import CustomEvents, CustomerDefs, Prices, AssetLibrary
from Handlers import ClickHandler
from Generators import CharSpawner, BackgroundPopulator, Menus


def MainEventHandler(activeGame=Game.MasterGame) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT and event == CustomEvents.NightCycle:
            DayNightEvent()
        if event.type == pygame.USEREVENT and event == CustomEvents.GameOver:
            GameOver()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ClickHandler.MouseHandler(event=event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            activeGame.Settings.ChangeClockMul(value=-1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
            activeGame.Settings.ChangeClockMul(value=1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            CharSpawner.BuyWorker()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            CharSpawner.CustomerSpawner(force=True)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            activeGame.Settings.ToggleClock24()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            activeGame.GameClock.SetRunning(not activeGame.GameClock.Running)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            activeGame.ShowScreen = not activeGame.MasterGame.ShowScreen
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            Menus.OptionsMenu()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            Menus.ShopMenu()


def DebugSetup() -> None:
    CharSpawner.BuyWorker(free=True)
    CharSpawner.BuyWorker(free=True)

    BackgroundPopulator.SetupBackground()


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
