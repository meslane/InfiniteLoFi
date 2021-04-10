import mido
import time
import math

def output_song(newSong, mpb, tpb): #microseconds per beat, ticks per beat

    try:
        with mido.open_output() as outport:
            #print(note)
            looptime = time.time()
            s = 0
            i = 0
            ticks = 0
            while i < len(newSong):
                if (time.time() - looptime > 0.001):
                        looptime = time.time()
                        s += 0.001
                        #print(ms)
                        
                ticks = math.floor(s * (1000000/(mpb/tpb)))
                #print(ticks)
                        
                if ticks >= newSong[i].time:
                    print(newSong[i])
                    outport.send(newSong[i])
                    i += 1
                    ticks = 0
                    s = 0
                    
        outport.close()

    except:
        print("you are on a mac u loser")