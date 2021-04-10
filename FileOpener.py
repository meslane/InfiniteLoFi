# Created by Aditya Kumar and Casey Kwinn
# Date: April 10, 2021

import mido
#import struct
from mido import MidiFile

def FileOpener (midiList, filename):

    mid = MidiFile(filename)
    p = mido.Parser()
    temp = []

    for i, track in enumerate(mid.tracks):
        #print('Track {}: {}'.format(i, track))
        for msg in track:
            if not msg.is_meta:
                #print(msg)
                temp.append(msg)

    midiList.append(temp)

    return;