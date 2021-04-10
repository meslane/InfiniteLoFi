import mido
import time
import math

def output_song(newSong, clocksPerClick):

    try:
        with mido.open_output() as outport:
            #print(note)
            looptime = time.time()
            ms = 0
            i = 0
            delta = 0
            while i < len(newSong):
                if (time.time() - looptime > 0.001):
                        looptime = time.time()
                        ms += 0.001
                        #print(ms)
                        
                delta = math.floor((ms * 500))
                #print(delta)
                        
                if delta >= newSong[i].time:
                    print(newSong[i])
                    outport.send(newSong[i])
                    i += 1
                    delta = 0
                    ms = 0
                    
        outport.close()

    except:
        print("you are on a mac u loser")