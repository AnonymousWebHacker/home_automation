import speech_recognition as sr
import subprocess
proceso = None
saludos = """
hola hola
"""

from gtts import gTTS
def speak(text):
  tts = gTTS(text=text, lang="en")
  filename = "voice.mp3"
  tts.save(filename)

import playsound
def play(filename):
  playsound.playsound(filename)

  
def ejecutar_comando(comando):
    global proceso
    if "abrir terminal" in comando:
        proceso = subprocess.Popen(["tilix"])
    elif "saludar" in comando:
        print("Estas Saludando")
    elif "cerrar terminal" in comando:
        proceso.terminate()
    elif "abrir firefox" in comando:
        proceso = subprocess.Popen(["firefox"])

# Obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("En que puedo ayudarle?")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

# recognize speech using Google
try:
    #print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    print("Detecto que dice: " + r.recognize_google(audio, language="es-ES"))
    comando = r.recognize_google(audio, language="es-ES")
    ejecutar_comando(comando)

except sr.UnknownValueError:
    print("No reconozco el comando")
except sr.RequestError as e:
    print("Error al hacer tarea; {0}".format(e))

while True:
    ejecutar_comando()