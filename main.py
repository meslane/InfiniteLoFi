import mido
from pathlib import Path

import FileOpener
import markov
from TupleToMessage import TupleToMessage
from outputsong import output_song
from key import piano

def main():
    print("hello Casey")
    
if __name__ == "__main__":
    main()
    piano = piano()

    midiList = []
    directory = 'MIDI'

    files = Path(directory).glob('*')
    for file in files:
        timing = FileOpener.FileOpener(midiList, file)
        #print(file)

    finalList = []

    # for track in midiList:
    #     finalList += track
    #
    # print(len(finalList))
    #
    # print(timing[0], timing[1])
    #
    # while True:
    #     m = markov.markov(finalList, 2, 500)
    #     newSong = TupleToMessage(m)
    #     output_song(newSong, timing[0], timing[1])
    #     print("song over")