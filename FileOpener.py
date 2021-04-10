# Created by Aditya Kumar and Casey Kwinn
# Date: April 10, 2021

import mido
import struct
from mido import MidiFile

def FileOpener (midiList, filename):

    mid = MidiFile(filename)
    p = mido.Parser()

    for i, track in enumerate(mid.tracks):
        #print('Track {}: {}'.format(i, track))
        for msg in track:
            #print(msg)
            midiList.append(msg)
            pass

    return;
        #midiList;
