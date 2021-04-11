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

def draw_buttons(curr_width, curr_height):
    button_width = curr_width / 8
    button_height = curr_height / 12

    pygame.draw.rect(screen, (0, 0, 0), ((curr_width / 4) - 2, ((curr_height * 4) / 6) - 2, button_width + 4, button_height + 5), border_radius=3)
    pygame.draw.rect(screen, (211, 211, 211), (curr_width / 4, (curr_height * 4) / 6, button_width, button_height), border_radius=3)
    play = pygame.font.SysFont('Raleway Bold', 40)
    textsurface = play.render('PLAY', True, (128,128,0))
    screen.blit(textsurface,((screen_width / 4 ) +  15, screen_height - 200 + 12))
    pygame.draw.rect(screen, (0, 0, 0), (((5 * curr_width) / 8) - 2, ((curr_height * 4) / 6) - 2, button_width + 4, button_height + 5), border_radius=3)
    pygame.draw.rect(screen, (211, 211, 211), ((5 * curr_width) / 8, (curr_height * 4) / 6, button_width, button_height), border_radius=3)
    quit = pygame.font.SysFont('Raleway Bold', 40)
    textsurface = play.render('QUIT', True, (128,0,0))
    screen.blit(textsurface,((screen_height - 100) +  15, screen_height - 200 + 12))

    welcome_msg = pygame.font.SysFont('Raleway Bold', 65)
    textsurface = play.render('Infinite LoFi Music Generator', True, (0, 0, 0))
    screen.blit(textsurface, (202, 525))
    
def play_or_quit(position):
    if (position[0] >= 200 and position[0] <= 300) and (position[1] >= 400 and position[1] <= 445):
        # call the play music button:
        print("have to implement")
    elif (position[0] >= 500 and position[0] <= 600) and (position[1] >= 400 and position[1] <= 445):
        exit()
 
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
            play_or_quit(pos)



    screen.fill((128, 128, 128))
    curr_width = screen.get_width()
    curr_height = screen.get_height()
    draw_buttons(curr_width, curr_height)
    # build white keys
    for i in range(num_white_keys):
        curr_white_key_X = 50
        curr_white_key_Y = screen_height - 150
        curr_white_key = pygame.Rect(curr_white_key_X, curr_white_key_Y, white_key_width, white_key_height)
        curr_white_key_X += white_key_width
        pygame.draw.rect(screen, (255, 255, 255), curr_white_key)

    pygame.draw.rect(screen, (0, 0, 0), (350, 200, 100, 50))

    pygame.display.update()
