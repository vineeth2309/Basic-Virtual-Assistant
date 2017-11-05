import wolframalpha
import wikipedia
from tkinter import *
#from gtts import gTTS
import pyttsx
import speech_recognition as sr
from pygame import mixer
import string
import time
#from newsapi.sources import Sources

#SPEEH TO TEXT ENGINE
r = sr.Recognizer()
m = sr.Microphone()

def checkspeech(r):
    with sr.Microphone() as source:

        audio = r.listen(source)
        try:
            print("You said: " + r.recognize_google(audio))
            return (r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ("WW")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ("WW")
####

#TEXT TO SPEECH ENGINE
engine=pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-25)
engine.say('Hello')
engine.say('Greetings')    
engine.runAndWait()
####
win=Tk()

#LABEL
l=Label(win,text="How may I help you?")
#l.grid(row=0,column=0)
l.pack(side=LEFT)
###

#TEXTBOX
v=StringVar()
e=Entry(win,textvariable=v)
#e.grid(row=1,column=0)
e.pack()
###

    
#BUTTON
b1=Button(win,text="Enter")
#b1.grid(row=2,column=0)
b1.pack(side=RIGHT)
####


#BUTTON PRESS OR ENTER EVENT
def button1press() :
    input1=v.get()
    print(input1)
    wolramalpha(input1)
###

#WOLFRAM ALPHA  AND WIKIPEDIA FUNCTIONS CALL    
def wolframalphacall(input1):
        #WOLFRAMALPHA
        
        app_id=''
        client = wolframalpha.Client(app_id)
        res=client.query(input1)
        #for pod in res.pods:
            #print(pod.text)
        answerwolfram=(next(res.results).text)     
        print('WOLFRAM')
        print(answerwolfram)
        engine.say(answerwolfram)
        engine.runAndWait()
        mixer.init()
        mixer.music.load('chime2.mp3')
        mixer.music.play()

        print('DONE')
###
def wikicall(input1) :
        #WIKIPEDIA
        answerwiki=wikipedia.summary(input1,sentences=2)
        print('WIKI')
        print (answerwiki)
        engine.say(answerwiki)
        engine.runAndWait()
        mixer.init()
        mixer.music.load('chime2.mp3')
        mixer.music.play()
        print('DONE')

def musicplay(input1):
    mixer.init()
    #path1='F:\\Music\\'
    #path2=input1
    #path3='.mp3'
    #path=path1+path2+path3
    mixer.music.load('F:\\Music\\'+input1+'.mp3')
    mixer.music.play()

#MICROPHONE RUNNING
while True:
    
    
    #s.get(category='sports',language='en',country='uk')
    r.pause_threshold = 0.7
    r.energy_threshold = 2200
    with m as source:
        #r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
    print("MICROPHONE")
    speech=str(checkspeech(r))
    speech3=speech.split(' ',1)[0]
    if (speech3=="Alexa"):
        mixer.init()
        mixer.music.load('chime1.mp3')
        mixer.music.play()
        print("\n\nListening")
        speechrequest=str(checkspeech(r))
        speech1=speechrequest.split(' ')
        speech2=speechrequest.split(' ',1)[0]
        speech1=" ".join(speech1[1:])
        speech1=string.capwords(speech1)
        #speech2=string.capwords(speech2)
        #print("This is speech1: "+speech1)
        #print('This is speech2: '+speech2)

        
        if(speechrequest=="what is the time"):
           engine.say(time.ctime())
           engine.runAndWait()
        if (speech2=='Wiki'):
            wikicall(speech1)
        elif (speech2=='Wolfram'):
            wolframalphacall(speech1)
        elif (speech2=='Play'):
            musicplay(speech1)
        elif (speech2=='Google'):
            q=pypygo.query(speech1)
            q=q.abstract
            print(q)
            engine.say(q)
            engine.runAndWait()
    
###

b1.configure(command=button1press)

win.mainloop()

    ###




