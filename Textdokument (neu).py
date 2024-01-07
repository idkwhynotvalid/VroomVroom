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
pygame.mixer.init()

# Constants
screen_info = pygame.display.Info()

HEIGHT = screen_info.current_h - 85
WIDTH = HEIGHT/1000*1224
FPS = 60
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (169, 169, 169)
NUM_LANES = 5


folder = "compi"

#l = os.path.join("audio", folder, "auto gas.mp3")
#l = r"inf audio\{ort}\auto gas.mp3".format(ort=folder)

#import sound
acc_sound_compi = pygame.mixer.Sound(os.path.join("inf audio", "compi", "auto gas.mp3"))
norm_sound_compi = pygame.mixer.Sound(os.path.join("inf audio", "compi", "auto norm.mp3"))
heli_sound_compi = pygame.mixer.Sound(os.path.join("inf audio", "compi", "Helicopter.mp3"))
missile_sound_compi = pygame.mixer.Sound(os.path.join("inf audio", "compi", "Missile.mp3"))
crash_sound_compi = pygame.mixer.Sound(os.path.join("inf audio", "compi", "Auto crash.mp3"))
brake_sound_compi = pygame.mixer.Sound(os.path.join("inf audio", "compi", "auto bremsen.mp3"))

#import human sound
acc_sound_me = pygame.mixer.Sound(os.path.join("inf audio", "me", "auto gas.mp3"))
norm_sound_me = pygame.mixer.Sound(os.path.join("inf audio", "me", "auto norm.mp3"))
heli_sound_me = pygame.mixer.Sound(os.path.join("inf audio", "me", "Helicopter.mp3"))
missile_sound_me = pygame.mixer.Sound(os.path.join("inf audio", "me", "Missile.mp3"))
crash_sound_me = pygame.mixer.Sound(os.path.join("inf audio", "me", "Auto crash.mp3"))
brake_sound_me = pygame.mixer.Sound(os.path.join("inf audio", "me", "auto bremsen.mp3"))

        #music import
music = pygame.mixer.music.load(r"inf audio\DRIVE.mp3")


