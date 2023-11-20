import pygame
import random
import sys
import os
import time 

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LANE_WIDTH = 150
NUM_LANES = 3


# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3-Lane Car Highway Game")
clock = pygame.time.Clock()

# Load car images
player_car_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "player_car.jpg")).convert()
enemy_car_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "enemy_car.jpg")).convert()

# Scale the car images
car_scale1 = 0.2
car_scale2 = 0.5
player_car_img = pygame.transform.scale(player_car_img, (int(player_car_img.get_width() * car_scale1), int(player_car_img.get_height() * car_scale1)))
enemy_car_img = pygame.transform.scale(enemy_car_img, (int(enemy_car_img.get_width() * car_scale2), int(enemy_car_img.get_height() * car_scale2)))

# Initialize player car position
player_x = WIDTH // 2 - player_car_img.get_width() // 2
player_y = HEIGHT - player_car_img.get_height() - 20

# Initialize enemy cars
enemy_cars = []

# Initialize variables
start_time = time.time()
enemy_speed = 5  # Initial speed of enemy cars

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - LANE_WIDTH //3 >= 0:
        player_x -= 8
    if keys[pygame.K_RIGHT] and player_x + LANE_WIDTH //3 <= WIDTH - player_car_img.get_width():
<<<<<<< Updated upstream
        player_x += 8
=======
        player_x += 4
    if keys[pygame.K_UP] and player_y - 30>= 0:
        player_y -= 4
    if keys[pygame.K_DOWN] and player_y + 30 + enemy_car_img.get_height() <= HEIGHT:
        player_y += 4
>>>>>>> Stashed changes

    # Calculate elapsed time
    current_time = time.time() - start_time
    
    # Increase enemy speed over time
    if current_time > 2:  # Adjust the time to change speed
        enemy_speed = 4  # Adjust the new speed
    
    # Move enemy cars and spawn new ones
    for car in enemy_cars:
        car[1] += enemy_speed  # Adjust the speed of enemy cars
        if car[1] > HEIGHT:
            enemy_cars.remove(car)

    for lane in range(NUM_LANES):
        if random.randint(0, 800) < 3:  # Adjust the probability for more or fewer enemy cars
            enemy_cars.append([random.choice([200- 0.5*enemy_car_img.get_width(), 400- 0.5*enemy_car_img.get_width(), 600- 0.5*enemy_car_img.get_width()]), -enemy_car_img.get_height()])

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

