"""Class for visibile sprites"""
from dataclasses import dataclass
from enum import Enum
import pygame
import Classes.People as People
import Classes.GameObject as GameObj
import Classes.Game as Game
import Utilities.Utils as utils
from Handlers.MovementHandler import CharacterMovementHandler


@dataclass
class ImagePaths:
    AssetFolder = r"Assets"
    WorkerPath = AssetFolder + r"\waiter.png"
    CustomerPath = AssetFolder + r"\person.png"
    TablePath = AssetFolder + r"\table.png"
    BackgroundPath = AssetFolder + r"\background.png"


iPaths = ImagePaths()


class ImageTypes(Enum):
    Null, Worker, Customer, Table = range(4)


PathToTypeDict = {
    iPaths.WorkerPath: ImageTypes.Worker,
    iPaths.CustomerPath: ImageTypes.Customer,
    iPaths.TablePath: ImageTypes.Table,
}


class CharImageSprite(GameObj.GameObject):
    CorrespondingID: int = 0
    ImageType: ImageTypes = ImageTypes.Null
    rect: pygame.rect.Rect = pygame.rect.Rect(0, 0, 0, 0)
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
        self.ImageType = PathToTypeDict[path]
        self.CheckSpawnCollision()

        self.CorrespondingID = objID

    def CheckSpawnCollision(self):
        currentCenter = self.rect.center
        for group in Game.MasterGame.SpriteGroups:
            for sprite in group:
                while sprite.rect.colliderect(self.rect) and sprite is not self:
                    self.rect.center = utils.PositionRandomVariance(
                        currentCenter, (0.1, 1), Game.MasterGame.ScreenSize
                    )

    def UpdateSprite(self):
        ## Place to add Dynamic Sprites
        pass

    def __repr__(self):
        return str(self.CorrespondingID) + " " + str(self.ImageType)


class BackgroundElementSprite(GameObj.GameObject):
    ImageType: ImageTypes = ImageTypes.Null

    def __init__(self, position, path):
        super().__init__(backgroundFlag=True, moveFlag=False, collisionFlag=False)
        self.image = pygame.image.load(
            path
        )  # Replace with the actual sprite image file
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect.y = position[1]
        self.ImageType = PathToTypeDict[path]
