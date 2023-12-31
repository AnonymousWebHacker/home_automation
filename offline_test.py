from vosk import Model, KaldiRecognizer
import speech_recognition as sr
import pyaudio

model = Model(r"/home/jose/Documentos/ProcearAudio/vosk-model-small-es-0.42/")
recognizer = KaldiRecognizer(model, 16000) 

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        print(f"' {text[14:-3]} '")