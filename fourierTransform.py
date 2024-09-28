import pyaudio
import numpy as np
from scipy.fftpack import fft

import matplotlib.pyplot as plt

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

plt.ion()
fig, ax = plt.subplots()
x = np.arange(0, 2 * CHUNK, 2)
line, = ax.plot(x, np.random.rand(CHUNK))

ax.set_ylim(0, 70)
ax.set_xlim(0, CHUNK)

while True:
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    yf = fft(data)
    ydata = np.abs(yf[0:CHUNK])  / (128 * CHUNK)
    line.set_ydata(ydata)
    fig.canvas.draw()
    fig.canvas.flush_events()

stream.stop_stream()
stream.close()
p.terminate()