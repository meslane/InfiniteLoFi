import mido
from pathlib import Path

from InfiniteLoFi.FileOpener import FileOpener


def main():
    print("hello Casey")
    
if __name__ == "__main__":
    main()

    midiList = []
    directory = 'MIDI'

    files = Path(directory).glob('*')
    for file in files:
        FileOpener(midiList, file)
        #print(file)

    # i = 1
    # for section in midiList:
    #   print(i)
    #   i += 1
    #   for note in section:
    #       print(note)
