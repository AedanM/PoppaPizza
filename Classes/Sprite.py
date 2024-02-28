"""Class for visibile sprites"""

from typing import Any

import pygame

from AtomicbritEngine.Engine import SpriteObjects, TimerBar, Utils
from Classes import GameBase
from Definitions import AssetLibrary, ColorDefines
from Definitions.DefinedLocations import LocationDefs
from Handlers import CharacterMovementHandler, Matching


class CharImageSprite(SpriteObjects.CharacterSprite):
    """Class for Sprites of Characters"""

    # pylint: disable=invalid-name
    CorrespondingID: int = 0
    ImageType: AssetLibrary.ImageTypes = AssetLibrary.ImageTypes.Null
    PersonalTimer: TimerBar.TimerBar = None  # type: ignore

    def __init__(
        self,
        path,
        objID,
        position: tuple[int, int] = None,  # type: ignore
        center: tuple[int, int] = None,  # type: ignore
        maxSize: int = int(Utils.ScaleValToSize(val=100, newSize=LocationDefs.ScreenSize)),
    ) -> None:
        super().__init__(
            backgroundFlag=False,
            moveFlag=True,
            collisionFlag=True,
            maxSize=maxSize,
            position=position,
            center=center,
            path=path,
        )
        self.ImageType = AssetLibrary.PathToTypeDict[path]
        # self.CheckSpawnCollision()
        self.CorrespondingID = objID
        self.MvmHandler = CharacterMovementHandler.CharacterMovementHandler()

    # HACK- pass active game in plz
    @property
    def DataObject(self) -> Any | None:
        """Numerical Data Object Associated with Image

        Returns-
            Customer | Worker: Data Object Assoc with Sprite
        """
        activeGame = GameBase.MasterGame
        objDict = Matching.MatchIdToPerson(activeGame=activeGame, inputId=self.CorrespondingID)
        if objDict is not None and "sprite" in objDict:
            objDict.pop("sprite")
            obj = list(objDict.values())[0]
            return obj

    def CheckSpawnCollision(self, activeGame) -> None:
        """Changes spawn location until new sprite is not colliding

        Args-
            activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.
        """
        currentCenter = self.rect.center
        for group in activeGame.SpriteGroups:
            for sprite in group:
                while sprite.rect.colliderect(self.rect) and sprite is not self:
                    self.rect.center = Utils.PositionRandomVariance(
                        position=currentCenter,
                        percentVariance=(0.1, 1),
                        screenSize=activeGame.ScreenSize,
                    )

    def ChangeOutfit(self, newOutfitPath) -> None:
        """Update Sprite Image and resize to fit

        Args-
            newOutfitPath (str): Path to New Outfit
        """
        newImage = pygame.image.load(newOutfitPath).convert_alpha()
        newImageRect = newImage.get_rect()
        dim = Utils.ResizeMaxLength(
            dim=(newImageRect.width, newImageRect.height),
            maxSide=max(self.rect.width, self.rect.height),
        )
        newImage = pygame.transform.scale(newImage, dim)
        newImageRect = self.rect
        self.image = newImage
        self.ImageType = AssetLibrary.PathToTypeDict[newOutfitPath]

    def UpdateSprite(self, activeGame) -> None:
        """Update sprite for each frame"""
        if self.PersonalTimer is not None:
            self.UpdateTimerAndDraw(activeGame=activeGame)
            self.PersonalTimer.Rect = self.rect.topleft  # type: ignore
        super().UpdateSprite(activeGame=activeGame)

    def UpdateTimerAndDraw(self, activeGame) -> None:
        """Update Timer Dimensions and Redraw if active

        Args-
            activeGame (Game, optional): Current Game. Defaults to Game.MasterGame.
        """
        timerBar = self.PersonalTimer
        if timerBar.Running:
            timerBar.UpdateTimer(currentTime=activeGame.GameClock.Minute)
            customerObj = Matching.MatchIdToPerson(
                activeGame=activeGame, inputId=timerBar.AssocId, targetOutput="customer"
            )
            if (
                timerBar.StartingState != 0
                and timerBar.AssocId != 0
                and (
                    customerObj is None
                    or customerObj.CurrentState.value != timerBar.StartingState  # type: ignore
                )
            ):
                timerBar.Running = False
            else:
                pygame.draw.rect(
                    activeGame.Screen,
                    timerBar.MaxColor.RGB,
                    timerBar.MaxTimerRect,
                )
                pygame.draw.rect(
                    activeGame.Screen,
                    timerBar.DynamicColor,
                    timerBar.TimerRect,
                )

    def CreatePersonTimerBar(
        self,
        completeTask,
        activeGame,
        assocId=0,
        length=29.0,
        startingState=0,
        offset=(0, 0),
        width=0,
        fillColor=ColorDefines.LimeGreen,
    ) -> None:
        """Create a timer bar bound to this objcet

        Args-
            completeTask (Task): Function to exec on completion of timer
            assocId (int, optional): Id of Associated Job. Defaults to 0.
            length (float, optional): Length of Timer in game minutes. Defaults to 29.0.
            startingState (int, optional): Starting State of Customer, if Object is one. Defaults to 0.
            offset (tuple, optional): Offset of timer bar from sprite. Defaults to (0, 0).
            width (int, optional): Max width of timer bar. Defaults to 0.
            fillColor (ColorTools.Color, optional): Color of Timer bar. Defaults to ColorTools.LimeGreen.
        """
        self.PersonalTimer = TimerBar.TimerBar(
            duration=length if length != 0 else 29.0,
            position=(self.rect.topleft),
            assocId=assocId,
            offset=offset,
            startTime=activeGame.GameClock.Minute,
        )
        self.PersonalTimer.StartingState = startingState
        self.PersonalTimer.OnComplete = completeTask
        self.PersonalTimer.TimerRect.y -= 25
        self.PersonalTimer.SetMaxSize(size=self.rect.width if width == 0 else width)
        self.PersonalTimer.FillColor = fillColor
        self.PersonalTimer.RestartTimer(currentTime=activeGame.GameClock.Minute)

    def __repr__(self) -> str:
        """String Rep of Object"""
        return str(self.CorrespondingID) + " " + str(self.ImageType)


