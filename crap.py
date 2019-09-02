import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

    fs=44100
    duration = 5  # seconds
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float64')
    print("Recording Audio")
    sd.wait()
print("Audio recording complete , Play Audio")
sd.play(myrecording, fs)
sd.wait()
print("Play Audio Complete")

# import os
# from pocketsphinx import LiveSpeech, get_model_path
#
# model_path = get_model_path()
#
# speech = LiveSpeech(
#     verbose=False,
#     sampling_rate=16000,
#     buffer_size=2048,
#     no_search=False,
#     full_utt=False,
#     hmm=os.path.join(model_path, 'en-us'),
#     lm=os.path.join(model_path, 'en-us.lm.bin'),
#     dic=os.path.join(model_path, 'cmudict-en-us.dict')
# )
#
# for phrase in speech:
#     print(phrase)