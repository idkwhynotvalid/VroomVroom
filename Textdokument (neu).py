import pygame
import random
import sys
import os
import time 

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 900, 1000
FPS = 60
RED = (255, 0, 0)
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
enemy_speed = 10  # Initial speed of enemy cars
game_over = False


# Add variables to hold rotation angle and rotation speed
angle = 0 
rotation_speed = 5


# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT] and player_x - LANE_WIDTH >= 0:
            player_x -= 8
            angle = rotation_speed
        if keys[pygame.K_RIGHT] and player_x + LANE_WIDTH <= WIDTH - player_car_img.get_width():
            player_x += 8
            angle = -rotation_speed
        if keys[pygame.K_UP] and player_y - 30>= 0:
            player_y -= 6
        if keys[pygame.K_DOWN] and player_y + 30 + enemy_car_img.get_height() <= HEIGHT:
            player_y += 6


    # Calculate elapsed time
    current_time = time.time() - start_time
    
    # Move enemy cars and spawn new ones
    for car in enemy_cars:
        car[1] += current_time**0.5  # Adjust the speed of enemy cars
        if car[1] > HEIGHT:
            enemy_cars.remove(car)
            
            
    for lane in range(NUM_LANES):
        if random.randint(0, 800) < 6:
            x_position = random.choice([300 - 0.5 * enemy_car_img.get_width(), 400 - 0.5 * enemy_car_img.get_width(), 500 - 0.5 * enemy_car_img.get_width(), 600 - 0.5 * enemy_car_img.get_width()])
            too_close = any(abs(x_position - car[0]) < enemy_car_img.get_width() for car in enemy_cars if car[1] < HEIGHT and car[0] == x_position)
            if not too_close:
                enemy_cars.append([x_position, -enemy_car_img.get_height()])



    # Check for collisions
    player_rect = pygame.Rect(player_x, player_y, player_car_img.get_width(), player_car_img.get_height())
    for car in enemy_cars:
        enemy_rect = pygame.Rect(car[0], car[1], enemy_car_img.get_width(), enemy_car_img.get_height())
        if player_rect.colliderect(enemy_rect):
            game_over=True
    
    
   
    
    
    # Rotate the player car image
    rotated_player_car = pygame.transform.rotate(player_car_img, angle)
    rotated_rect = rotated_player_car.get_rect(center=(player_x + rotated_player_car.get_width() / 2, player_y + rotated_player_car.get_height() / 2))
    # Draw rotated player car
    screen.blit(rotated_player_car, rotated_rect)
    

    # Draw background
    screen.fill(BLACK)
    screen.blit(player_car_img, (player_x, player_y))
    for car in enemy_cars:
        screen.blit(enemy_car_img, (car[0], car[1]))
    
    
    # Draw player car
   # screen.blit(player_car_img, (player_x, player_y))

    # Draw enemy cars
    for car in enemy_cars:
        screen.blit(enemy_car_img, (car[0], car[1]))


    pygame.display.flip()
    clock.tick(FPS)
    
    # Game over screen
    if game_over == True:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over!", True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()

        # Wait for a few seconds before quitting
        pygame.time.wait(3000)  # 3000 milliseconds (3 seconds)
        pygame.quit()
        sys.exit()
        
        
#different speed for cars, 4 lanes.

