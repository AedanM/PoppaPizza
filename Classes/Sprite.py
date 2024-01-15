import pygame
from dataclasses import dataclass
from enum import Enum
from Handlers import *
import Classes.People as People
import Classes.GameObject as GameObj


@dataclass
class ImagePaths:
    workerPath = r"C:\Users\mchaae01\OneDrive - Nidec\Pictures\waiter.png"
    customerPath = r"C:\Users\mchaae01\OneDrive - Nidec\Pictures\Picture1.png"
    tablePath = r"C:\Users\mchaae01\OneDrive - Nidec\Pictures\table.jpg"


iPaths = ImagePaths()


class ImageTypes(Enum):
    Worker, Customer, Table = range(3)


PathToTypeDict = {
    iPaths.workerPath: ImageTypes.Worker,
    iPaths.customerPath: ImageTypes.Customer,
    iPaths.tablePath: ImageTypes.Table,
}


class CharImageSprite(GameObj.GameObject):
    correspondingID: int = 0
    imageType: ImageTypes = None
    rect: pygame.Rect = None
    MvmHandler: MovementHandler.CharacterMovementHandler = None

    def __init__(self, position, path, objID):
        super().__init__(False, True, True)
        self.image = pygame.image.load(
            path
        )  # Replace with the actual sprite image file
        self.image = pygame.transform.scale_by(self.image, 0.25)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.MvmHandler = MovementHandler.CharacterMovementHandler()
        self.imageType = PathToTypeDict[path]

        self.correspondingID = objID

    def updateSprite(self):
        ## Place to add Dynamic Sprites
        pass

    def __repr__(self):
        return str(self.correspondingID) + " " + str(self.imageType)


class BackgroundElementSprite(GameObj.GameObject):
    imageType: ImageTypes = None

    def __init__(self, position, path):
        super().__init__(True, False, False)
        self.image = pygame.image.load(
            path
        )  # Replace with the actual sprite image file
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.imageType = PathToTypeDict[path]
