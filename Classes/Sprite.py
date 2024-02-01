"""Class for visibile sprites"""
import pygame

from Classes import Game, GameObject, TimerBar
from Definitions import AssetLibrary, ColorTools
from Handlers import MovementHandler
from Utilities import Utils as utils


class CharImageSprite(GameObject.GameObject):
    # pylint: disable=invalid-name
    CorrespondingID: int = 0
    ImageType: AssetLibrary.ImageTypes = AssetLibrary.ImageTypes.Null
    rect: pygame.rect.Rect = pygame.rect.Rect(0, 0, 0, 0)
    MvmHandler: MovementHandler.CharacterMovementHandler = None
    PersonalTimer: TimerBar.TimerBar = None

    def __init__(self, position, path, objID, maxSize=100) -> None:
        super().__init__(backgroundFlag=False, moveFlag=True, collisionFlag=True)
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(surface=self.image, size=(maxSize, maxSize))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.MvmHandler = MovementHandler.CharacterMovementHandler()
        self.ImageType = AssetLibrary.PathToTypeDict[path]
        # self.CheckSpawnCollision()

        self.CorrespondingID = objID

    @property
    def DataObject(self):
        objDict = Game.MasterGame.MatchIdToPerson(inputId=self.CorrespondingID)
        objDict.pop("sprite")
        obj = list(objDict.values())[0]
        return obj

    def CheckSpawnCollision(self, activeGame=Game.MasterGame) -> None:
        currentCenter = self.rect.center
        for group in activeGame.SpriteGroups:
            for sprite in group:
                while sprite.rect.colliderect(self.rect) and sprite is not self:
                    self.rect.center = utils.PositionRandomVariance(
                        position=currentCenter,
                        percentVarianceTuple=(0.1, 1),
                        screenSize=activeGame.ScreenSize,
                    )

    def ChangeOutfit(self, newOutfitPath) -> None:
        newImage = pygame.image.load(newOutfitPath)
        newImageRect = newImage.get_rect()
        dim = utils.ResizeMaxLength(
            dim=(newImageRect.width, newImageRect.height),
            maxSide=max(self.rect.width, self.rect.height),
        )
        newImage = pygame.transform.scale(newImage, dim)
        newImageRect = self.rect
        self.image = newImage
        self.ImageType = AssetLibrary.PathToTypeDict[newOutfitPath]

    def UpdateSprite(self) -> None:
        if self.PersonalTimer is not None:
            self.PersonalTimer.UpdateAndDraw()
            self.PersonalTimer.Rect = self.rect.topleft
        self.Update()

    def CreatePersonTimerBar(
        self,
        completeTask,
        assocId=0,
        length=29.0,
        startingState=0,
        offset=(0, 0),
        width=0,
        fillColor=ColorTools.LimeGreen,
    ) -> None:
        self.PersonalTimer = TimerBar.TimerBar(
            duration=length if length != 0 else 29.0,
            position=(self.rect.topleft),
            assocId=assocId,
            offset=offset,
        )
        self.PersonalTimer.StartingState = startingState
        self.PersonalTimer.OnComplete = completeTask
        self.PersonalTimer.TimerRect.y -= 25
        self.PersonalTimer.SetMaxSize(size=self.rect.width if width == 0 else width)
        self.PersonalTimer.FillColor = fillColor
        self.PersonalTimer.StartTimer()

    def __repr__(self) -> str:
        return str(self.CorrespondingID) + " " + str(self.ImageType)


class BackgroundElementSprite(GameObject.GameObject):
    ImageType: AssetLibrary.ImageTypes = AssetLibrary.ImageTypes.Null

    # pylint: disable=invalid-name
    def __init__(self, position, path, maxSize=60, offset=(0, 0)) -> None:
        super().__init__(backgroundFlag=True, moveFlag=False, collisionFlag=False)
        self.image = pygame.image.load(
            path
        )  # Replace with the actual sprite image file
        self.rect = self.image.get_rect()
        dim = utils.ResizeMaxLength(
            dim=(self.rect.width, self.rect.height), maxSide=maxSize
        )
        self.image = pygame.transform.scale(self.image, dim)
        self.rect.x = position[0] + offset[0]

        self.rect.y = position[1] + offset[1]
        self.ImageType = AssetLibrary.PathToTypeDict[path]


class RectangleObject(GameObject.GameObject):
    # pylint: disable=invalid-name
    def __init__(
        self,
        position,
        color=(0, 0, 0),
        size=(100, 100),
    ) -> None:
        super().__init__(backgroundFlag=True, moveFlag=False, collisionFlag=False)
        self.image = pygame.Surface(size=size)
        self.image.fill(color.RGB)
        self.rect = self.image.get_rect()
        self.rect.center = position


class ButtonObject(GameObject.GameObject):
    # pylint: disable=invalid-name
    OnClick = None

    def __init__(
        self,
        position,
        text="Blank",
        color=ColorTools.White,
        backColor=ColorTools.Black,
        size=(100, 100),
        onClick=None,
    ) -> None:
        super().__init__(backgroundFlag=True, moveFlag=False, collisionFlag=False)
        self.image = pygame.Surface(size=size)
        self.image.fill(backColor.RGB)
        self.image.set_alpha(240)
        self.text = text
        self.position = position
        self.OnClick = onClick
        self.Color = color
        buttonRect = pygame.Rect(0, 0, size[0], size[1])
        pygame.draw.rect(
            surface=self.image,
            color=color.RGB,
            rect=buttonRect,
            width=5,
            border_radius=10,
        )

        self.rect = self.image.get_rect()
        self.rect.center = position
