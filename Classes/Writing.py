"""Functions for Text Generation"""

import pygame
from Definitions import AssetLibrary, ColorDefines
from Definitions.DefinedLocations import LocationDefs
from Engine import Color, Utils

pygame.font.init()
DefinedFonts = {
    "Titles": pygame.font.Font(
        filename=pygame.font.match_font("elephant"),  # type: ignore
        size=60,
    ),
    "Trivia Game": pygame.font.Font(
        filename=pygame.font.match_font("century schoolbook", True), size=36  # type: ignore
    ),
    "Datetime": pygame.font.Font(filename=pygame.font.match_font("book antiqua"), size=24),  # type: ignore
    "Buttons": pygame.font.Font(
        filename=pygame.font.match_font("gill sans", True),  # type: ignore
        size=24,
    ),  # type: ignore
    "Default": pygame.font.Font(
        filename=pygame.font.match_font("century schoolbook"),  # type: ignore
        size=24,
    ),  # type: ignore
    "Trivia Answers": pygame.font.Font(
        filename=pygame.font.match_font("century schoolbook"), size=48  # type: ignore
    ),
}


class TextBox:
    Text: str
    TopLeft: tuple | None
    Center: tuple | None
    ForeColor: Color.Color
    Font: pygame.font.Font
    Rect: pygame.Rect

    def __init__(
        self,
        text="",
        topLeft=None,
        center=None,
        foreColor=ColorDefines.White,
        font=DefinedFonts["Default"],
    ) -> None:
        self.Text = text
        self.TopLeft = topLeft
        self.Center = center
        self.ForeColor = foreColor
        self.Font = font

    def WriteToScreen(self, activeScreen) -> None:
        return CreateTextBox(
            text=self.Text,
            foreColor=self.ForeColor,
            font=self.Font,
            screen=activeScreen,
            locationTopLeft=self.TopLeft,
            center=self.Center,
        )


def CreateTextBox(
    text, foreColor, font, screen, backColor=None, locationTopLeft=None, center=None
) -> None:
    """Write a text box to the screen

    Args-
        locationTopLeft (tuple): Top left position of bounding box
        text (str): Text to Write
        foreColor (ColorTools.Color): Text Color
        font (ColorTools.Color): Font Object
        screen (pygame.Surface): Screen to write onto
        backColor (ColorTools.Color, optional): Background of text box, None is transparency. Defaults to None.
    """
    text = (
        font.render(text, False, foreColor.RGB)
        if not backColor
        else font.render(text, False, foreColor.RGB, backColor.RGB)
    )
    textrect = text.get_rect()
    if locationTopLeft:
        textrect.x = locationTopLeft[0]
        textrect.y = locationTopLeft[1]
    elif center:
        textrect.center = center
    screen.blit(source=text, dest=textrect)
    return textrect


def WriteDateLabel(activeGame) -> None:
    """Write Date and $ into top left bar

    Args-
        activeGame (Game): Current Game
    """
    clockText = f"{activeGame.GameClock.DateTime} ${activeGame.UserInventory.Money:0.2f} FPS:{round(activeGame.GameClock.PygameClock.get_fps(),2)}"

    CreateTextBox(
        locationTopLeft=(0, 0),
        text=clockText,
        foreColor=ColorDefines.White,
        backColor=ColorDefines.Blue,
        font=DefinedFonts["Datetime"],
        screen=activeGame.Screen,
    )


def WriteButtonLabel(activeGame) -> None:
    """Adds a text box label to all active buttons

    Args-
        activeGame (Game): Current Game
    """
    for button in activeGame.ButtonList:
        CreateTextBox(
            locationTopLeft=Utils.OffsetTuple(inputTuple=button.position, offset=(-45, -12)),
            text=button.text,
            foreColor=ColorDefines.Black,
            font=DefinedFonts["Buttons"],
            screen=activeGame.Screen,
        )


def WriteKitchenLabel(activeGame) -> None:
    kitchenRect = [
        x for x in activeGame.ForegroundSpriteGroup if x.rect.center == LocationDefs.LockerRoom0
    ][0].rect
    numWorkers = len(
        [
            sprite
            for sprite in activeGame.CharSpriteGroup
            if sprite.ImageType in AssetLibrary.WorkerOutfits
            and kitchenRect.collidepoint(sprite.rect.x, sprite.rect.y)
        ]
    )

    kitchenText = f"{numWorkers} Worker{'s' if numWorkers != 1 else ''} inside"

    CreateTextBox(
        locationTopLeft=Utils.OffsetTuple(inputTuple=LocationDefs.LockerRoom0, offset=(-100, 0)),
        text=kitchenText,
        foreColor=ColorDefines.White,
        font=DefinedFonts["Default"],
        screen=activeGame.Screen,
    )
