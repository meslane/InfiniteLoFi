# Created Aditya Kumar and Casey Kwinn
# Date: April 10, 2021

import mido
#import struct
from mido import MidiFile

def FileOpener (midiList, filename):

    mid = MidiFile(filename)
    p = mido.Parser()
    temp = []
    
    ticksPerBeat = mid.ticks_per_beat
    clocksPerClick = 0
    
    for i, track in enumerate(mid.tracks):
        #print('Track {}: {}'.format(i, track))
        for msg in track:
            if not msg.is_meta:
                #print(msg)
                temp2 = msg.bytes()
                temp2.append(msg.time)
                temp.append(tuple(temp2))
            elif (msg.type == "set_tempo"):
               pass 

    midiList.append(temp)

    return ticksPerBeat