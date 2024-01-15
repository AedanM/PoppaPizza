import pygame


class DefinedLocations:
    @property
    def KitchenLocation(self):
        return (100, 100)

    @property
    def KitchenDoorLocation(self):
        return (150, 200)

    @property
    def LockerRoomLocation(self):
        return (500, 10)

    @property
    def CustomerExit(self):
        return (1200, 1000)


LocationDefs = DefinedLocations()


class DefinedPaths:
    @staticmethod
    def KitchenToCustomer(sprite, dest):
        return [sprite.rect.center, LocationDefs.KitchenDoorLocation, dest.rect.center]

    @staticmethod
    def BackToKitchen(sprite):
        return [
            sprite.rect.center,
            LocationDefs.KitchenDoorLocation,
            LocationDefs.KitchenLocation,
        ]

    @staticmethod
    def CustomerToExit(sprite):
        return [sprite.rect.center, LocationDefs.CustomerExit]
