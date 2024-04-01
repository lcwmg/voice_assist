import speech_recognition as sr
import pyttsx3
import time
from xbee import XBee, ZigBee
import serial

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to listen to the user's voice command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""

# Function to speak the response
def speak(response):
    engine.say(response)
    engine.runAndWait()

# Function to turn on home electronic appliances
def turn_on_appliance(appliance):
    # Code to send command to turn on the appliance
    print(f"Turning on {appliance}...")

# Function to schedule shutdown command
def schedule_shutdown(minutes):
    print(f"Scheduling shutdown in {minutes} minutes...")
    time.sleep(minutes * 60)  # Convert minutes to seconds
    print("Shutting down...")
    # Code to send shutdown command to home automation system

# Main function to execute the voice assistant
def main():
    while True:
        command = listen()
        if "hello" in command:
            speak("Hello! How can I assist you today?")
        elif "turn on" in command:
            appliance = command.split("turn on")[1].strip()
            turn_on_appliance(appliance)
            speak(f"{appliance} has been turned on.")
        elif "schedule shutdown" in command:
            minutes = int(command.split("schedule shutdown")[1].strip())
            schedule_shutdown(minutes)
            speak(f"Shutdown has been scheduled in {minutes} minutes.")
        elif "goodbye" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    main()