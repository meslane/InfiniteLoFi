import mido
import time
import math

def output_song(newSong, tempo, ppq):
    with mido.open_output() as outport:
        #print(note)
        looptime = time.time()
        s = 0
        i = 0
        delta = 0
        while i < len(newSong):
            if (time.time() - looptime > 0.001):
                looptime = time.time()
                s += 0.001
                #print(ms)

            delta = math.floor(s * (1000000/(tempo/ppq)))
            #print(delta)

            if delta >= newSong[i].time:
                print(newSong[i])
                outport.send(newSong[i])
                i += 1
                delta = 0
                s = 0
                
        outport.close()