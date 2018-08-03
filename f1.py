from pathlib import Path
import numpy, scipy, matplotlib.pyplot as plt, sklearn, urllib, IPython.display as ipd
import librosa, librosa.display

c1_signals = []
counter=1
for p in Path().glob('audio/train/c1/*.mp3'):
    counter=counter+1
    if counter > 10:
        break
    else:
        y, sr = librosa.load(p, duration=30, offset=10)
        c1_signals.append(y[0])
