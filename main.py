import mido
from pathlib import Path

import FileOpener
import markov
from InfiniteLoFi.TupleToMessage import TupleToMessage


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
        
    m = markov.markov(midiList[0], 2, 100)

    print(m)

    newSong = TupleToMessage(m)

    # i = 1
    # for section in newSong:
    #     print(i)
    #     i += 1
    #     print(section)
