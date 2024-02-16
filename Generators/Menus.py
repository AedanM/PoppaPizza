"""Generator Functions for Menus"""

import pygame_menu

from Handlers import ShopHandler

global GlobalGame


def OpenMenu(activeGame) -> None:
    """Default Entry Point for Menus"""
    global GlobalGame
    GlobalGame = activeGame
    activeGame.GameClock.SetRunning(state=False)


def CloseMenu() -> None:
    """Default Exit Point for Menus"""
    global GlobalGame
    GlobalGame.GameClock.SetRunning(state=True)


def DayTransistion(activeGame) -> None:
    """Splash screen between days

    Args-
        surface (pygame.Surface, optional): Screen to render menu on.
    """
    OpenMenu(activeGame=activeGame)
    menu = pygame_menu.Menu(
        title="End of Day",
        width=800,
        height=600,
        theme=pygame_menu.themes.THEME_GREEN,  # type: ignore
        onclose=CloseMenu,
    )
    menu.add.label(title=f"Day {activeGame.GameClock.Day}", label_id="Title")
    menu.get_widget(widget_id="Title").scale(width=2, height=2, smooth=True)  # type: ignore
    menu.add.label(
        title=(
            f"Customers Served: {activeGame.UserInventory.Statistics.GetDailyServedCustomers()}"
            + " / "
            + f"{activeGame.UserInventory.Statistics.GetDailyTotalCustomers()}"
        )
    )
    menu.add.label(
        title=f"Costume Changes: {activeGame.UserInventory.Statistics.GetDailyCostumeChanges()}"
    )
    menu.add.label(
        title=f"Money Earned: {activeGame.UserInventory.Statistics.GetDailyEarnings():.2f}"
    )
    menu.add.label(title=f"Money Spent: {activeGame.UserInventory.Statistics.GetDailySpend():.2f}")
    menu.add.label(title=f"Profit: {activeGame.UserInventory.Statistics.GetDailyProfit():.2f}")
    menu.add.button(title="Continue to Next Day", action=pygame_menu.events.CLOSE)  # type: ignore
    menu.mainloop(surface=activeGame.Screen, wait_for_event=True)


def OptionsMenu(activeGame) -> None:
    """Menu for Game Configuration

    Args-
        surface (pygame.Surface, optional): Screen to render menu on. Defaults to Game.activeGame.Screen.
    """
    OpenMenu(activeGame=activeGame)
    surface = activeGame.Screen
    menu = pygame_menu.Menu(
        title="Settings",
        width=400,
        height=300,
        theme=pygame_menu.themes.THEME_BLUE,  # type: ignore
        onclose=CloseMenu,
    )
    menu.add.toggle_switch(
        toggleswitch_id="24Toggle",
        title="24 Hour Clock",
        default=activeGame.Settings.Clock24,
        state_text=("Off", "On"),
        state_values=(False, True),
        onchange=lambda x: activeGame.Settings.SetClock24(value=x),
    )
    menu.add.range_slider(
        title="Speed",
        default=0,
        range_values=list(
            range(
                activeGame.Settings.ClockPowRange[0],
                activeGame.Settings.ClockPowRange[1] + 1,
            )
        ),
        value_format=lambda x: f"{pow(base=2, exp=x)}x",
        range_text_value_enabled=False,
        onchange=lambda x: (activeGame.Settings.SetClockMul(value=x)),
    )

    menu.add.button(title="Return", action=pygame_menu.events.CLOSE)  # type: ignore
    menu.mainloop(surface=surface, wait_for_event=True)


def ShopMenu(activeGame) -> None:
    """Menu for shop screen

    Args-
        surface (pygame.Surface, optional): Screen to generate Menu on. Defaults to Game.activeGame.Screen.
    """
    OpenMenu(activeGame=activeGame)
    surface = activeGame.Screen
    menu = pygame_menu.Menu(
        title="Shop",
        width=800,
        height=600,
        theme=pygame_menu.themes.THEME_BLUE,  # type: ignore
        onclose=CloseMenu,
    )
    menu.add.range_slider(
        title="Daily Advertising Spend",
        default=0.0,
        range_values=(0, 500.0),
        increment=1.0,
    )
    menu.add.button(
        title="x1",
        action=lambda: (ShopHandler.BuyNumWorkers(num=1, activeGame=activeGame)),
    )
    menu.add.button(title="Return", action=pygame_menu.events.CLOSE)  # type: ignore
    menu.mainloop(surface=surface, wait_for_event=True)


# TODO- Move Reason to Enum
def GameOverMenu(activeGame, reason="You ran out of Money") -> None:
    """Displayed Screen when Game Ends

    Args-
        surface (pygame.Screen, optional): Screen which the menu is rendered on. Defaults to Game.activeGame.Screen.
        reason (str, optional): Reason for Game Over as a Str. Defaults to "You ran out of Money".
    """
    OpenMenu(activeGame=activeGame)
    surface = activeGame.Screen
    menu = pygame_menu.Menu(
        title="Game Over",
        width=activeGame.Screen.get_width(),
        height=activeGame.Screen.get_height(),
        onclose=pygame_menu.events.EXIT,  # type: ignore
        theme=pygame_menu.themes.THEME_DARK,  # type: ignore
    )
    menu.add.label(title=f"Game Over \n{reason}\n\n", font_size=60, font_shadow=True)
    menu.add.button(title="Close Game", action=pygame_menu.events.EXIT)  # type: ignore
    menu.mainloop(surface=surface)
