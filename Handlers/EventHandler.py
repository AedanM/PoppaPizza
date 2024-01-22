import pygame
import sys
from Classes import Settings, People, Game
from Handlers import ClickHandler


def MainEventHandler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ClickHandler.MouseHandler()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            Settings.GameSettings.ChangeClockMul(value=-1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
            Settings.GameSettings.ChangeClockMul(value=1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            People.Worker.CreateWorker()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            People.Customer.CreateCustomer()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            Game.MasterGame.ShowScreen = not Game.MasterGame.ShowScreen
