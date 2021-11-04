#--------------------------------------#to import ------------(text)
import googletrans
#import pyttsx3
import speech_recognition as sr
import gtts
import pygame
import os
#-------------------------------------#setup----------------------
gts = googletrans.Translator()
#speaker = pyttsx3.init()
pygame.mixer.init()

#-------------------------------------1. setup function---------------------

def listen_recording():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Recording...')
        audio = r.listen(source)
    try:
        unknown_text = (r.recognize_google(audio))
        translate(unknown_text)
    except sr.UnknownValueError:
        print('Unknown Error')

def translate(message):
    lang = input("what lang do u want to translate")
    speak(message, lang)

def speak(message, input_lang):
    print(input_lang)
    output = gts.translate(message, dest=input_lang)
    print(output.text)
    translated_message = output.text
    tts = gtts.gTTS(translated_message, lang=input_lang, slow=True)
    pygame.mixer.music.unload()
    os.remove('audio.mp3')
    filename = 'audio.mp3'
    tts.save(filename)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # print(lang)
    # print(output.origin)
    # print(output.text)
    # speaker.say(output.text)
    # speaker.runAndWait()

talk = True

while talk is True:
    listen_recording()
    ans = input("enter Y if you want to leave").lower()
    if ans == "y":
        break

#print(gtts.lang.tts_langs())
#https://gtts.readthedocs.io/en/latest/module.html