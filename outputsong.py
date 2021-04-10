import mido

def output_song(newSong):
    
    outport = mido.open_output(mido.get_output_names()[0])
    print(outport)

    with mido.open_output(mido.get_output_names()[0]) as outport:
        for note in newSong:
            print(note)
    outport.close()