import pygame
from pygame import RESIZABLE

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
pygame.display.set_caption("Infinite LoFi Generator")

#initialize white key sizes
num_white_keys = 52
white_key_height = 100
white_key_width = (screen_width-100)/52 - 2

def draw_buttons():
    pygame.draw.rect(screen, (0, 0, 0), (198, 423, 104, 55), border_radius=3)
    pygame.draw.rect(screen, (211, 211, 211), (200, 425, 100, 50), border_radius=3)
    play = pygame.font.SysFont('Raleway Bold', 40)
    textsurface = play.render('PLAY', True, (128,128,0))
    screen.blit(textsurface,(215,438))
    pygame.draw.rect(screen, (0, 0, 0), (498, 423, 104, 55), border_radius=3)
    pygame.draw.rect(screen, (211, 211, 211), (500, 425, 100, 50), border_radius=3)
    quit = pygame.font.SysFont('Raleway Bold', 40)
    textsurface = play.render('QUIT', True, (128,0,0))
    screen.blit(textsurface,(515,438))

    welcome_msg = pygame.font.SysFont('Raleway Bold', 65)
    textsurface = play.render('Infinite LoFi Music Generator', True, (0, 0, 0))
    screen.blit(textsurface, (202, 525))
    
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()



    screen.fill((128, 128, 128))
    draw_buttons()
    # build white keys
    for i in range(num_white_keys):
        curr_white_key_X = 50
        curr_white_key_Y = screen_height - 150
        curr_white_key = pygame.Rect(curr_white_key_X, curr_white_key_Y, white_key_width, white_key_height)
        curr_white_key_X += white_key_width
        pygame.draw.rect(screen, (255, 255, 255), curr_white_key)

    pygame.draw.rect(screen, (0, 0, 0), (350, 200, 100, 50))

    pygame.display.update()
