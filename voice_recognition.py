import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('say which you want so search on google')
    audio = r.listen(source)


try:
    x =  r.recognize_google(audio)
    print(x)
    webbrowser.open_new_tab('https://www.google.com/search?q='+x)
    
except:
    pass
