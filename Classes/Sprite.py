import pygame
from dataclasses import dataclass
from enum import Enum
import Classes.People as People
import Classes.GameObject as GameObj
import Classes.Game as Game
import Classes.utils as utils
from Handlers.MovementHandler import CharacterMovementHandler


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
    MvmHandler: CharacterMovementHandler = None

    def __init__(self, position, path, objID):
        super().__init__(backgroundFlag=False, moveFlag=True, collisionFlag=True)
        self.image = pygame.image.load(
            path
        )  # Replace with the actual sprite image file
        self.image = pygame.transform.scale_by(self.image, 0.1)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.MvmHandler = CharacterMovementHandler()
        self.imageType = PathToTypeDict[path]
        self.checkSpawnCollision()

        self.correspondingID = objID

    def checkSpawnCollision(self):
        currentCenter = self.rect.center
        for group in Game.MasterGame.SpriteGroups:
            for sprite in group:
                while sprite.rect.colliderect(self.rect) and sprite is not self:
                    self.rect.center = utils.PositionRandomVariance(
                        currentCenter, (0.1, 1)
                    )

    def updateSprite(self):
        ## Place to add Dynamic Sprites
        pass

    def __repr__(self):
        return str(self.correspondingID) + " " + str(self.imageType)


class BackgroundElementSprite(GameObj.GameObject):
    imageType: ImageTypes = None

    def __init__(self, position, path):
        super().__init__(backgroundFlag=True, moveFlag=False, collisionFlag=False)
        self.image = pygame.image.load(
            path
        )  # Replace with the actual sprite image file
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.imageType = PathToTypeDict[path]
