import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LANE_WIDTH = 200

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Highway Game")
clock = pygame.time.Clock()

# Load car images
player_car_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "player_car.jpg")).convert()
enemy_car_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "enemy_car.jpg")).convert()

# Initialize player car position
player_x = WIDTH // 2 - player_car_img.get_width() // 2
player_y = HEIGHT - player_car_img.get_height() - 20

# Initialize enemy cars
enemy_cars = []

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
<<<<<<< HEAD
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()

    if not moved:
        player_car.reduce_speed()
        
#halihalo


pygame.quit()















=======
    if keys[pygame.K_LEFT] and player_x - LANE_WIDTH >= 0:
        player_x -= LANE_WIDTH
    if keys[pygame.K_RIGHT] and player_x + LANE_WIDTH <= WIDTH - player_car_img.get_width():
        player_x += LANE_WIDTH
>>>>>>> 6bc1d41b10ef99a79af0a1627fa08635cc5537be

    # Move enemy cars and spawn new ones
    for car in enemy_cars:
        car[1] += 5  # Adjust the speed of enemy cars
        if car[1] > HEIGHT:
            enemy_cars.remove(car)

    if random.randint(0, 100) < 5:  # Adjust the probability for more or fewer enemy cars
        enemy_cars.append([random.choice([player_x, player_x + LANE_WIDTH - enemy_car_img.get_width()]), -enemy_car_img.get_height()])

    # Check for collisions
    player_rect = pygame.Rect(player_x, player_y, player_car_img.get_width(), player_car_img.get_height())
    for car in enemy_cars:
        enemy_rect = pygame.Rect(car[0], car[1], enemy_car_img.get_width(), enemy_car_img.get_height())
        if player_rect.colliderect(enemy_rect):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Draw background
    screen.fill(BLACK)

    # Draw player car
    screen.blit(player_car_img, (player_x, player_y))

    # Draw enemy cars
    for car in enemy_cars:
        screen.blit(enemy_car_img, (car[0], car[1]))

    pygame.display.flip()
    clock.tick(FPS)
