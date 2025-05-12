import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def listen_command():
    with sr.Microphone() as source:
        print("[Speech] Listening for command...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"[Speech] Recognized Command: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("[Speech] Could not understand audio.")
            return None

def speak_response(message):
    print(f"[Speech] Speaking: {message}")
    tts_engine.say(message)
    tts_engine.runAndWait()

if __name__ == "__main__":
    while True:
        cmd = listen_command()
        if cmd:
            if "stop" in cmd:
                speak_response("Emergency Stop Activated.")
            elif "start" in cmd:
                speak_response("Starting Trash Collection Routine.")
            elif "exit" in cmd:
                speak_response("Exiting Speech Interface.")
                break
            else:
                speak_response("Command not recognized.")