class StartScreenAnimation(pygame.sprite.Sprite):
    def __init__(self, scale=1.0):
        super().__init__()
        self.sprites = [
            pygame.image.load(os.path.join(os.path.dirname(__file__), "frame_0.png")),
            pygame.image.load(os.path.join(os.path.dirname(__file__), "frame_1.png")),
            pygame.image.load(os.path.join(os.path.dirname(__file__), "frame_2.png")),
            pygame.image.load(os.path.join(os.path.dirname(__file__), "frame_3.png")),
            pygame.image.load(os.path.join(os.path.dirname(__file__), "frame_4.png")),
            pygame.image.load(os.path.join(os.path.dirname(__file__), "frame_5.png")),
        ]
        self.current_sprite = 0
        self.scale = scale
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (int(self.sprites[self.current_sprite].get_width() * scale), int(self.sprites[self.current_sprite].get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = [0, 0]
        self.animation_speed = 5  # Adjust animation speed as needed
        self.frame_counter = 0



    def update(self):
        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.current_sprite = (self.current_sprite + 1) % len(self.sprites)
            self.image = pygame.transform.scale(self.sprites[self.current_sprite], (int(self.sprites[self.current_sprite].get_width() * self.scale), int(self.sprites[self.current_sprite].get_height() * self.scale)))



class background_load (pygame.sprite.Sprite):
    def __innit__(self, pos_x, pos_y):
        super().__innit__()
        self.sprites = []
        self.sprites.append(pygame.image.load((os.path.join(os.path.dirname(__file__), "frame_0.png"))))
        self.sprites.append(pygame.image.load((os.path.join(os.path.dirname(__file__), "frame_1.png"))))
        self.sprites.append(pygame.image.load((os.path.join(os.path.dirname(__file__), "frame_2.png"))))
        self.sprites.append(pygame.image.load((os.path.join(os.path.dirname(__file__), "frame_3.png"))))
        self.sprites.append(pygame.image.load((os.path.join(os.path.dirname(__file__), "frame_4.png"))))
        self.sprites.append(pygame.image.load((os.path.join(os.path.dirname(__file__), "frame_5.png"))))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        
        self.rect = self.image.get_rect()
        self.rect.topleft = [0,0]
    
    def update(self):
        self.current_sprite += 1
        
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            
        self.image = self.sprites[self.current_sprite]
    


class Helicopter:
    def __init__(self, x_position2):
        self.x = x_position2
        self.y = y_position2


class Car:
    def __init__(self, x_position, y_position, speed, image):
        self.x = x_position
        self.y = y_position
        self.speed = speed
        self.image = image

    def bottom(self):
        return self.y + self.image.get_height()


class Circle:
    def __init__(self, player_x):
        self.x = player_x
        self.y = HEIGHT - HEIGHT / 10
        self.spawn_time = time.time()  # Track when the circle is spawned
        self.lifespan = circle_spawn_interval  # Set lifespan for each circle
        self.warning_start_time = None
        self.explosion_triggered = False
        self.explosion_y = None
        self.explosion_set = False
        self.show_warning = False


circle_radius = 0
circle_color_normal = (0, 255, 0)  # Green
circle_color_warning = (255, 0, 0)  # Red
circle_spawn_interval = 13  # in seconds#20
circle_follow = 3 #8
circle_wait = 8 #12
circle_warning_duration = 2  # in seconds6
elapsed_time = 0 
last_circle_spawn_time = 0
checkingsth = True
distance_to_bottom = 0
collision_check_enabled = True
last_chosen_lane = None


def spawn_circle():
    circle = Circle(player_x)
    circles.append(circle)
    return time.time()

def remove_expired_circles():
    global game_over
    global checkingsth
    current_time = time.time()

    for circle in circles.copy():
        # Calculate the elapsed time since the circle was spawned
        time_since_spawn = int(current_time - circle.spawn_time)




        # Check if it's time to show the warning circle
        if time_since_spawn >= circle_follow:
            checkingsth = False
            circle.warning_start_time = current_time
            circle.show_warning = True
      

        # Check if it's time to show the explosion circle
        if time_since_spawn >= circle_follow + circle_warning_duration:
            is_collision()
            circle.show_warning = False
            circle.explosion_triggered = True
            if not circle.explosion_set:
                circle.explosion_y = circle.y - 20*speed3
                circle.explosion_set = True  # Mark that explosion position is set     






        # Check if the circle has exceeded its lifespan and should be removed
        if time_since_spawn >= circle_wait:
            circles.remove(circle)
            checkingsth = True
            circle.explosion_set = False




def is_collision(): 
    global game_over
    player_mask = pygame.mask.from_surface(rotated_player_car)

    offset = (circle.x - player_x, circle.y - player_y)
    
    #if player_mask.overlap(circle_mask, offset):
#        game_over = True
#       print("hallo")

    warn_mask = pygame.mask.from_surface(warn_img)  # Assuming enemy_car has an 'image' attribute
    offset = (int(circle.x - player_x - warn_img.get_width() / 2), int(circle.y - player_y - warn_img.get_height() / 2))


    
    if collision_check_enabled:
        if player_mask.overlap(warn_mask, offset):
            game_over = True

def will_collide(new_car, existing_cars, lookahead=2000):
    new_car_bottom = new_car.bottom()

    for car in existing_cars:
        if car.x == new_car.x:
            car_bottom = car.bottom()
            if not (new_car_bottom < car.y or new_car.y > car_bottom):
                return True
            if new_car.speed > car.speed:
                distance_to_reach_car_front = car.y - new_car_bottom
                time_to_reach_car_front = distance_to_reach_car_front / (new_car.speed - car.speed)
                predicted_car_front_bottom = car_bottom + (car.speed * time_to_reach_car_front)
                if 0 < time_to_reach_car_front < lookahead and new_car.y < predicted_car_front_bottom:
                    return True
    return False

def remove_overlapping_cars(cars):
    cars_to_remove = []

    # Sort cars in each lane by their y position
    sorted_cars = sorted(cars, key=lambda car: (car.x, car.y))

    for i in range(len(sorted_cars) - 1):
        car1, car2 = sorted_cars[i], sorted_cars[i + 1]

        # Check only cars in the same lane
        if car1.x == car2.x:
            # Check if car1 overlaps with car2
            if car1.y < car2.y < car1.y + car1.image.get_height():
                cars_to_remove.append(car2)  # Choose the car ahead to remove

    # Remove the cars that are overlapping
    for car in cars_to_remove:
        cars.remove(car)

def is_spawn_area_clear(new_car_x, new_car_height, existing_cars, buffer=200):
    spawn_area_top = -new_car_height - buffer
    spawn_area_bottom = buffer

    for car in existing_cars:
        if car.x == new_car_x:
            car_top = car.y
            car_bottom = car.y + car.image.get_height()
            if not (car_bottom < spawn_area_top or car_top > spawn_area_bottom):
                return False
    return True



# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3-Lane Car Highway Game")
clock = pygame.time.Clock()
score = 0

#start_screen
game_state = "start_screen"
mindistance = 1000

# Load helicopter image
helicopter_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "helicopter.jpg")).convert()

