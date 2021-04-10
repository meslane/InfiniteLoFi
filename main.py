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
        FileOpener.FileOpener(midiList, file)
        #print(file)

    # print(midiList)

    m = markov.markov(midiList[0], 2, 100)

    newSong = TupleToMessage(m)

    # print(newSong)

    output_song(newSong)