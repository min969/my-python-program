from rivescript import RiveScript
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import time
bot = RiveScript(utf8=True)

bot.load_directory("brain")
bot.sort_replies()

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def chat(message):
    if message == "":
        return -1, "No message found "
    else:
        response = bot.reply("user", message)
    if response:
        return 0, response
    else:
        return -1, "No response found"