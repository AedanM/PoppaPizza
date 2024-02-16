import os
import pickle
from typing import Any

import pygame

DEFAULT_SAVE_FOLDER = r".\Saves\\"
if not os.path.exists(DEFAULT_SAVE_FOLDER):
    os.mkdir(DEFAULT_SAVE_FOLDER)


def SaveImage(obj, surface) -> Any:
    return pygame.image.tobytes(surface, "RGBA")


def LoadImage(obj, imageBytes) -> Any:
    return pygame.image.frombytes(imageBytes, (obj.rect.width, obj.rect.height), "RGBA")


def SaveGame(path, saveObj) -> bool:
    try:
        with open(DEFAULT_SAVE_FOLDER + path, "wb") as fp:
            pickle.dump(saveObj, fp)
            return True
    except IOError as e:
        print(f"Error:{e} - Cannot Save Game")
    return False


def LoadGame(path) -> tuple[bool, Any]:
    try:
        with open(DEFAULT_SAVE_FOLDER + path, "rb") as fp:
            newGame = pickle.load(fp)
            return (True, newGame)
    except IOError as e:
        print(f"Error:{e} - Cannot Save Game")
    return (False, None)
