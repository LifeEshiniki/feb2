import music21 as m21
import pretty_midi
import matplotlib.pyplot as plt
import pandas as pd

#コーパスの利用
piece = m21.converter.parse("C:/Users/match/PycharmProjects/feb2/senbon.mid")


sabi_piece = piece[0].measures(38,45)
sabi_piece.plot("histogram","pitchclass")

print(sabi_piece.analyze("key"))