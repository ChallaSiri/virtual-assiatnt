from gtts import gTTS
import speech_recognition as sr
import os
import playsound
"""speech=gTTS('Hey how are you',lang='en-IN')
speech.save('hey.mp3')"""
# to make sure it listens
def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("i am listening")
        audio=r.listen(source,phrase_time_limit=5)
    data=""
#exception handling
    try:
        data=r.recognize_google(audio,language='en-US')
        print("you said:"+data)
    except sr.UnknownValueError:
        print("I CANNOT HEAR YOU")
    except sr.RequestError as e:
        print("Request failed")
    return data
#listen()
#responding
def respond(String):
    print(String)
    tts=gTTS(text=String,lang='en')
    tts.save('speech.mp3')
    playsound.playsound('speech.mp3')
    os.remove('speech.mp3')

#virtual assistant actions

def voice_assistant(data):
    """ giving your actions"""
    if "how are you" in data:
        listening=True
        respond("Good and doing well")
respond("Hey siri how are you ?")
listening=True
while listening==True:
    data=listen()
    listening=voice_assistant(data)
    

