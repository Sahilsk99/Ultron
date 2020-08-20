import tkinter as tk
from PlayUltronGif import playGif
from PIL import Image, ImageTk
from itertools import count
import pythoncom
from threading import Thread
import win32com.client
import speech_recognition
import time
from User_Voice_Validate import Chk_Commands
import datetime

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speech_identifier = speech_recognition.Recognizer()
localtime = time.asctime(time.localtime(time.time()))
now = datetime.datetime.now()
hr = now.hour


def vp_start_gui():
    root = tk.Tk()
    top = gifWin(root)
    root.mainloop()


class gifWin:
    def __init__(self, top=None):

        ### Basic Window Background
        def basicWindow():
            top.lift()
            top.configure(background="white")
            top.overrideredirect(True)
            top.geometry('1300x700')
            windowWidth = 1300
            windowHeight = 700
            positionRight = int(top.winfo_screenwidth() / 2 - windowWidth / 2)
            positionDown = int(top.winfo_screenheight() / 2 - windowHeight / 2)
            top.geometry("+{}+{}".format(positionRight, positionDown))
            top.wm_attributes("-topmost", True)
            top.wm_attributes("-disabled", True)
            top.wm_attributes("-transparentcolor", "white")

        ### Load Ultron avatar
        def loadAvtarComponents():
            self.lblGif = tk.Label(top)
            self.lblGif.place(relx=3.50, rely=0.0, height=700, width=1200)
            self.lblGif.configure(background="white")
            lbl = playGif(self.lblGif)
            lbl.load("Ultron_Avatar.gif")
            lbl.pack()

        ### LOad Actual ultron main speech recognition and speak module with gif Avatar
        def mainFunction():
            ##############################################################################
            ##                            HELPER FUNCTIONS                              ##
            ##############################################################################

            ### Speak sentence with gif
            def ultronSpeak(sentence):
                pythoncom.CoInitialize()
                self.lblGif.pack()
                speaker.Speak(sentence)
                self.lblGif.pack_forget()

            ### Recognize voice and perform operation command
            def ultronVoiceRecog():
                ### Convert Voice into Text
                def getText():
                    with speech_recognition.Microphone(0) as source:
                        speech_identifier.adjust_for_ambient_noise(source, duration=1)
                        print("\n############## Say Something ##############")
                        audio = speech_identifier.listen(source, phrase_time_limit=5)
                    try:
                        voiceText = speech_identifier.recognize_google(audio)
                        print('Input Command >> '+voiceText)
                        return voiceText.lower()
                    except speech_recognition.UnknownValueError:
                        print("----- I'm waiting for your command -------")

                greet = ''
                if hr < 12:
                    greet = "Good morning Sir"
                elif hr >= 12 and hr < 17:
                    greet = "Good afternoon Sir"
                elif hr >= 17 and hr <= 19:
                    greet = "Good Evening Sir"

                ultronSpeak(greet + 'Hello I am Ultron Created by Sahil Start Speaking to me')

                ##############################################################################################
                ### Main Function run untile condition false
                ##############################################################################
                ##                            MAIN SCRIPT                                   ##
                ##############################################################################
                while True:
                    text = getText()
                    if text == None:
                        pass
                    else:
                        # ultronSpeak(text)
                        reply = Chk_Commands(text)
                        if reply != None:
                            print("Ultron Reply  >> "+reply)
                            ultronSpeak(reply)
                            print()
            #############################################################################################

            ### Start mic funtion in thread
            t3 = Thread(target=ultronVoiceRecog)
            t3.start()

        ### Load And play Theme sound and play GIf
        basicWindow()

        loadAvtarComponents()
        t2 = Thread(target=mainFunction)
        t2.start()

if __name__ == '__main__':
    vp_start_gui()