class BackgroundElementSprite(SpriteObjects.GameObject):
    """Class for background sprites"""

    ImageType: AssetLibrary.ImageTypes = AssetLibrary.ImageTypes.Null

    # pylint: disable=invalid-name
    def __init__(self, position, path, maxSize=60, offset=(0, 0)) -> None:
        """Init for background elements

        Args-
            position (tuple): Top left corner of sprite
            path (str): Path to image
            maxSize (int, optional): Max size of element. Defaults to 60.
            offset (tuple, optional): Offset from position. Defaults to (0, 0).
        """
        super().__init__(backgroundFlag=True, moveFlag=False, collisionFlag=False)
        self.image = pygame.image.load(
            path
        ).convert_alpha()  # Replace with the actual sprite image file
        self.rect = self.image.get_rect()
        dim = Utils.ResizeMaxLength(dim=(self.rect.width, self.rect.height), maxSide=maxSize)
        self.image = pygame.transform.scale(self.image, dim)
        self.rect.x = position[0] + offset[0]

        self.rect.y = position[1] + offset[1]
        self.ImageType = AssetLibrary.PathToTypeDict[path]


class ButtonObject(SpriteObjects.GameObject):
    """Defined Button Shape"""

    # pylint: disable=invalid-name
    def __init__(
        self,
        position,
        text="Blank",
        color=ColorDefines.White,
        backColor=ColorDefines.Black,
        size=(100, 100),
        enabled=True,
    ) -> None:
        """Init for Button

        Args-
            position (tuple): Center of button
            text (str, optional): String for Button to Show. Defaults to "Blank".
            color (Color, optional): Base Color. Defaults to ColorTools.White.
            backColor (Color, optional): Background Color. Defaults to ColorTools.Black.
            size (tuple, optional): Dimensions of Shape. Defaults to (100, 100).
            enabled (bool, optional): Is the button able to be clicked. Defaults to True.
        """
        super().__init__(backgroundFlag=True, moveFlag=False, collisionFlag=False)
        self.image = pygame.Surface(size=size)
        self.image.fill(backColor.RGB if enabled else ColorDefines.Grey.RGB)
        self.image.set_alpha(240 if enabled else 128)
        self.text = text
        self.position = position
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

    @classmethod
    def AddButton(cls, location, text, color, backColor, enabled, activeGame) -> None:
        """Generates a Button on a specified location

        Args-
            location (tuple): tuple position of button center
            text (str): Button Label
            color (Color): Main Color
            backColor (Color): Background Color of Button
            enabled (bool): Button Enable
            activeGame (Game, optional): Current Game being used. Defaults to Game.MasterGame.
        """
        buttonObj = ButtonObject(
            position=location,
            color=color,
            backColor=backColor,
            text=text,
            size=[125, 50],
            enabled=enabled,  # type:ignore
        )

        activeGame.ForegroundSpriteGroup.add(buttonObj)
        if not [x for x in activeGame.ButtonList if x.position == location]:
            activeGame.ButtonList.append(buttonObj)
