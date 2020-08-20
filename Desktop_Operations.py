import win32gui
import win32con
import os, subprocess

from datetime import datetime
import keyboard
import pyperclip
from Browser_Operations import visit_website

def turnOffScreen():
    #to turn off use :-
    win32gui.SendMessage(win32con.HWND_BROADCAST,win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)

def turnOnScreen():
    #to turn on use :-
    win32gui.SendMessage(win32con.HWND_BROADCAST,win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, -1)

def sleepPc():
    os.system(r'%windir%\system32\rundll32.exe powrprof.dll,SetSuspendState Hibernate')

def shutDownPc():
    os.system("shutdown /s /t 1")

def restartPc():
    os.system("shutdown /r /t 1")

def openApps(appName):

    if appName=='calculator':
        os.startfile("C:\Windows\System32\calc.exe")

    elif appName=='notepad' or appName=='editor' or appName=='notebook' or appName=='text editor':
        os.startfile("C:\Windows\System32\\notepad.exe")

    elif appName=='paint':
        os.startfile("C:\Windows\System32\mspaint.exe")

    elif appName=='explorer' or appName=='file manager' or appName=='folder' or appName=='manager' or appName=='pc' or appName=='this pc':
        os.system('explorer')

    elif appName=='google chrome' or appName=='chrome' or appName=='browser':
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")

    elif appName=='pycharm' or appName=='life' or appName=='my playground' or appName=='playground' or appName=='code editor':
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\JetBrains PyCharm Edu 2019.1.lnk")

    elif appName=='ms office' or appName=='excel' or appName=='word' or appName=='power point' or appName=='office' or appName=='wps' or appName=='wps office':
        os.startfile(r"C:\Users\Sahil Sheikh\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\WPS Office\WPS Office.lnk")

    elif appName=='jupyter' or appName=='jupyter notebook':
        os.startfile(r"C:\Users\Sahil Sheikh\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Jupyter Notebook.lnk")

    elif appName=='spyder':
        os.startfile(r"C:\Users\Sahil Sheikh\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Spyder.lnk")

    elif appName=='command prompt' or appName=='cmd' or appName=='terminal' or appName=='prompt':
        os.startfile(r"C:\Users\Sahil Sheikh\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt.lnk")

    elif appName=='task manager' or appName=='task' or appName=='process' or appName=='all process' or appName=='processes':
        keyboard.press_and_release('ctrl+shift+esc')

    elif appName=='setting':
        keyboard.press_and_release('Win+I')

    elif appName=='control panel' or appName=='panel':
        os.startfile('control')

    elif appName=='facebook' or appName=='fb':
        visit_website('http://www.facebook.com')

    elif appName=='whatsapp' or appName=='wa':
        visit_website('http://web.whatsapp.com')

    elif appName=='instagram' or appName=='insta':
        visit_website('http://instagram.com')

    elif appName=='desktop' or appName=='home':
        subprocess.Popen(r'explorer "C:\Users\Sahil Sheikh\Desktop"')

    elif appName=='c drive' or appName=='c':
        subprocess.Popen(r'explorer "C:"')

    elif appName=='d drive' or appName=='d':
        subprocess.Popen(r'explorer "D:"')

    elif appName=='e drive' or appName=='e':
        subprocess.Popen(r'explorer "E:"')

    elif appName=='f drive' or appName=='f':
        subprocess.Popen(r'explorer "F:"')

    else:
        return 'Command not Recognized please Try Again'

def minimizeWin():
    Minimize = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

def minimizeAllCurentWin():
    keyboard.press_and_release('win+m')

def maximizeWin():
    Maximize = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(Maximize, win32con.SW_MAXIMIZE)

def restoreWin():
    Restore = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(Restore, win32con.SW_RESTORE)

def restoreAllWin():
    keyboard.press_and_release('shift+win+m')

def closeWin():
    keyboard.press_and_release('alt+f4')

def getScreenShot():
    keyboard.press_and_release('Win+PrtScn')

def getDate():
    now = datetime.now()
    monthName = now.strftime('%B')
    year = now.year
    day = now.day
    dayName = now.strftime("%A")
    return 'Today is {} {} of {} {} '.format(dayName,day,monthName,year)

def getTime():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    return 'Current timinig is is {} hour and {} minute'.format(hour,minute)

def get_clipboard():
    return pyperclip.paste()

def pressKey(key):
    keyboard.press_and_release(key)

def writeText(text):
    keyboard.write(text)

def gotoDirectory(appName):
    if appName=='desktop' or appName=='home':
        subprocess.Popen(r'explorer "C:\Users\Sahil Sheikh\Desktop"')

    elif appName=='c drive' or appName=='c':
        subprocess.Popen(r'explorer "C:"')

    elif appName=='d drive' or appName=='d':
        subprocess.Popen(r'explorer "D:"')

    elif appName=='e drive' or appName=='e':
        subprocess.Popen(r'explorer "E:"')

    elif appName=='f drive' or appName=='f':
        subprocess.Popen(r'explorer "F:"')

def creatFolder():
    keyboard.press_and_release('shift+ctrl+N')


