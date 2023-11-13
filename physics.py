import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CAR_WIDTH, CAR_HEIGHT = 50, 100
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Car Game")

# Load car image
car_image = pygame.image.load("pictures/car.png")  # Make sure to replace "car.png" with the path to your car image
car_image = pygame.transform.scale(car_image, (CAR_WIDTH, CAR_HEIGHT))

# Initial car position
car_x = WIDTH // 2 - CAR_WIDTH // 2
car_y = HEIGHT - CAR_HEIGHT - 20

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Update car position based on keys
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= 5
    if keys[pygame.K_RIGHT] and car_x < WIDTH - CAR_WIDTH:
        car_x += 5
    if keys[pygame.K_UP] and car_y > 0:
        car_y -= 5
    if keys[pygame.K_DOWN] and car_y < HEIGHT - CAR_HEIGHT:
        car_y += 5

    # Draw background
    screen.fill(WHITE)

    # Draw road (a simple straight line)
    pygame.draw.line(screen, BLACK, (0, 0), (WIDTH, 0), 5)

    # Draw the car
    screen.blit(car_image, (car_x, car_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
