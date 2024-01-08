import pygame
from dataclasses import dataclass
from enum import Enum
workerPath = r"C:\Users\mchaae01\OneDrive - Nidec\Pictures\waiter_110620211.jpg"
customerPath = r"C:\Users\mchaae01\OneDrive - Nidec\Pictures\Picture1.png"

class ImageTypes(Enum):
    Worker,Customer = range(2)

class ImageSprite(pygame.sprite.Sprite):
    correspondingID: int = 0
    imageType: ImageTypes = None
    rect: pygame.Rect = None
    
    
    def __init__(self, position, path, objID):
        super().__init__()
        self.image = pygame.image.load(path)  # Replace with the actual sprite image file
        self.image = pygame.transform.scale_by(self.image,0.25)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        
        if(path == workerPath):
            self.imageType = ImageTypes.Worker
        elif(path == customerPath):
            self.imageType = ImageTypes.Customer
        
        self.correspondingID = objID
        
        
    def UpdatePosition(self, position):
        self.x = position[0]
        self.y = position[1]
        