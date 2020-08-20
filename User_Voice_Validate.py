import re
from threading import Thread
import Searching_Operations, Browser_Operations, Desktop_Operations, Mobile_Operations
def Chk_Commands(str):

    str = str.lower()

    ### GOogle Search
    google = "google about "
    search = "search for "
    search1 = 'search about '
    search2 = 'google on '
    search3 = 'search '
    search4 = 'google search '

    ## BRowser Operation
    if str=='open browser':
        Thread(target=Browser_Operations.open_browser).start()
        return 'Opening Web Browser'
    elif str=='swipe up':
        Browser_Operations.swipe_up()
    elif str=='swipe down':
        Browser_Operations.swipe_down()
    elif str=='close tab':
        Browser_Operations.closeTab()
    elif 'visit' in str:
        reg_ex = re.search('visit (.+)', str)
        if reg_ex:
            domain = reg_ex.group(1)
            print(domain)
            url = 'https://www.' + domain
            Thread(target=Browser_Operations.visit_website, args=(url,)).start()
            return 'Wait a second Sir Visiting {}'.format(domain)


    ### Desktop Operation
    ### Open apps
    elif 'open' in str or 'run' in str or 'execute' in str or 'want' in str :
        if 'dont' in str or 'do not' in str:
            pass
        else:
            str = str.replace('my','')
            if 'open' in str:
                reg_ex = re.search('open (.+)', str)
            elif 'run' in str:
                reg_ex = re.search('run (.+)', str)
            elif 'execute' in str:
                reg_ex = re.search('execute (.+)', str)
            elif 'want' in str:
                reg_ex = re.search('want (.+)', str)

            if reg_ex:
                app = reg_ex.group(1).strip()
                try:
                    Thread(target=Desktop_Operations.openApps,args=(app,)).start()
                    return 'Opening {} '.format(app)
                except:
                    return 'Sorry App not installed in my system'



    elif 'turn screen off' in str or 'turn off' in str or 'screen off' in str:
        Desktop_Operations.turnOffScreen()
    elif 'turn screen on' in str or 'turn on ' in str or 'screen on' in str:
        Desktop_Operations.turnOnScreen()
    elif 'sleep ' in str or 'sleep desktop ' in str:
        Desktop_Operations.sleepPc()
    # elif 'shutdown' in str or 'shutdown pc' in str or 'power off' in str:
    #     Thread(target=Desktop_Operations.shutDownPc).start()
    #     return 'Shutting down your PC'
    elif 'restart' in str or 'reboot' in str or 'restart pc' in str or 'restart windows' in str:
        Thread(target=Desktop_Operations.restartPc).start()
        return 'Rebooting Windows'
    elif 'minimise all' in str or 'minimize all window' in str:
        Desktop_Operations.minimizeAllCurentWin()
    elif 'minimise' in str:
        Desktop_Operations.minimizeWin()
    elif 'maximise' in str or 'maximum' in str:
        Desktop_Operations.maximizeWin()
    elif 'restore' in str:
        Desktop_Operations.restoreWin()
    elif 'close' in str or 'close it' in str:
        Desktop_Operations.closeWin()
    elif "what is today date" in str or "tell me date" in str or "what is today's date" in str or "date" in str or 'tell me today date' in str or "tell me today's date" in str:
        return Desktop_Operations.getDate()
    elif "what time is it" in str or "tell me time" in str or "what's the time" in str or "time" in str or "what current time" in str:
        return Desktop_Operations.getTime()


    ## stop
    elif 'stop' in str:
        Desktop_Operations.pressKey('q')
        Desktop_Operations.pressKey('space')
    elif str=='play':
        Desktop_Operations.pressKey('space')

    ## Youtube SOng
    elif 'play' in str:
        reg_ex = re.search('play (.+)', str)
        if reg_ex:
            song = reg_ex.group(1)
            print(song)
            Thread(target=Searching_Operations.playSong,args=(song,)).start()
            return 'Opening Browser to Play  {}'.format(song)

    ### GOogle Search
    elif str == google+str[13:]:
        Thread(target=Searching_Operations.googleSearch,args=(str[13:],)).start()
        return "here we go"
    elif str == search+str[11:] :
        Thread(target=Searching_Operations.googleSearch,args=(str[11:],)).start()
        return "I'm on it sir"
    elif str == search1+str[13:] :
        Thread(target=Searching_Operations.googleSearch,args=(str[13:],)).start()
        return "on my Way"
    elif str == search2+str[10:] :
        Thread(target=Searching_Operations.googleSearch,args=(str[10:],)).start()
        return "I'm on it sir"
    elif str == search3+str[7:] :
        Thread(target=Searching_Operations.googleSearch,args=(str[7:],)).start()
        return "I'm on it sir"
    elif str == search4+str[14:] :
        Thread(target=Searching_Operations.googleSearch,args=(str[14:],)).start()
        return "I'm Searching it sir"

    ### Button Automation Shortcut
    elif 'go to' in str:
        reg_ex = re.search('go to (.+)', str)
        if reg_ex:
            Desktop_Operations.gotoDirectory(reg_ex.group(1).strip())
            return 'ok'
    elif 'create folder' in str or 'new folder' in str:
        Desktop_Operations.creatFolder()
    elif 'create new file' in str or 'new file' in str:
        Desktop_Operations.pressKey('ctrl+N')
    elif 'save file' in str or 'save it' in str or 'save' in str:
        Desktop_Operations.pressKey('ctrl+S')
    elif 'select all' in str or 'select' in str:
        Desktop_Operations.pressKey('ctrl+A')
    elif 'copy it' in str or 'copy' in str or 'copy text' in str:
        Desktop_Operations.pressKey('ctrl+c')
    elif 'cut it' in str or 'cut' in str:
        Desktop_Operations.pressKey('ctrl+X')
    elif 'paste it' in str or 'paste' in str:
        Desktop_Operations.pressKey('ctrl+V')
    elif 'press' in str:
        reg_ex = re.search('press (.+)', str)
        if ' ' in reg_ex.group(1):
            app = reg_ex.group(1)
            hotKey = app[:-2]
            key = app[-1:].upper()
            cmd = hotKey+'+'+key
            try:
                Desktop_Operations.pressKey(cmd)
            except:
                return 'Sorry I did not get your command try again'
        else:
            cmd = reg_ex.group(1)
            try:
                Desktop_Operations.pressKey(cmd)
            except:
                return 'Sorry I did not get your command try again'

    elif 'type' in str:
        reg_ex = re.search('type (.+)', str)
        if reg_ex:
            Desktop_Operations.writeText(reg_ex.group(1))

    elif 'write' in str:
        reg_ex = re.search('write (.+)', str)
        if reg_ex:
            Desktop_Operations.writeText(reg_ex.group(1))



    #### Mobile Operations
    elif 'send gmail' in str or 'send email' in str or 'send mail' in str or 'send a gmail' in str or 'send a email' in str or 'send a mail' in str:
        resp = Mobile_Operations.sendGmail()
        return resp

    #### Mobile Operations
    elif 'send sms' in str or 'send message' in str or 'send text' in str or 'send a text' in str or 'send a message' in str:
        resp = Mobile_Operations.sendSMS('','')
        return resp

    elif 'missing phone' in str or 'missing my cell phone' in str or 'find my cell phone' in str or 'find my phone' in str or 'finding my cell phone' in str or 'finding my phone' in str or 'find my mobile phone' in str :
        resp = Mobile_Operations.makeCall()
        return resp

    ### Trending News
    elif 'trending news' in str or 'tell me about news' in str or 'today news' in str or 'tell me today news' in str or 'news' in str:
        Thread(target=Searching_Operations.get_news).start()
        return 'Sure sir Searching'

    elif 'hello' in str:
        return 'Good sir what about you'

    elif 'good' in str:
        return 'Thank for Compliment sir'

    elif 'you can do' in str:
        print(
               '#################################################################' \
               '\n##'\
               '\n##      1. I can search anything on Google' \
               '\n##      2. I can play song on youtube' \
               '\n##      3. I can find lasted trending news'\
               '\n##      4. I can send Gmail and SMS to any mobile'\
               '\n##      5. I can make call on your cell phone'\
               '\n##      6. I can open any installed application on your system'\
               '\n##      7. I can change your current directory '\
               '\n##      8. I can control your desktop such as shutdown, turn off,' \
               '\n##         reboot, turn screen off, Lock, Unlock, etc'\
               '\n##      9. I can handle all browser operation such scroll up ' \
               '\n##         Scroll down, visit website, close tab, open tabs'\
               '\n##      10. I can perform keyboard typing and can press any special key'\
               '\n##'\
               '\n#################################################################' \
            )
        return '\nI can do lots of things such as listed above \n' \

    elif 'shut down your system' in str or 'shut down' in str or 'shutdown pc' in str or 'power off' in str:
        Mobile_Operations.say('Okay boss I am shutting down my system Have a great day bye bye')
        import os
        os._exit(0)

### Notepad automation Example
def notepad_Example_Automation():
    import time
    time.sleep(1)
    Chk_Commands('Select all Text')
    time.sleep(1)
    Chk_Commands('the copy text')
    time.sleep(1)
    Chk_Commands('open notepad')
    time.sleep(3)
    Chk_Commands('create new file')
    Chk_Commands('PASTE the text')
    Chk_Commands('press control s')
    time.sleep(3)
    Chk_Commands('type checkFile')
    Chk_Commands('press enter')
    Chk_Commands('minimize it')

# Chk_Commands('I waNT my cmd')
# Chk_Commands('type python')
# Chk_Commands('press enter')
