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

    files = Path(directory).glob('*')
    for file in files:
        timing = FileOpener.FileOpener(midiList, file)
        #print(file)
    
    finalList = []
    
    for track in midiList:
        finalList += track

    m = markov.markov(finalList, 3, 10000)

    newSong = TupleToMessage(m)

    # print(newSong)
    
    print(timing[0], timing[1])

    output_song(newSong, timing[0], timing[1])