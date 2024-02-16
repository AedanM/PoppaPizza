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


def SaveSpriteGroup(spriteGroup: pygame.sprite.Group) -> dict:
    saveObj = {}
    for sprite in spriteGroup:
        print(dir(sprite))
        spriteDict = {
            "Image Type": sprite.ImageType if "ImageType" in dir(sprite) else None,
            "Sprite Rect": sprite.rect,
            "Object Type": type(sprite),
            # TODO- Make this state based not lamda based so it can save
            # "MvmHandler": sprite.MvmHandler,
        }
        saveObj[hash(sprite)] = spriteDict
    return saveObj


def LoadSpriteGroup(saveObj, Name, spriteGroup: pygame.sprite.Group) -> None:
    for hashedSprite, savedSprite in saveObj[Name].items():
        for sprite in spriteGroup:
            if hash(sprite) == hashedSprite:
                print(savedSprite)
                # TODO -Finish Load


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
