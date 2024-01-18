"""Handler for User Clicks"""
from enum import Enum
import pygame
import Classes.People as People
import Classes.Game as Game
import Classes.Sprite as Sprite
import Handlers.CustomerHandler as CustomerHandler


class ClickState(Enum):
    Neutral, ClickedCustomer, ClickedWorker = range(3)


GlobalClickState = ClickState.Neutral
GSELECTED = 0


def MouseHandler():
    global GlobalClickState
    mouseX, mouseY = pygame.mouse.get_pos()
    for sprite in Game.MasterGame.CharSpriteGroup:
        if not sprite.IsBackground:
            if sprite.rect.collidepoint(mouseX, mouseY):
                if sprite.ImageType == Sprite.ImageTypes.Customer:
                    CustomerClickRoutine(sprite)
                elif sprite.ImageType == Sprite.ImageTypes.Worker:
                    WorkerClickRoutine(sprite)
            elif GlobalClickState is ClickState.ClickedWorker:
                for worker in Game.MasterGame.CharSpriteGroup:
                    if (
                        worker.CorrespondingID == GSELECTED
                        and worker.ImageType is Sprite.ImageTypes.Worker
                    ):
                        worker.MvmHandler.StartNewMotion(
                            (worker.rect.center), (mouseX, mouseY)
                        )
                GlobalClickState = ClickState.Neutral
            else:
                GlobalClickState = ClickState.Neutral


def CustomerClickRoutine(target):
    global GlobalClickState
    if GlobalClickState is ClickState.Neutral:
        CustomerHandler.AssignWorker(target)

    GlobalClickState = ClickState.ClickedCustomer
    # this is where you make all other sprites glow


def WorkerClickRoutine(target):
    global GlobalClickState, GSELECTED
    if GlobalClickState is ClickState.ClickedCustomer:
        pass
    elif (
        GlobalClickState is ClickState.Neutral
        or GlobalClickState is ClickState.ClickedWorker
    ):
        GSELECTED = target.CorrespondingID
    GlobalClickState = ClickState.ClickedWorker
