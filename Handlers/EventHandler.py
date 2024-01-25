import pygame
import sys
from Classes import Game
from Definitions import CustomEvents, Prices
from Handlers import ClickHandler
from Generators import CharSpawner, BackgroundPopulator, Menus


def MainEventHandler(activeGame=Game.MasterGame) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT and event == CustomEvents.NightCycle:
            DayNightEvent()
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
            activeGame.Clock.SetRunning(not activeGame.Clock.Running)
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


def DayNightEvent() -> None:
    print("DAY CHANGE EVENT HERE")
    workerPay = 0.0
    for worker in Game.MasterGame.WorkerList:
        workerPay += worker.BasePay * Prices.DefaultPrices.Salary
    rent = Prices.CurrentRent

    Game.MasterGame.UserInventory.Money -= workerPay + rent
