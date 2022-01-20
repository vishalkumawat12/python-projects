import requests
from os import system
from playsound import playsound
from gtts import gTTS
aksw='https://api.dictionaryapi.dev/api/v2/entries/en_US/'+'sleep'
ans = requests.get(aksw)
# print(ans.status_code)
# print(ans.headers['content-type'])
# print("cls")
def rules(RuleBook):

    audio = gTTS(RuleBook, lang='en', slow=False)
    audio.save("rule.mp3")
    playsound("rule.mp3")
system('cls')
a=list(ans.json())
dm=b=a[0]
a=(b['phonetics'])
b=a[0]
# print(b['audio'])
c=str(b['audio'])
print(c)
playsound(c)
tt=list(dm['meanings'])
print(tt)
dd=tt[0]
iqw=dd['definitions']
di1=iqw[0]
print(di1['definition'])
rules(di1['definition'])