# Scale the helicopter image
helicopter_scale = 0.05
helicopter_img = pygame.transform.scale(helicopter_img, (int(helicopter_img.get_width() * helicopter_scale), int(helicopter_img.get_height() * helicopter_scale)))
x_position2 = WIDTH // 2 - helicopter_img.get_width() // 2
y_position2 = HEIGHT - helicopter_img.get_height() -50



# Load car images
player_car_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "fc-rx7.png")).convert_alpha()

enemy_car_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "enemy_car.png")).convert_alpha()

circle_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "warning.png")).convert_alpha()

explosion_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "explo.png")).convert_alpha()

warn_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "3818227.png")).convert_alpha()
trafficfolder = os.path.join(os.path.dirname(__file__), "traffic")
enemy_car_images = [
    pygame.image.load(os.path.join(trafficfolder, "lada_1.png")).convert_alpha(),
    pygame.image.load(os.path.join(trafficfolder, "lada_2.png")).convert_alpha(),
    pygame.image.load(os.path.join(trafficfolder, "lada_3.png")).convert_alpha(),
    pygame.image.load(os.path.join(trafficfolder, "pickup_truck.png")).convert_alpha(),
    pygame.image.load(os.path.join(trafficfolder, "pickup_truck_2.png")).convert_alpha(),
    pygame.image.load(os.path.join(trafficfolder, "truck_1.png")).convert_alpha(),
]


# explosion variables before main loop

explosion_img_frame1 = pygame.image.load(os.path.join(os.path.dirname(__file__), "elxplo_frame_0.png")).convert_alpha()
explosion_img_frame2 = pygame.image.load(os.path.join(os.path.dirname(__file__), "elxplo_frame_1.png")).convert_alpha()
explosion_img_frame3 = pygame.image.load(os.path.join(os.path.dirname(__file__), "elxplo_frame_2.png")).convert_alpha()
explosion_img_frame4 = pygame.image.load(os.path.join(os.path.dirname(__file__), "elxplo_frame_3.png")).convert_alpha()
explosion_img_frame5 = pygame.image.load(os.path.join(os.path.dirname(__file__), "elxplo_frame_4.png")).convert_alpha()
explosion_img_frame6 = pygame.image.load(os.path.join(os.path.dirname(__file__), "elxplo_frame_5.png")).convert_alpha()
explosion_img_frame7 = pygame.image.load(os.path.join(os.path.dirname(__file__), "elxplo_frame_6.png")).convert_alpha()
explosion_img_frame8 = pygame.image.load(os.path.join(os.path.dirname(__file__), "elxplo_frame_7.png")).convert_alpha()
explosion_img_frame9 = pygame.image.load(os.path.join(os.path.dirname(__file__), "elxplo_frame_8.png")).convert_alpha()


explosion_img_list = [explosion_img_frame1,
                      explosion_img_frame2,
                      explosion_img_frame3,
                      explosion_img_frame4,
                      explosion_img_frame5,
                      explosion_img_frame6,
                      explosion_img_frame7,
                      explosion_img_frame8,
                      explosion_img_frame9
                      ] # ...

