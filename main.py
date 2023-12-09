import sounddevice as sd
import numpy as np
import time

from pynput.keyboard import Key, Controller
keyboard = Controller()

duration = 0.1
minvolume = 0.5


def print_mic_volume(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10  # Calculate volume (RMS amplitude)
    if volume_norm > minvolume:
        keyboard.press(Key.space)
    elif volume_norm <= minvolume:
        keyboard.release(Key.space)

with sd.InputStream(callback=print_mic_volume, channels=1, samplerate=44100):
    print("Monitoring microphone volume... (Press Ctrl+C to exit)")
    try:
        while True:
            time.sleep(duration)
    except KeyboardInterrupt:
        pass
