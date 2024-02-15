"""Defined Custom Events"""

import pygame

NightCycle = pygame.event.Event(pygame.USEREVENT, attr1="NightCycle")
GameOver = pygame.event.Event(pygame.USEREVENT, attr1="GameOver")
UpdateBackground = pygame.event.Event(pygame.USEREVENT, attr1="UpdateBackground")
