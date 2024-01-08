import pygame


class TimerBarClass:
    width: int = 0
    maxWidth: int = 300
    height: int = 25
    color: tuple = (0, 255, 0)
    startTime: int = 0
    completionPercentage: float = 0.0
    jobID: int = 0
    
    def __init__(self, duration: float, displayScreen: pygame.surface.Surface, position: tuple, jobID: int):
        self.Rect = pygame.Rect(position[0], position[1], self.width, self.height)
        self.startTime = pygame.time.get_ticks()
        self.duration = duration
        self.screen = displayScreen
        self.jobID = jobID

    def startTimer(self):
        self.startTime = pygame.time.get_ticks()

    def ageTimer(self):
        self.completionPercentage = (
            (pygame.time.get_ticks() - self.startTime) / 1000.0
        ) / self.duration
        self.width = min(self.completionPercentage * self.maxWidth, self.maxWidth)
        self.updateView()

    def updateView(self):
        self.Rect.width = self.width
        self.Rect.height = self.height
        pygame.draw.rect(self.screen, self.color, self.Rect)
