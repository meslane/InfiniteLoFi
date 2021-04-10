import mido
from pathlib import Path

import FileOpener
import markov
from TupleToMessage import TupleToMessage
from outputsong import output_song

def main():
    print("hello Casey")
    
if __name__ == "__main__":
    main()

    midiList = []
    directory = 'MIDI'
    clocks = 0

    
    files = Path(directory).glob('*')
    for file in files:
        clocks = FileOpener.FileOpener(midiList, file)
        #print(file)
    
    #clocks = FileOpener.FileOpener(midiList, "Fugue1.mid")
    
    print(clocks)

    # print(midiList)
    
    finalList = []
    
    for track in midiList:
        finalList += track

    m = markov.markov(finalList, 3, 10000)

    newSong = TupleToMessage(m)

    # print(newSong)

    output_song(newSong, 800000, clocks)