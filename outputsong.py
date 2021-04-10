import mido
import time

def output_song(newSong):

    try:
        with mido.open_output() as outport:
            for note in newSong:
                print(note)
                outport.send(note)
        outport.close()

    except:
        print("you are on a mac u loser")