import pygame
import random
import sys
import os
import math

import time


import time 
from random import randrange 

# Initialize Pygame
pygame.init()

# Constants
screen_info = pygame.display.Info()

WIDTH, HEIGHT = 900, screen_info.current_h - 85
FPS = 60
RED = (255, 0, 0)
BLACK = (0, 0, 0)
NUM_LANES = 3


class Car:
    def __init__(self, x_position, initial_speed):
        self.x = x_position
        self.y = -player_car_img.get_height() # Start above the screen
        self.speed = initial_speed


circle_radius = 0
circle_color_normal = (0, 255, 0)  # Green
circle_color_warning = (255, 0, 0)  # Red
circle_spawn_interval = 20  # in seconds
circle_follow = 8
circle_warning_duration = 6  # in seconds
elapsed_time = 0 
last_circle_spawn_time = 0


def spawn_circle():
    circle = Circle(player_x)
    circles.append(circle)
    return time.time()

def remove_expired_circles():
    for circle in circles.copy():
        if circle.warning_start_time is not None and elapsed_time / FPS - circle.warning_start_time / FPS >= circle_warning_duration:
            circle.color = circle_color_warning    
        if circle.warning_start_time is not None and elapsed_time / FPS - circle.warning_start_time / FPS >= circle_follow:
            circles.remove(circle)
            
def is_collision(rect, circle):
    closest_x = max(rect.left, min(circle.x, rect.right))
    closest_y = max(rect.top, min(circle.y, rect.bottom))
    distance = math.sqrt((circle.x - closest_x) ** 2 + (circle.y - closest_y) ** 2)
    return distance < circle.radius


class Circle:
    def __init__(self, player_x):
        self.x = player_x
        self.y = HEIGHT - HEIGHT / 10
        self.color = (255, 255, 255)
        self.warning_start_time = None
        



#music
music = pygame.mixer.music.load(r"inf audio\DRIVE.mp3")
pygame.mixer.music.play(-1)
    
    
# car sound import
acc_sound = pygame.mixer.Sound(r"inf audio\compi\auto gas.mp3")
crash_sound = pygame.mixer.Sound(r"inf audio\compi\Auto crash.mp3")
brake_sound = pygame.mixer.Sound(r"inf audio\compi\auto bremsen.mp3")
norm_sound = pygame.mixer.Sound(r"inf audio\compi\auto norm.mp3")
heli_sound = pygame.mixer.Sound(r"inf audio\compi\Helicopter.mp3")
missile_sound = pygame.mixer.Sound(r"inf audio\compi\Missile.mp3")



 

class Helicopter:
    def __init__(self, x_position2):
        self.x = x_position2
        self.y = y_position2


# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3-Lane Car Highway Game")
clock = pygame.time.Clock()
score = 0



# Load helicopter image
helicopter_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "helicopter.jpg")).convert()

# Scale the helicopter image
helicopter_scale = 0.05
helicopter_img = pygame.transform.scale(helicopter_img, (int(helicopter_img.get_width() * helicopter_scale), int(helicopter_img.get_height() * helicopter_scale)))
x_position2 = WIDTH // 2 - helicopter_img.get_width() // 2
y_position2 = HEIGHT - helicopter_img.get_height() -50

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

player_y = HEIGHT - HEIGHT / 5

# Initialize enemy cars
enemy_cars = []
#circles
circles = []

# Initialize variables
start_time = time.time()
game_over = False

