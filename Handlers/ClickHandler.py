"""Handler for User Clicks"""
from enum import Enum
import pygame
from Classes import Game, Sprite, People
from Handlers import CustomerHandler


class ClickState(Enum):
    Neutral, ClickedCustomer, ClickedWorker = range(3)


GlobalClickState = ClickState.Neutral


def MouseHandler() -> None:
    global GlobalClickState
    mouseX, mouseY = pygame.mouse.get_pos()
    for sprite in Game.MasterGame.CharSpriteGroup:
        if not sprite.IsBackground:
            if sprite.rect.collidepoint(mouseX, mouseY):
                if sprite.ImageType == Sprite.ImageTypes.Customer:
                    CustomerClickRoutine(target=sprite)
                elif sprite.ImageType == Sprite.ImageTypes.Worker:
                    WorkerClickRoutine(target=sprite)
            elif GlobalClickState is ClickState.ClickedWorker:
                GlobalClickState = ClickState.Neutral
            else:
                GlobalClickState = ClickState.Neutral


def CustomerClickRoutine(target) -> None:
    global GlobalClickState
    customerObj = Game.MasterGame.MatchSpriteToPerson(
        inputId=target.CorrespondingID, targetOutput="customer"
    )
    if (
        GlobalClickState is ClickState.Neutral
        and not customerObj.WorkerAssigned
        and customerObj.CurrentState == People.CustomerStates.Queuing
    ):
        CustomerHandler.SitAtTable(target=target, customer=customerObj)
    elif (
        GlobalClickState is ClickState.Neutral
        and customerObj.CurrentState == People.CustomerStates.WaitingForService
    ):
        CustomerHandler.AssignWorker(target=target, targetObj=customerObj)

    GlobalClickState = ClickState.ClickedCustomer
    # this is where you make all other sprites glow


def WorkerClickRoutine(target) -> None:
    pass
