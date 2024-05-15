import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

# Initialize the speech recognition engine
recognize = sr.Recognizer()

# Set the default voice for text-to-speech synthesis
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change the index to use a different voice if needed


def speakout(text):
    engine.say(text)
    engine.runAndWait()

def timeandgreet():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speakout("Good Morning!")

    elif 12 <= hour < 18:
        speakout("Good Afternoon!")

    else:
        speakout("Good Evening!")

    speakout("How can I assist you?")

def searchweb(query):
    speakout(f"Searching for {query} on the web...")
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognize.pause_threshold = 1
        audio = recognize.listen(source)

    try:
        print("Recognizing...")
        query = recognize.recognize_google(audio, language='en-US')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return ""
    return query


def execute_command(command):
    if "hello" in command:
        speakout("Hello there!")

    elif 'wikipedia' in command:
        speakout('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        speakout('According to Wikipedia')
        print(results)
        speakout(results)
        
    elif "search" in command:
        search_query = command.split("search")[-1].strip()
        searchweb(search_query)

    elif 'open youtube' in command:
        webbrowser.open("youtube.com")

    elif 'open google' in command:
        webbrowser.open("google.com")

    elif 'time' in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speakout(f"The time is {now}")

    elif 'date' in command:
        now = datetime.datetime.now().strftime("%D-%m-%Y")
        speakout(f"The date is {now}")

    elif 'exit' in command:
        speakout("Goodbye!")
        exit()

    else:
        speakout("I'm sorry, I couldn't understand your command.")


if __name__ == "__main__":
    timeandgreet()
    while True:
        command = listen().lower()
        if command:
            execute_command(command)