# Add variables to hold rotation angle and rotation speed
angle = 0
rotation_speed = 1

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if not game_over:
        if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            if angle >0:
                angle -= 2*rotation_speed
                if angle <=1 and angle >=-1:
                    angle = 0
            elif angle <0:
                angle += 2*rotation_speed
                if angle <= 1 and angle>=-1:
                    angle = 0
        
        

        if keys[pygame.K_LEFT] and player_x >= 150:
            player_x -= 8
            angle += rotation_speed
        if keys[pygame.K_RIGHT] and player_x + enemy_car_img.get_width() <= 750:
            player_x += 8
            angle -= rotation_speed
        if keys[pygame.K_UP] and player_y - HEIGHT / 10 >= 0:
            player_y -= 6
        if keys[pygame.K_DOWN] and player_y + HEIGHT / 10 + enemy_car_img.get_height() <= HEIGHT:
            player_y += 6

    
        
        
    # Calculate elapsed time
    current_time = time.time() - start_time
    if int(current_time) % 1 == 0:
        score += 1/60
        
        
        
        
  

    elapsed_time += 1
    if int(elapsed_time) % (circle_spawn_interval * 60) == 0:
        last_circle_spawn_time = spawn_circle()
    remove_expired_circles()






        # Move enemy cars and spawn new ones
    for car in enemy_cars:
        distance_to_bottom = HEIGHT - player_y
        car.y += current_time ** 0.5 + car.speed + 0.01 * distance_to_bottom
        if car.y > HEIGHT:
            enemy_cars.remove(car)





    for lane in range(NUM_LANES):
        if random.randint(0, 800) < 6:
            x_position = random.choice([187.5 - 0.5 * enemy_car_img.get_width(), 362.5 - 0.5 * enemy_car_img.get_width(), 537.5 - 0.5 * enemy_car_img.get_width(), 712.5 - 0.5 * enemy_car_img.get_width()])
            too_close = any(abs(x_position - enemy_car.x) < enemy_car_img.get_width() for enemy_car in enemy_cars if enemy_car.y < HEIGHT and enemy_car.x == x_position)
            if not too_close:
                speed = random.randint(1, 5)
                enemy_cars.append(Car(x_position, speed))

    player_rect = pygame.Rect(player_x, player_y, player_car_img.get_width(), player_car_img.get_height())
    for car in enemy_cars:
        enemy_rect = pygame.Rect(car.x, car.y, enemy_car_img.get_width(), enemy_car_img.get_height())
        if player_rect.colliderect(enemy_rect):
            game_over = True
    
    
    for circle in circles:
        circle_speed = 2  # Adjust the speed as needed
        distance_x = player_x + player_car_img.get_width() / 2 - circle.x
        distance_y = player_y + player_car_img.get_height() / 2 - circle.y
        angle1 = math.atan2(distance_y, distance_x)
        circle.x += circle_speed * math.cos(angle1) 
        circle.y += circle_speed * math.sin(angle1) 
        
        if circle.warning_start_time is None and elapsed_time  % circle_follow * FPS == 0:
            circle.warning_start_time = elapsed_time

    
    
    
    # Draw background
    screen.fill(BLACK)
    screen.blit(player_car_img, (player_x, player_y))
    for car in enemy_cars:
        screen.blit(enemy_car_img, (car.x, car.y))

    # Rotate the player car image
    rotated_player_car = pygame.transform.rotate(player_car_img, angle)
    rotated_rect = rotated_player_car.get_rect(center=(player_x + rotated_player_car.get_width() / 2, player_y + rotated_player_car.get_height() / 2))
    # Draw rotated player car
    screen.blit(rotated_player_car, rotated_rect)

    #Helicopter
    rotated_helicopter = pygame.transform.rotate(helicopter_img, angle)
    rotated_rect2 = rotated_helicopter.get_rect(center=(x_position2 +  rotated_helicopter.get_width() / 2, y_position2 + rotated_helicopter.get_height() / 2))
    # Draw rotated helicopter
    screen.blit(rotated_helicopter, rotated_rect2)
    
    
    
    
    # Draw enemy cars
    for car in enemy_cars:
        screen.blit(enemy_car_img, (car.x, car.y))


    # Draw circles
    for circle in circles:
        circle_radius = circle.y / 5
        pygame.draw.circle(screen, circle.color, (int(circle.x), int(circle.y)), circle_radius)


    score2 = int(score)
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score2}", True, "WHITE")
    score_rect = score_text.get_rect(topright=(WIDTH - 10, 10))
    screen.blit(score_text, score_rect)
    pygame.display.flip()
    clock.tick(FPS)

    # Game over screen
    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over!", True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            
        screen.blit(text, text_rect)
        pygame.display.flip()

        # Wait for a few seconds before quitting
        pygame.time.wait(3000)  # 3000 milliseconds (3 seconds)
        pygame.quit()
        sys.exit()
        
#different speed for cars, 4 lanes. hallo
