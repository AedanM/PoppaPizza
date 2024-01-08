import pygame
import pygame.gfxdraw
import Classes.People as pc
import Classes.Job as jc
import Classes.Sprite as sc
import Classes.Game as g
from enum import Enum


class ClickState(Enum):
    Neutral,Clicked_Customer,Clicked_Worker  = range(3)
    
GlobalClickState = ClickState.Neutral
GlobalSelectedID = 0


def MouseHandler():
    global GlobalClickState, GlobalSelectedID
    mouse_x,mouse_y = pygame.mouse.get_pos()
    print(mouse_x,mouse_y, GlobalClickState)
    for sprite in g.MasterGame.SpriteGroup:
        if sprite.rect.collidepoint(mouse_x,mouse_y):
            print("Connected")
            if(sprite.imageType == sc.ImageTypes.Customer):
                CustomerClickRoutine(sprite)
            elif(sprite.imageType == sc.ImageTypes.Worker):
                WorkerClickRoutine(sprite)
            break
        elif(GlobalClickState is ClickState.Clicked_Worker):
            for worker in g.MasterGame.SpriteGroup:
                if(worker.correspondingID == GlobalSelectedID and worker.imageType is sc.ImageTypes.Worker):
                    print(worker.rect)
                    worker.rect.x = mouse_x
                    worker.rect.y = mouse_y
                    print(worker.rect)
                    GlobalClickState = ClickState.Neutral
            break
        else:
            GlobalClickState = ClickState.Neutral
    
def CustomerClickRoutine(target):
    global GlobalClickState
    if(GlobalClickState is ClickState.Neutral):
        for sprite in g.MasterGame.SpriteGroup:
            GlobalClickState = ClickState.Clicked_Customer
            #this is where you make all other sprites glow
    

def WorkerClickRoutine(target):
    global GlobalClickState, GlobalSelectedID
    if(GlobalClickState is ClickState.Clicked_Customer):
        
        pass
    elif(GlobalClickState is ClickState.Neutral):
        GlobalSelectedID = target.correspondingID
    GlobalClickState = ClickState.Clicked_Worker
    
                