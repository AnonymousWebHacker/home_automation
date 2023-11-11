import speech_recognition as sr
import subprocess
import pyautogui

recognizer =  sr.Recognizer()
proceso = None
saludos = """
HOla mundo
"""

def ejecutar_comando(comando):
    global proceso
    if "abrir notepad" in comando:
        proceso = subprocess.Popen(["notepad.exe"])
    elif "saludar" in comando:
        pyautogui.write(saludo)
    elif "cerrar notepad" in comando:
        proceso.terminate()


def escuchar_comandos():
    with sr.Microphone() as source: 
        print("En que te puedo ayudar.")
        recognizer.adjust_for_ambient_noise(source)
        audio =  recognizer.listen(source)
try:
    comando = recognizer.recognize_google(audio, language="es-ES")
    print(f"Comando reconocido: {comando}")
    ejecutar_comando(comando)

except sr.UnknownValueError:
    print("No reconozco el comando")
except sr.RequestError as e:
    print(f"Error al hacer tarea: {e}")

while True:
    escuchar_comandos()