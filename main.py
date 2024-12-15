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

# Load assets
player_idle = pygame.image.load("assets/player_idle.png")
player_run = [
    pygame.image.load("assets/player_run1.png"),
    pygame.image.load("assets/player_run2.png"),
]
player_slash = [
    pygame.image.load("assets/player_slash1.png"),
    pygame.image.load("assets/player_slash2.png"),
]

# Scale assets
player_idle = pygame.transform.scale(player_idle, (50, 50))
player_run = [pygame.transform.scale(img, (50, 50)) for img in player_run]
player_slash = [pygame.transform.scale(img, (50, 50)) for img in player_slash]

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
is_slashing = False

# Animation variables
frame_index = 0
frame_delay = 5
frame_counter = 0
player_state = "idle"  # "idle", "run", "slash"

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
        player_state = "run"
    elif keys[pygame.K_d]:
        player_x += player_speed
        player_state = "run"
    else:
        player_state = "idle"

    if keys[pygame.K_w] and not is_jumping:
        player_velocity_y = -10
        is_jumping = True

    # Katana controls (Arrow keys)
    if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        player_state = "slash"
        is_slashing = True

    # Apply gravity
    player_velocity_y += gravity
    player_y += player_velocity_y

    # Ground collision
    if player_y >= SCREEN_HEIGHT - player_height - 10:
        player_y = SCREEN_HEIGHT - player_height - 10
        is_jumping = False

    # Animation handling
    frame_counter += 1
    if frame_counter >= frame_delay:
        frame_counter = 0
        frame_index = (frame_index + 1) % len(player_run if player_state == "run" else player_slash)

    # Draw player
    if player_state == "idle":
        screen.blit(player_idle, (player_x, player_y))
    elif player_state == "run":
        screen.blit(player_run[frame_index], (player_x, player_y))
    elif player_state == "slash":
        screen.blit(player_slash[frame_index], (player_x, player_y))
        if frame_index == len(player_slash) - 1:
            is_slashing = False  # Reset slashing after animation

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
