import music21 as m21
import pretty_midi
import matplotlib.pyplot as plt
import pandas as pd

#コーパスの利用
piece = m21.corpus.parse("mozart/k545/movement1_exposition.xml")

# 楽譜表示（musescoreやFinaleなどがインストールされていないと動かない、）
piece.show()

x = None

for m in piece[2].getElementsByClass('Measure'):
    for p in m.pitches:
        if p.name == 'F#':
            x = m.measureNumber
            print(m.measureNumber)
piece[2][x+2].show()#なんで？