multiplication = 1
explosion_event = 0
current_explosion_frame = 0

# functions

def explode(expl_x, expl_y):
    global explosion_event
    global explosion_x
    global explosion_y
    global current_explosion_frame
    global explosion_delay

    pygame.mixer.Sound.play(missile_sound_compi)
    #print("explosion")
    current_explosion_frame = 0
    explosion_delay = 0
    
    
    
    explosion_event = 1
    # 0 = stop
    # 1 = start
    # 2 = animating

    explosion_x = expl_x
    explosion_y = expl_y



def explosion_anim():
    global explosion_event
    global current_explosion_frame
    global explosion_delay
     
    explosion_speed = 5

    if explosion_event == 1: # start animation
        explosion_event = 2
        current_explosion_frame = 0

    elif current_explosion_frame == len(explosion_img_list): # end animation
        explosion_event = 0
        return

    elif explosion_event == 2: # animate
        
        
        # draw current frame
        global explosion_x
        global explosion_y

        explosion_y += 20 * multiplication 
        
        #print(elapsed_time, explosion_x, explosion_y)

        explosion_img_rect = explosion_img_list[current_explosion_frame].get_rect(
        center=((explosion_x + explosion_img_list[current_explosion_frame].get_width() / 2),
                (explosion_y + explosion_img_list[current_explosion_frame].get_height() / 2))
        )

        #print("blitting:", current_explosion_frame)

        screen.blit(pygame.transform.scale(explosion_img_list[current_explosion_frame], (
            explosion_img_list[current_explosion_frame].get_width() * 2,
            explosion_img_list[current_explosion_frame].get_height() * 2
        )), explosion_img_rect)
        
        explosion_delay += 1

        if explosion_delay % explosion_speed == 0:
            current_explosion_frame += 1
    



def scale_car_images(car_images, scale_factor):
    return [pygame.transform.scale(img, (int(img.get_width() * scale_factor), int(img.get_height() * scale_factor))) for img in car_images]

# Scale the car images
car_scale1 = 1
car_scale2 = 1.2
scaled_enemy_car_images = scale_car_images(enemy_car_images, car_scale2)
danger_scale = 1.4
warn_scale = 1.4
player_car_img = pygame.transform.scale(player_car_img, (int(player_car_img.get_width() * car_scale1), int(player_car_img.get_height() * car_scale1)))
enemy_car_img = pygame.transform.scale(enemy_car_img, (int(enemy_car_img.get_width() * car_scale2), int(enemy_car_img.get_height() * car_scale2)))
circle_img = pygame.transform.scale(circle_img, (int(circle_img.get_width() * danger_scale), int(circle_img.get_height() * danger_scale)))
warn_img = pygame.transform.scale(warn_img, (int(warn_img.get_width() * warn_scale), int(warn_img.get_height() * warn_scale)))
# Initialize player car position
player_x = WIDTH // 2 - player_car_img.get_width() // 2

player_y = HEIGHT - HEIGHT / 5
#Helicopter x update
desired_helicopter_x = player_x
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


