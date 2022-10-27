import speech_recognition as sr
import pyttsx3
import pyjokes
import wikipedia
import pywhatkit
import datetime



listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)


def Mycommand(text):
    engine.say(text)
    engine.runAndWait()

def listenToMyCommand():
    try:
        with sr.Microphone() as source:
                print("What can I help you with today?")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'Jarvis' in command:
                    command = command.replace('Jarvis','')


    except: 
            pass
    return command
    
def runAssistant():
    command = listenToMyCommand()
    print(command)
    if 'play' in command:
        commandInMyVoice = command.replace('play','')
        Mycommand('playing '+ commandInMyVoice)
        pywhatkit.playonyt(commandInMyVoice)
        
    elif 'who is siddharth' in command:
        Mycommand('''Siddharth is a awesome guy who is always looking to learn something new. He
                  loves motorbikes and his favorite bike is BMW S 1000 RR. He is on his way to get a Master's degree in
                  Computer Science.''')
        
    elif 'who is' in command:
        whoIS = command.replace('who is' , '')
        about = wikipedia.summary(whoIS, 6)
        print(about)
        Mycommand(about)
        
    elif 'what is' in command:
        whatIS = command.replace('what is', '')
        aboutWhat = wikipedia.summary(whatIS, 6)
        print(aboutWhat)
        Mycommand(aboutWhat)
        
        
    elif 'joke' in command:
        Mycommand(pyjokes.get_joke())
            
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S %p')
        print(time)
        Mycommand('Current time is ' + time)
        
    else:
        Mycommand("I could not understand you. Can you please repeat what you said? ")
        
  
while True:  
        
     runAssistant()
        
        