import mido
from mido import MidiFile

def TupleToMessage ( m ):


    final = []

    for tuple in m:
        temp = list(tuple)
        temp2 = mido.Message.from_bytes(temp[0:3])
        temp2.time = temp[3]
        final.append(temp2)


    return final;
