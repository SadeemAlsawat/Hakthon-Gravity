import json
import speech_recognition as sr
import pyttsx3
#import pyautogui
#import pyperclip
from tkinter import *
import tkinter.font as font

# Load data from JSON file
def load_data(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

# Convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Initialize the speech recognizer
r = sr.Recognizer()

# Load data from JSON file
data = load_data('C:/Users/AEliP/Downloads/intents.json')
intents = data['intents']

def speak(text):
    engine = pyttsx3.init()
    voice_id = "english"  
    engine.setProperty('voice', voice_id)
    engine.setProperty('rate', 150)  
    engine.setProperty('volume', 1)  
    engine.say(text)
    engine.runAndWait()

def Talk():
    recognizer = sr.Recognizer()
    text = ""
    if len(text) == 0:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio, language="en-EN")
                print("Recognized: {}".format(text))

                if  "problem" in text:
                    steps = "what do you feel?"
                    print(steps)
                    speak(steps)
                    text = ""

        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            text = ""
        
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.6)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio, language="en-EN")
                print("Recognized: {}".format(text))

                for intent in intents:
                    if  intent['tag'].lower() in text.lower():
                        print("tag: "+ intent['tag'])
                        responses = intent['responses']
                        steps = "what do you feel?"
                        print(responses)
                        speak(responses)
                        text = ""

        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            text = ""



# Create a tkinter window
root = Tk()
root.title('Awa')
root.geometry('600x400')

myFont = font.Font(size=20)
title_font = font.Font(size=16, weight="bold")

text = Label(text="Press to talk to the bot")
text.place(relx=0.5, rely=0.2, anchor=CENTER)
text['font'] = title_font

btn = Button(root, text='Talk', bd='5', bg='green', activebackground='red', fg='white', command=Talk)
btn['font'] = myFont
btn.place(relx=0.5, rely=0.6, anchor=CENTER)
root.mainloop()