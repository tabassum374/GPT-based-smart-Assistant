from openai import OpenAI
from apikey import api_data
import os
import speech_recognition as sr
import pyttsx3 
import webbrowser

Model = 'gpt-3.5-turbo'
client = OpenAI(api_key=api_data)
def Reply(question):
    completion = client.chat.completions.create(
        model=Model,
        messages=[
            {'role':"system","content":"You are a helpful assistant"},
            {'role':'user','content':question}
        ],
        max_tokens=200
    )
    answer = completion.choices[0].message.content
    return answer
# Text to Speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
speak("Hello how are you?")
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening .......')
        r.pause_threshold = 1 #wait for 1 sec before considering the end of phrase
        audio=r.listen(source)
    try:
        print('Recognizing ....')
        query =r.recognize_google(audio, language = 'en-in')
        print("User Said: {} \n",format(query))
    except Exception as e:
        print("say that again .....")
        return "None"
    return query
if __name__ == '__main__':
    while True:
        query = takeCommand().lower()
        if query == 'none':
            continue
        ans = Reply(query)
        print(ans)
        speak(ans)
        # Specific Browser Related Tasks
        if "Open youtube" in query:
            webbrowser.open('www.youtube.com')
        if "Open Google" in query:
            webbrowser.open('www.google.com')          
        if "Open Hotstar" in query:
            webbrowser.open('www.hotstar.com') 
        if "Open linkedin" in query:
            webbrowser.open('www.google.com')
        if "bye" in query:
            break
