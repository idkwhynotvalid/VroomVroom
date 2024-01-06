import pygame
import os

def rotate(circle_img, rect, angle):
    """Rotate the image while keeping its center."""
    new_circle_img = pygame.transform.rotate(circle_img, angle)
    rect = new_circle_img.get_rect(center=rect.center)
    return new_circle_img, rect

def initialize():
    pygame.init()
    return pygame.display.set_mode((640, 480)), pygame.Color('gray15')

def main():
    clock = pygame.time.Clock()
    screen, gray = initialize()

    circle_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "warning.png")).convert_alpha()
    orig_circle_img = circle_img

    rect = circle_img.get_rect(center=(94, 94))
    angle = 0

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        angle += 2
        rotated_circle_img, rect = rotate(orig_circle_img, rect, angle)

        screen.fill(gray)
        screen.blit(rotated_circle_img, rect)
        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
    pygame.quit()
