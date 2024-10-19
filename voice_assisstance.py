import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

print('Loading your AI personal assistant - G One')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Adjusting for ambient noise
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        speak("Listening...")

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)  # Setting timeout and phrase time limit
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said: {statement}\n")

        except sr.UnknownValueError:
            speak("Sorry, I did not catch that. Could you please repeat?")
            return "None"

        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting to the speech service.")
            return "None"

        except Exception as e:
            speak("Pardon me, please say that again.")
            return "None"

        return statement

speak("Loading your AI personal assistant ")
wishMe()

if __name__ == '__main__':
    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()

        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant  is shutting down, Good bye')
            print('your personal assistant  is shutting down, Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google Chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail is open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("What's the city name?")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(f"Temperature in Kelvin unit is {current_temperature}")
                speak(f"Humidity in percentage is {current_humidiy}")
                speak(f"Weather description: {weather_description}")
                print(f"Temperature: {current_temperature}\nHumidity: {current_humidiy}\nDescription: {weather_description}")
            else:
                speak("City Not Found")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am voice assistant version 1.0, your personal assistant. I can do minor tasks like '
                  'opening YouTube, Google Chrome, Gmail, StackOverflow, predict time, take a photo, search Wikipedia, predict weather '
                  'in different cities, get top headlines from Times of India, and answer computational or geographical questions!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Keerthi")
            print("I was built by Keerthi")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is StackOverflow")

        elif 'news' in statement:
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India. Happy reading!')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer computational and geographical questions. What would you like to ask?')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok, your PC will log off in 10 seconds. Make sure to exit from all applications.")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)












