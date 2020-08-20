import speech_recognition
from twilio.rest import Client
import urllib.parse
import urllib.request
import yagmail,pyttsx3
import speech_recognition
from threading import Thread

speech_identifier = speech_recognition.Recognizer()

def say(text):
    engine = pyttsx3.init()
    engine.say(text,"txt")
    engine.runAndWait()

def getText():
    with speech_recognition.Microphone(0) as source:
        speech_identifier.adjust_for_ambient_noise(source,duration=1)
        print("# Say Something #")
        audio = speech_identifier.listen(source,phrase_time_limit=5)
    try:
        voiceText =  speech_identifier.recognize_google(audio)
        return voiceText
    except speech_recognition.UnknownValueError:
        print("I'm waiting for your command")


def sendSMS(numbers='',message=''):
    if numbers=='' and message=='':
        Thread(target=say,args=('please enter the mobile number of Receiver ',)).start()
        numbers = input(">>>> Enter the  ||MOBILE|| Number of Receiver --:: ")
        say('please tell what is your message would you like to send to receiver')
        message = getText()
        print('>> Message ',message)
    try:
        apikey="y91y/WBUY+k-I9eap8G39CfNZm1GkaIAz7xSapWDgI"
        sender="TXTLCL"
        data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
            'message' : message, 'sender': sender})
        data = data.encode('utf-8')
        request = urllib.request.Request("https://api.textlocal.in/send/?")
        f = urllib.request.urlopen(request, data)
        fr = f.read()
        print(fr)
        return 'message send successfully'
    except Exception as e:
        return 'message not send due to '+str(e)
    
def sendGmail():
    say('Sure Sir')
    say('please enter the GMAIL address of Receiver')
    email = input(">>>> Enter the  ||GMAIL|| address of Receiver --:: ")
    say('please tell me what is your Subject')
    subject = getText()
    print('>> Subject is :',subject)
    say('please tell me the message body of mail')
    message = getText()
    print('>> Message Body is: ',message)
    try:
        yag = yagmail.SMTP("alert.drowsiness.system@gmail.com", "drowsiness@123")
        yag.send(to = email, subject =subject, contents = message)
        yag.close()
        return 'Mail send Successfully'
    except Exception as e:
        return 'Mail not send due to '+str(e)


def makeCall():
    Thread(target=say,args=('Ok Boss I am Making Call to your Cell phone and Sending message to your cell phone',)).start()
    account_sid = 'AC979593ffc2ab7d49a04de70e6d712579'
    auth_token = 'c63cd412da65187098e95be42a84aabc'
    try:
        client = Client(account_sid, auth_token)
        call = client.calls.create(
                               # url='http://demo.twilio.com/docs/<?xml version="1.0" encoding="utf-8"?><Response><Say>Welcome to twilio!</Say></Response>',
                                url='http://demo.twilio.com/docs/voice.xml',
                                to='+917972846137',
                                from_='+917972846137'                        )
        return 'Call Request Send Successfully'
    except Exception as e:
        return 'Unable to make call due to '+str(e)


