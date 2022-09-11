import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import ssl
import certifi
import time
import os # to remove created audio files
from PIL import Image
import subprocess
import pyautogui #screenshot
import pyttsx3
import bs4 as bs
import urllib.request
import requests

class person:
    name = ''
    def setName(self, name):
        self.name = name

class rachel:
    name = ''
    def setName(self, name):
        self.name = name



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
x=False
def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            engine_speak('Sorry,I did not get that')
            x=True
        except sr.RequestError:
            engine_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(rachel_obj.name + ":", audio_string) # print what app said
    os.remove(audio_file) # remove audio file

def respond(voice_data):
    # 1: greeting
    x=False
    if there_exists(['hey','hi','hello','holla']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)
        x=True

    # 2: name

    if there_exists(["what is your name","what's your name","tell me your name"]):

        if person_obj.name:
            engine_speak(f"My name is {rachel_obj.name}, {person_obj.name}") #gets users name from voice input
        else:
            engine_speak(f"My name is {rachel_obj.name}. But I see, you have not provided your name, So kindly tell me your name ") #incase you haven't provided your name.
            # engine_speak(f"So Please your name in the text box")
            # person_obj.name=input("please enter your name")
            # person_name = voice_data.split("is")[-1].strip()
            # engine_speak("okay, i will remember that " + person_obj.name)
            # person_obj.setName(person_name)
            
            # engine_speak("okay, i will remember that " + person_obj.name)
        x=True

    if there_exists(["my name is"]):
        if(person_obj.name):
            engine_speak("Your name is " + person_obj.name)
        
        else:
            person_name = voice_data.split("is")[-1].strip()
            engine_speak("okay, i will remember that " + person_name)
            person_obj.setName(person_name) # remember name in person object
        x=True
    
    if there_exists(["what is my name","what's my name"]):
        engine_speak("Your name must be " + person_obj.name)
        x=True
    
    if there_exists(["change your name to", "change name to"]):
        rachel_name = voice_data.split("to")[-1].strip()
        engine_speak("okay, i will remember that my name is " + rachel_name)
        rachel_obj.setName(rachel_name) # remember name in rachel object
        x=True
    if there_exists(["change my name to", "change my name to"]):
        person_obj.name = voice_data.split("to")[-1].strip()
        engine_speak("okay, i will remember that your name is " + rachel_name)
        person_obj.setName(person_name) # remember name in rachel object
        x=True

    # 3: greeting
    if there_exists(["how are you","how are you doing","how you doin"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)
        x=True

    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it","what is the time"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        engine_speak(time)
        x=True

    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")
        x=True
    
    elif there_exists(["search"]) and 'youtube' not in voice_data:
        search_term = voice_data.replace("search","")
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")
        x=True
    

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        search_term = search_term.replace("on youtube","").replace("search","")
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")
        x=True

     #7: get stock price
    if there_exists(["price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")
        x=True
    


     #8 time table
    if there_exists(["show my time table","time table"]):
        im = Image.open(r"Data/mytime_table.jpg")
        im.show()
        x=True
    
     #9 weather
    if there_exists(["weather"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")
        x=True
     

     #10 stone paper scisorrs
    if there_exists(["game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves=["rock", "paper", "scissor"]
    
        cmove=random.choice(moves)
        pmove=voice_data
        

        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        #engine_speak("hi")
        if pmove==cmove:
            engine_speak("the match is draw")
        elif pmove== "rock" and cmove== "scissor":
            engine_speak("Player wins")
        elif pmove== "rock" and cmove== "paper":
            engine_speak("Computer wins")
        elif pmove== "paper" and cmove== "rock":
            engine_speak("Player wins")
        elif pmove== "paper" and cmove== "scissor":
            engine_speak("Computer wins")
        elif pmove== "scissor" and cmove== "paper":
            engine_speak("Player wins")
        elif pmove== "scissor" and cmove== "rock":
            engine_speak("Computer wins")
        x=True

     #11 toss a coin
    if there_exists(["toss","flip","coin"]):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        engine_speak("The computer chose " + cmove)
        x=True

     #12 calc
    if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply' or 'x':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")
        x=True
     #13 screenshot
    if there_exists(["capture","my screen","screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('Data/screen.png')
        engine_speak("Screen Shot has been succesfully saved in the Data folder")
        x=True

    
    
     #14 to search wikipedia for definition
    if there_exists(["definition of","wikipedia search"," search on wikipedia","wikipedia"]):
        definition=record_audio("what do you need the definition of")
        url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if (len(definitions)>1):
                engine_speak('here is what i found '+definitions[1])
            elif definitions[0]:
                engine_speak ('Here is what i found '+definitions[0])
            else:
                engine_speak('im sorry i could not find that definition, please try a web search')
                
        else:
                engine_speak("im sorry i could not find the definition for "+definition)
        x=True


    if there_exists(["exit", "quit", "goodbye","stop","adios"]):
        engine_speak("Thanks for using Rachel ,see you later, adios!")
        x=True
        exit()

    # Current city or region
    if there_exists(["where am i"]):
        Ip_info = requests.get('https://api.ipdata.co?api-key=06bea9ed1ea9244d6bd182b8446d70843760312d9494ee305f3f57f7').json()
        # Ip_info = requests.get('https://api.ipdata.co/country_name?api-key=APIKEY').json()
        loc = Ip_info['region']
        engine_speak(f"You must be somewhere in {loc}")    
        x=True
   
   # Current location as per Google maps
    if there_exists(["what is my exact location"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("You must be somewhere near here, as per Google maps")    
        x=True
    # if there_exists(["exit"]):
    #     engine_speak("Thanks for using Rachel , it was nice talking to you")  
    #     exit()

    if(x==False):
        engine_speak("please try again")



time.sleep(1)

person_obj = person()
rachel_obj = rachel()
rachel_obj.name = 'rachel'
person_obj.name = "Milan"
engine = pyttsx3.init()


while(1):
    x=False
    voice_data = record_audio("Recording") # get the voice input
    print("Done")
    print("Query:", voice_data)
    respond(voice_data) # respond
