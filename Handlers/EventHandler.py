import pygame
import sys
from Classes import People, CustomEvents, Prices
from Classes.Game import MasterGame
from Handlers import ClickHandler
from Generators import CharSpawner, BackgroundPopulator


def MainEventHandler(activeGame=MasterGame) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT and event == CustomEvents.NightCycle:
            DayNightEvent(activeGame)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ClickHandler.MouseHandler()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            activeGame.Settings.ChangeClockMul(value=-1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
            activeGame.Settings.ChangeClockMul(value=1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            People.Worker.CreateWorker()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            People.Customer.CreateCustomer()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            activeGame.Settings.ToggleClock24()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            activeGame.ShowScreen = not activeGame.MasterGame.ShowScreen


def DebugSetup() -> None:
    CharSpawner.WorkerSpawner(force=True)
    CharSpawner.WorkerSpawner(force=True)
    BackgroundPopulator.AddTables()


def DayNightEvent(activeGame=MasterGame) -> None:
    print("DAY CHANGE EVENT HERE")
    workerPay = 0.0
    for worker in activeGame.WorkerList:
        workerPay += worker.BasePay
    rent = Prices.CurrentRent

    activeGame.UserInventory.Money -= workerPay + rent
