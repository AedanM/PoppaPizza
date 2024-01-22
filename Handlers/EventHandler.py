import pygame
import sys
from Classes import People, CustomEvents
from Classes.Game import MasterGame
from Handlers import ClickHandler


def MainEventHandler(activeGame=MasterGame) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT and event == CustomEvents.NightCycle:
            print("DAY CHANGE EVENT HERE")
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
