import pygame
import pygame.gfxdraw
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1200, 1200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Glowing Sprite Example")

# Set up the player sprite
player_image = pygame.image.load(r"C:\Users\mchaae01\OneDrive - Nidec\Pictures\Picture1.png")  # Replace with the actual sprite image file
player_rect = player_image.get_rect()
player_rect.topleft = (100, 100)

# Flag to control glow effect
draw_glow = True

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the glow effect if enabled
    if True:
        glow_radius = 50
        pygame.gfxdraw.filled_circle(screen, player_rect.centerx, player_rect.centery, glow_radius, (255, 255, 0, 50))

    # Draw the player
    # screen.blit(player_image, player_rect.topleft)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)
