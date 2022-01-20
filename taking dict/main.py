import speech_recognition as sr
# from mpyg321.mpyg321 import MPyg321Player
from playsound import playsound
import os
from gtts import gTTS
import requests


def ask():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
        r.pause_threshold = 1
        print(audio)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            # r.energy_threshold=-1
            print(f"User said: {query}\n")
            
        except Exception as e:
            # print(e)
            print("Say that again please...")
            return

    return query


def rules():
    RuleBook = "if you want to quit then say exit and now lets use this dicsnary"
    audio = gTTS(RuleBook, lang='en', slow=False)
    audio.save("rule.mp3")
    playsound("rule.mp3")


if __name__ == "__main__":
    mydict = {"apple":
              "a frout"}
    # rules()
    on = True

    Query = ask().lower()
    if Query in mydict.keys():
        print(type(Query))
        find1='https://api.dictionaryapi.dev/api/v2/entries/en_US/'+'dog'
        ans = requests.get(find1)
        print(ans.status_code)
        print(ans.json)
