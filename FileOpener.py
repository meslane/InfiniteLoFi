# Created Aditya Kumar and Casey Kwinn
# Date: April 10, 2021

import mido
#import struct
from mido import MidiFile

def FileOpener (midiList, filename):

    mid = MidiFile(filename)
    #temporary list to hold each note
    temp = []

    #gets the rate at which each note is played
    ticksPerBeat = mid.ticks_per_beat
    tempolist = []
    tempo = 500000

    #iterates through each line of the MIDI file
    for i, track in enumerate(mid.tracks):
        #print('Track {}: {}'.format(i, track))
        #separates each line into those with and without meta data
        for msg in track:
            #if the line does not have meat data, then the data i converted to byte form and stored
            if not msg.is_meta:
                #print(msg)
                temp2 = msg.bytes()

                #the time is not stored when converted into byte form so it is added to the tuple later
                temp2.append(msg.time)
                temp.append(tuple(temp2))

            #retrieves the tempo of the song
            elif (msg.type == "set_tempo"):
                tempolist.append(msg.tempo)

    #adds the temp list into a list of notes
    midiList.append(temp)

    #calculates the tempo
    if tempolist:
        tempo = sum(tempolist)/len(tempolist)

    return (tempo, ticksPerBeat)