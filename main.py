import mido
from pathlib import Path
import time
import math
import pygame

import FileOpener
import markov
from TupleToMessage import TupleToMessage
from outputsong import output_song
import key

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
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
    play = pygame.font.SysFont('Raleway Bold', int(curr_height / 15))
    textsurface = play.render('PLAY', True, (128,128,0))
    screen.blit(textsurface,((curr_width / 4 * 215) / 200,(((curr_height * 4) / 6) * 415) / 400))
    pygame.draw.rect(screen, (0, 0, 0), (((5 * curr_width) / 8) - 2, ((curr_height * 4) / 6) - 2, button_width + 4, button_height + 5), border_radius=3)
    pygame.draw.rect(screen, (211, 211, 211), ((5 * curr_width) / 8, (curr_height * 4) / 6, button_width, button_height), border_radius=3)
    textsurface = play.render('QUIT', True, (128,0,0))
    screen.blit(textsurface,((curr_width / 4 * 515) / 200, (((curr_height * 4) / 6) * 415) / 400))
    welcome_msg = pygame.font.SysFont('Raleway Bold', int(curr_height / 8 ))
    textsurface = play.render('Infinite LoFi Music Generator', True, (0, 0, 0))
    screen.blit(textsurface, ((curr_width / 4) + (screen_width / 100), (((curr_height * 4) / 6) * 505) / 400))

def play_or_quit(position):
    if (position[0] >= 200 and position[0] <= 300) and (position[1] >= 400 and position[1] <= 445):
        # call the play music button:
        print("have to implement")
    elif (position[0] >= 500 and position[0] <= 600) and (position[1] >= 400 and position[1] <= 445):
        exit()

def main():
    pygame.init()
    piano = key.piano()

    midiList = []
    directory = 'Bach'

    files = Path(directory).glob('*')
    for file in files:
        timing = FileOpener.FileOpener(midiList, file)
        #print(file)

    finalList = []
    
    for track in midiList:
        finalList += track
    
    print(len(finalList))
    
    print(timing[0], timing[1])
    
    outport = mido.open_output()
    
    #m = markov.markov(finalList, 2, 500)
    newSong = []
    
    looptime = time.time()
    s = 0
    i = 0
    delta = 0
    
    piano = key.piano()
    piano.build(screen)
    
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
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, curr_width, curr_height / 4))
        piano.draw(screen)

        pygame.display.update()
    
        if i >= len(newSong):
            print("song over")
            for i in range(0,88):
                piano.release(i)
            
            m = markov.markov(finalList, 2, 100)
            newSong = TupleToMessage(m)
            i = 0 
            s = 0
            delta = 0
            looptime = time.time()
        
        if (time.time() - looptime > 0.001):
            looptime = time.time()
            s += 0.001

        delta = math.floor(s * (1000000/(timing[0]/timing[1])))

        if delta >= newSong[i].time:
            print(newSong[i])
            if (newSong[i].type == 'note_on'):
                piano.press(newSong[i].note - 21)
            elif (newSong[i].type == 'note_off'):
                piano.release(newSong[i].note - 21)
            
            outport.send(newSong[i])
            i += 1
            delta = 0
            s = 0
        
        #output_song(newSong, timing[0], timing[1])
       
if __name__ == "__main__":
    main()