#background
background = pygame.image.load("background.jpg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Load and scale your background image
background = pygame.image.load("background.jpg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Initialize the y position for the background
background_y = 0
circle_y2 = 0
speed3 = 15

# Font setup for start screen
font = pygame.font.Font(None, 40)
text_yes = font.render("Yes", True, BLACK)
text_no = font.render("No", True, BLACK)
text_question = font.render("Humor?", True, BLACK)




#spritegroup

moving_sprites = pygame.sprite.Group()

first = 1
iteration = 0



pygame.init()

game_state = "start_screen"

start_screen_animation = StartScreenAnimation(scale=2.9)
# Game loop
while True:
    
    iteration += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif game_state == "start_screen" and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 300 <= mouse_pos[0] <= 500 and 300 <= mouse_pos[1] <= 350:
                folder = "me"
                game_state = "game_running"
                print("Starting the game...")  # Replace with your game start code
            elif 300 <= mouse_pos[0] <= 500 and 400 <= mouse_pos[1] <= 450:
                game_state = "game_running"

            
    

    


    if game_state == "start_screen":
        # Update and draw the animation during the start screen
        screen.fill((0, 0, 0))
    
   

        
        # Draw start screen elements
        start_screen_animation.update()
        screen.blit(start_screen_animation.image, start_screen_animation.rect)

        
        bg_frame_0 = pygame.image.load(os.path.join(os.path.dirname(__file__), "frame_0.png")).convert_alpha()
        bg_frame_1 = pygame.image.load(os.path.join(os.path.dirname(__file__), "frame_1.png")).convert_alpha()
        bg_frame_2 = pygame.image.load(os.path.join(os.path.dirname(__file__), "frame_2.png")).convert_alpha()
        bg_frame_3 = pygame.image.load(os.path.join(os.path.dirname(__file__), "frame_3.png")).convert_alpha()
        bg_frame_4 = pygame.image.load(os.path.join(os.path.dirname(__file__), "frame_4.png")).convert_alpha()
        bg_frame_5 = pygame.image.load(os.path.join(os.path.dirname(__file__), "frame_5.png")).convert_alpha()

        bg_frame_list = [bg_frame_0,
                         bg_frame_1,
                         bg_frame_2,
                         bg_frame_3,
                         bg_frame_4,
                         bg_frame_5
                         ]



    
        screen.blit(pygame.transform.scale(bg_frame_list[iteration % 6], (bg_frame_list[iteration % 6].get_width() * 3.8, bg_frame_list[iteration % 6].get_height() * 3.8)), (-450, 0))

        pygame.draw.rect(screen, WHITE, (300, 300, 200, 50))
        pygame.draw.rect(screen, WHITE, (300, 400, 200, 50))
        screen.blit(text_yes, (350, 315))
        screen.blit(text_no, (360, 415))
        screen.blit(text_question, (WIDTH/2-100, 100))

        pygame.display.flip()
    
    

        if folder == "me":
            
            pygame.mixer.music.set_volume(0.5)
            heli_sound_me.set_volume(2)
        else:
            pygame.mixer.music.set_volume(0.5)
            heli_sound_compi.set_volume(0.3)
        #play music
        clock.tick(FPS)


        pygame.mixer.music.play(-1)


    elif game_state == "game_running":
        
        if folder == "compi":
            pygame.mixer.Sound.play(heli_sound_compi, -1)
            pygame.mixer.Sound.play(norm_sound_compi,-1)
            pygame.mixer.Sound.play(acc_sound_compi,-1)
            
        else:
            pygame.mixer.Sound.play(heli_sound_me, -1)
            pygame.mixer.Sound.play(norm_sound_me,-1)
            pygame.mixer.Sound.play(acc_sound_me,-1)
            
          


        # Ensure the background loops seamlessly
        if background_y > 0:
            background_y = -background.get_height() + (background_y % background.get_height())
        

        # Blit the background image to create the scrolling effect
        screen.blit(background, (0, background_y))
        screen.blit(background, (0, background_y + background.get_height()))
                 
        


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
            

            if keys[pygame.K_LEFT]: #if player_x <= WIDTH/1224*300 or player_x + enemy_car_img.get_width() >= WIDTH-(WIDTH/1224*300)
                angle += rotation_speed
                
            if keys[pygame.K_RIGHT]: #and player_x + enemy_car_img.get_width() <= WIDTH-(WIDTH/1224*375)
                angle -= rotation_speed
                
            if keys[pygame.K_UP] and player_y - HEIGHT / 10 >= 0:
                player_y -= 6
                acc_sound_me.set_volume(1)
                acc_sound_compi.set_volume(0.5)
                norm_sound_me.set_volume(0)
                norm_sound_compi.set_volume(0)
                
            else:
                acc_sound_me.set_volume(0)
                acc_sound_compi.set_volume(0)
            
            if keys[pygame.K_DOWN] and player_y + HEIGHT / 10 + player_car_img.get_height() <= HEIGHT:
                player_y += 6
                
                
                
            
            if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                if player_y < HEIGHT - HEIGHT / 5:
                    player_y += 2
                norm_sound_me.set_volume(1)
                norm_sound_compi.set_volume(1)
            
                

            
            
            player_x -= angle * 0.7
            
            if player_x <= WIDTH/1224*350 or player_x + player_car_img.get_width() >= WIDTH-(WIDTH/1224*350):
                game_over = True
         
     
           

        
        # Calculate elapsed time
        current_time = time.time() - start_time
        if int(current_time) % 1 == 0:
            score += 1/60

        background_y += speed3 + 0.01 * distance_to_bottom + 0.1*current_time

        
        
  

        elapsed_time += 1
        if int(elapsed_time) % (circle_spawn_interval * 60) == 0:
            last_circle_spawn_time = spawn_circle()
        remove_expired_circles()





        distance_to_bottom = HEIGHT - player_y / 1.4
            # Move enemy cars and spawn new ones
        for car in enemy_cars:
            car.y += (0.1*current_time) + car.speed + 0.01 * distance_to_bottom
            if car.y > HEIGHT:
                enemy_cars.remove(car)


        desired_helicopter_x = player_x
        x_position_difference = desired_helicopter_x - x_position2
        helicopter_speed = 1
        if abs(x_position_difference) > 1:
            x_position2 += helicopter_speed * (x_position_difference / abs(x_position_difference))


        y_position_difference = abs(player_y - y_position2)

        swirl_amplitude = 10
        swirl_frequency = 1.5
        swirl_offset = swirl_amplitude * math.sin(swirl_frequency * pygame.time.get_ticks() / 1000)
        x_position2_swirled = x_position2 + swirl_offset
        helicopter_speed2 = 2
        x_position_hel_car = abs(x_position2_swirled - x_position2)
        if abs(x_position2_swirled - x_position2) > 1:
            x_position2 += helicopter_speed2 * ((x_position2_swirled - x_position2) / abs(x_position2_swirled - x_position2))




        last_spawn_position = [-1 for _ in range(NUM_LANES)]  # Initialize with -1
        
        for lane in range(NUM_LANES):
            if random.randint(0, 800) < 3:
                selected_image = random.choice(scaled_enemy_car_images)
                x_position = random.choice([
                    WIDTH/1224*400 - 0.5 * selected_image.get_width(), 
                    WIDTH/1224*508 - 0.5 * selected_image.get_width(), 
                    WIDTH/1224*610 - 0.5 * selected_image.get_width(), 
                    WIDTH/1224*713 - 0.5 * selected_image.get_width(), 
                    WIDTH/1224*815 - 0.5 * selected_image.get_width()
                ])
                new_car_height = selected_image.get_height()
                new_car = Car(x_position, -new_car_height, random.randint(1, 8), selected_image)

                # Check if spawn area is clear and no recent car has been spawned in this lane
                if is_spawn_area_clear(x_position, new_car_height, enemy_cars) and \
                (last_spawn_position[lane] < 0 or last_spawn_position[lane] - new_car_height > mindistance):
                    if not will_collide(new_car, enemy_cars):
                        enemy_cars.append(new_car)
                        remove_overlapping_cars(enemy_cars)
                        last_spawn_position[lane] = new_car.y  # Update last spawn position
                    else:
                        print("Collision predicted, car not spawned.")
                else:
                    print("cant spawn")
                remove_overlapping_cars(enemy_cars)
                if remove_overlapping_cars(enemy_cars):
                    print("ddd")

        rotated_player_car = pygame.transform.rotate(player_car_img, angle)
        player_mask = pygame.mask.from_surface(rotated_player_car)
        for car in enemy_cars:
            enemy_mask = pygame.mask.from_surface(car.image)  
            offset = (car.x - player_x, car.y - player_y)
            
            if player_mask.overlap(enemy_mask, offset):
                game_over = True

        #collision check between player and car.
        
        for circle in circles:
            if not circle.explosion_triggered:
                circle_speed = 2
                distance_x = player_x + player_car_img.get_width() / 2 - circle.x
                distance_y = player_y + player_car_img.get_height() / 2 - circle.y
                angle1 = math.atan2(distance_y, distance_x)
                circle.x += circle_speed * math.cos(angle1)
                circle.y += circle_speed * math.sin(angle1)

                if circle.warning_start_time is None and elapsed_time  % circle_follow * FPS == 0:
                    circle.warning_start_time = elapsed_time
        
    
    
        # Draw car
        for car in enemy_cars:
            screen.blit(car.image, (car.x, car.y))

        rotated_rect = rotated_player_car.get_rect(center=(player_x + rotated_player_car.get_width() / 2, player_y + rotated_player_car.get_height() / 2))
        # Draw rotated player car
        screen.blit(rotated_player_car, rotated_rect)

        #Helicopter

        heli_frame_0 = pygame.image.load(os.path.join(os.path.dirname(__file__), "heli_frame_0.png")).convert_alpha()
        heli_frame_1 = pygame.image.load(os.path.join(os.path.dirname(__file__), "heli_frame_1.png")).convert_alpha()
        heli_frame_2 = pygame.image.load(os.path.join(os.path.dirname(__file__), "heli_frame_2.png")).convert_alpha()
        heli_frame_3 = pygame.image.load(os.path.join(os.path.dirname(__file__), "heli_frame_3.png")).convert_alpha()


        heli_frame_list = [heli_frame_0,
                         heli_frame_1,
                         heli_frame_2,
                         heli_frame_3,
                         ]


        rotated_helicopter = pygame.transform.rotate(heli_frame_list[elapsed_time % 4], angle)
        rotated_rect2 = rotated_helicopter.get_rect(center=(x_position2 +  rotated_helicopter.get_width() / 2, y_position2 + rotated_helicopter.get_height() / 2))
        screen.blit(rotated_helicopter, rotated_rect2)

    


        # Draw circles, To change
        # Draw circles
        for circle in circles:
            circle_x = int(circle.x - circle_img.get_width()/2)  
            circle_y = int(circle.y - circle_img.get_height()/2) 
            if circle.explosion_triggered:
                circle.explosion_y += speed3 + 0.01 * distance_to_bottom + 0.1*current_time
                collision_check_enabled = False
                
            if checkingsth == True:
                screen.blit(circle_img, (circle_x, circle_y))
            if circle.show_warning:
                collision_check_enabled = True
                circle_x = int(circle.x - warn_img.get_width()/2)
                circle_y = int(circle.y - warn_img.get_height()/2)
                screen.blit(warn_img, (circle_x, circle_y))

            # Draw the explosion circle
            
            
            if circle.explosion_triggered:
                

                 circleexplo_x = int(circle_x - explosion_img_frame1.get_width()/2)
                 
                 
                 
                 if first == 1:
                    print(circleexplo_x, circle.explosion_y)
                    explode(circleexplo_x, circle.explosion_y)            
                    first = 0
  



        score2 = int(score)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score2}", True, "WHITE")
        score_rect = score_text.get_rect(topright=(WIDTH - 10, 10))
        screen.blit(score_text, score_rect)
        pygame.display.flip()
        clock.tick(FPS)

        # Game over screen
        if game_over:
            
            explode(player_x - 70, player_y - 10)

            for i in range(50):
                print("printing")
                elapsed_time += 1
                multiplication = 0
                explosion_anim()

            font = pygame.font.Font(None, 36)
            text = font.render("Game Over!", True, BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                
            screen.blit(text, text_rect)
            pygame.display.flip()
            #quit music
            pygame.mixer.Sound.stop(heli_sound_compi)
            pygame.mixer.Sound.stop(norm_sound_compi)
            pygame.mixer.Sound.stop(acc_sound_compi)
            pygame.mixer.Sound.stop(heli_sound_me)
            pygame.mixer.Sound.stop(norm_sound_me)
            pygame.mixer.Sound.stop(acc_sound_me)
            pygame.mixer.music.fadeout(3000)
            # Wait for a few seconds before quitting
            

            pygame.time.wait(3000)  # 3000 milliseconds (3 seconds)
            pygame.quit()
            sys.exit()
            
    explosion_anim()


    #different speed for cars, 4 lanes. hallo
    #66, 50, 311. rayan to change
