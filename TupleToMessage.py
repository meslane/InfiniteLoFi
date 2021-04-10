import mido
from mido import MidiFile

def TupleToMessage ( m ):


    final = []

    for tuple in m:
        temp = list(tuple)
        final.append(mido.Message.from_bytes(temp))

    return final;
