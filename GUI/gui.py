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
    # build white keys
    for i in range(num_white_keys):
        curr_white_key_X = 50
        curr_white_key_Y = screen_height - 150
        curr_white_key = pygame.Rect(curr_white_key_X, curr_white_key_Y, white_key_width, white_key_height)
        curr_white_key_X += white_key_width
        pygame.draw.rect(screen, (255, 255, 255), curr_white_key)

    pygame.draw.rect(screen, (0, 0, 0), (350, 200, 100, 50))

    pygame.display.update()
