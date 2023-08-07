import openai
import speech_recognition as sr
import pyttsx3

import os

from dotenv import load_dotenv
load_dotenv()

# OPENAI_KEY = os.getenv('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')

openai.api_key = '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'


def SpeakText(command):

    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


r = sr.Recognizer()


def record_text():
    while (1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)

                print("I'm Listeninig.......")

                audio2 = r.listen(source2)

                MyText = r.recognize_google(audio2)
                return MyText
        except sr.RequestError as e:
            print("Could not request results: {0}".format(e))

        except sr.UnknownValueError:
            print("Unknown Error Occurred")

def send_to_chatGPT(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temprature=0.5,
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message

messages = []
while(1): 
    text = record_text()
    messages.append({"role":"user","content":text})
    reponse = send_to_chatGPT(messages)
    SpeakText(reponse)
    print(reponse)