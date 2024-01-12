import pygame
import pygame.gfxdraw
from enum import Enum
import Classes.People as People
import Classes.Game as Game
import Classes.Sprite as Sprite
import Classes.ColorTools as ColorTools
import Handlers.CustomerHandler as CustomerHandler


class ClickState(Enum):
    Neutral, Clicked_Customer, Clicked_Worker = range(3)


GlobalClickState = ClickState.Neutral
GlobalSelectedID = 0


def MouseHandler():
    global GlobalClickState, GlobalSelectedID
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for sprite in Game.MasterGame.CharSpriteGroup:
        if not sprite.isBackground:
            if sprite.rect.collidepoint(mouse_x, mouse_y):
                if sprite.imageType == Sprite.ImageTypes.Customer:
                    CustomerClickRoutine(sprite)
                elif sprite.imageType == Sprite.ImageTypes.Worker:
                    WorkerClickRoutine(sprite)
                break
            elif GlobalClickState is ClickState.Clicked_Worker:
                for worker in Game.MasterGame.CharSpriteGroup:
                    if (
                        worker.correspondingID == GlobalSelectedID
                        and worker.imageType is Sprite.ImageTypes.Worker
                    ):
                        worker.MvmHandler.startNewMotion((worker.rect.center),(mouse_x, mouse_y))
                GlobalClickState = ClickState.Neutral
                break
            else:
                GlobalClickState = ClickState.Neutral


def CustomerClickRoutine(target):
    global GlobalClickState
    if GlobalClickState is ClickState.Neutral:
        CustomerHandler.AssignWorker(target)

    GlobalClickState = ClickState.Clicked_Customer
    # this is where you make all other sprites glow


def WorkerClickRoutine(target):
    # target.image = ColorTools.ChangeColorToColor(target, 0, 128)
    global GlobalClickState, GlobalSelectedID
    if GlobalClickState is ClickState.Clicked_Customer:
        pass
    elif (
        GlobalClickState is ClickState.Neutral
        or GlobalClickState is ClickState.Clicked_Worker
    ):
        GlobalSelectedID = target.correspondingID
    GlobalClickState = ClickState.Clicked_Worker
