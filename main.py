import mido
from pathlib import Path

import FileOpener
import markov


def main():
    midiList = []
    directory = 'MIDI'

    files = Path(directory).glob('*')
    for file in files:
        FileOpener.FileOpener(midiList, file)
        
    print(midiList)
        
    output = markov.markov(midiList, 2, 100)
    
    print(output)

    print("hello Casey")
    
if __name__ == "__main__":
    main()