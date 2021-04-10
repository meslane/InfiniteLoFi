import mido
from mido import MidiFile

def TupleToMessage ( m ):
    final = []

    for tuple in m:
        temp = list(tuple)
        try:
            temp2 = mido.Message.from_bytes(temp[0:3])
        except ValueError:
            temp2 = mido.Message.from_bytes(temp[0:-1])
            
        try:
            temp2.time = temp[3]
        except:
            temp2.time = temp[-1]
            
        final.append(temp2)


    return final;
