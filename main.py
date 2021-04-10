import mido
from pathlib import Path

import FileOpener
import markov

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

    # i = 1
    # for section in midiList:
    #   print(i)
    #   i += 1
    #   for note in section:
    #       print(note)
