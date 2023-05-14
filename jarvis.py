import pyttsx3
import speech_recognition

engine = pyttsx3.init()
voices = engine.getProperty("voices")  # 0 --- Boys and 1 -- Girls voice
engine.setProperty("voice", voices[0].id)
recognition = speech_recognition.Recognizer()


def speak_data(data):
    engine.say(data)
    engine.runAndWait()
    engine.stop()

# In the next video, stay tune!


def search_chargpt(query):
    pass


while True:
    try:
        with speech_recognition.Microphone() as microphone:
            speak_data(
                "Hello EvilCoder this is Jarvis, how can i help you today?")
            recognition.adjust_for_ambient_noise(microphone, duration=.2)
            audio = recognition.listen(microphone)
            speak_data("Coverting Speech to Text")
            audio_text = recognition.recognize_google(audio).lower()
            speak_data("You have spoken: " + audio_text)

            if "" in audio_text:
                search_chargpt(audio_text)

    except speech_recognition.exceptions.UnknownValueError:
        recognition = speech_recognition.Recognizer()
        continue
