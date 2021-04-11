import mido
from pathlib import Path
import time
import math

import FileOpener
import markov
from TupleToMessage import TupleToMessage
from outputsong import output_song
import key

def main():
    piano = key.piano()

    midiList = []
    directory = 'MIDI'

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
    
    while True:
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
            outport.send(newSong[i])
            i += 1
            delta = 0
            s = 0
        
        #output_song(newSong, timing[0], timing[1])
       
if __name__ == "__main__":
    main()