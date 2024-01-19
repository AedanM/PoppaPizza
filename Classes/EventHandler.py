import pygame
import Handlers.ClickHandler as ClickHandler
import Classes.Game as Game


def MainEventHandler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ClickHandler.MouseHandler()
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_t):
            Game.MasterGame.Clock.ChangeClockMul(-1)
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_y):
            Game.MasterGame.Clock.ChangeClockMul(1)
