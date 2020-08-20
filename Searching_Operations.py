import urllib.request
import urllib.parse
import re
import wikipedia
import webbrowser
from threading import Thread
import keyboard
import pyttsx3
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

def playSong(song):
    query_string = urllib.parse.urlencode({"search_query" : song})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    url = "http://www.youtube.com/watch?v=" + search_results[0]
    print(url)
    webbrowser.open(url)

def googleSearch(word):
    print(word)
    url="http://www.google.com/?#q="
    webbrowser.open_new_tab(url+word)

def get_news():
    def say(text):
        def stopCheck():
            while True:
                if keyboard.is_pressed('q') or keyboard.is_pressed('esc'):
                    engine.stop()
                    break

        engine = pyttsx3.init()
        #more code here but its just setting the volume and speech rate
        engine.say(text,"txt")
        Thread(target=stopCheck).start()
        engine.runAndWait()

    try:
        news_url="https://news.google.com/news/rss"
        Client=urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        for news in news_list[:5]:
            print(news.title.text.encode('utf-8'))
        result = news.title.text.encode('utf-8')
        Thread(target=say,args=(result,)).start()

    except Exception as e:
        print('Eror ')


