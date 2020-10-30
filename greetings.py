engine = pyttsx3.init('sapi5') #Pyttsx3 which is used for text to speech in Python and sapi5 is Microsoft speech application platform interface 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) #alice's voice

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 
  
def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>= 0 and hour<12: 
        speak("Good Morning Miss !") 
   
    elif hour>= 12 and hour<18: 
        speak("Good Afternoon Miss !")    
   
    else: 
        speak("Good Evening Miss !")   
   
    assname =("Alice 1 point o") 
    speak("I am your Assistant,How can I help you?") 
    speak(assname) 
