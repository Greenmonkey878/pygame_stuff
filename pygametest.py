import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('DND2D')
Clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
char_model = pygame.image.load('graphics/testcharonenobackground.png').convert_alpha()
char_x_pos = 1100
bush = pygame.image.load('graphics/bush.png').convert_alpha()
tree = pygame.image.load('graphics/tree.png').convert_alpha()
house_window = pygame.image.load('graphics/window.png').convert_alpha()
house_window_closed = pygame.image.load('graphics/closed_window.png').convert_alpha()
house_wall = pygame.image.load('graphics/house_wall.png').convert_alpha()
house_door = pygame.image.load('graphics/house_door.png').convert_alpha()
house_roof = pygame.image.load('graphics/house_roof.png').convert_alpha()

# test_surface = pygame.Surface((800width, 800height))
# test_surface.fill('green')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 700))
        screen.blit(house_wall, (175, 500))
        screen.blit(house_roof, (175,575))
        screen.blit(house_door, (150,575))
        screen.blit(house_roof, (200, 450))
        screen.blit(house_window_closed, (175, 450))
        screen.blit(house_window, (250,575))
        screen.blit(tree, (700, 575))
        screen.blit(bush, (500, 600))
        char_x_pos -= 5
        if char_x_pos < -100:
            char_x_pos = 1100
        screen.blit(char_model, (char_x_pos, 510))



# rectangles for collision.

    # draw elements
    # update stuff
    pygame.display.update()
    Clock.tick(60)
