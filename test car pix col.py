import pygame
import random
import sys
import os
import math

pygame.init()

#define screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 1000

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Masks")

#define colours
BG = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

#create car 
soldier = pygame.image.load("player_car.png").convert_alpha()
soldier_rect = soldier.get_rect()
soldier_mask = pygame.mask.from_surface(soldier)
mask_image = soldier_mask.to_surface()

#game loop
run = True
while run:

  #update background
  screen.fill(BG)
  
  screen.blit(mask_image, (0,0))

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  #update display
  pygame.display.flip()

pygame.quit()