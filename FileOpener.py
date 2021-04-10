# Created Aditya Kumar and Casey Kwinn
# Date: April 10, 2021

import mido
#import struct
from mido import MidiFile

def FileOpener (midiList, filename):

    mid = MidiFile(filename)
    p = mido.Parser()
    temp = []
    cpc = 0

    for i, track in enumerate(mid.tracks):
        #print('Track {}: {}'.format(i, track))
        for msg in track:
            if not msg.is_meta:
                print(msg)
                temp2 = msg.bytes()
                temp2.append(msg.time)
                temp.append(tuple(temp2))
            else:
                if msg.type == "time_signature":
                    cpc = msg.clocks_per_click

    midiList.append(temp)

    return cpc