import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Pixel Art Platformer")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player settings
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 5

# Player state
player_velocity_y = 0
is_jumping = False
gravity = 0.5

# Game loop
running = True
while running:
    screen.fill(WHITE)  # Clear the screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Movement (WASD)
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_w] and not is_jumping:
        player_velocity_y = -10
        is_jumping = True

    # Apply gravity
    player_velocity_y += gravity
    player_y += player_velocity_y

    # Ground collision
    if player_y >= SCREEN_HEIGHT - player_height - 10:
        player_y = SCREEN_HEIGHT - player_height - 10
        is_jumping = False

    # Drawing the player (simple rectangle for now)
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
