"""Functions for Text Generation"""

from Definitions import ColorTools
from Utilities import Utils


def CreateTextBox(
    locationTopLeft, text, foreColor, font, screen, backColor=None
) -> None:
    """Write a text box to the screen

    Args:
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
    textrect.x = locationTopLeft[0]
    textrect.y = locationTopLeft[1]
    screen.blit(source=text, dest=textrect)


def WriteDateLabel(activeGame) -> None:
    """Write Date and $ into top left bar

    Args:
        activeGame (Game): Current Game
    """
    clockText = (
        f"{activeGame.GameClock.DateTime} ${activeGame.UserInventory.Money:0.2f}"
    )

    CreateTextBox(
        locationTopLeft=(0, 0),
        text=clockText,
        foreColor=ColorTools.White,
        backColor=ColorTools.Blue,
        font=activeGame.Font,
        screen=activeGame.Screen,
    )


def WriteButtonLabel(activeGame) -> None:
    """Adds a text box label to all active buttons

    Args:
        activeGame (Game): Current Game
    """
    for button in activeGame.ButtonList:
        CreateTextBox(
            locationTopLeft=Utils.OffsetTuple(
                inputTuple=button.position, offset=(-45, -12)
            ),
            text=button.text,
            foreColor=ColorTools.Black,
            font=activeGame.Font,
            screen=activeGame.Screen,
        )
