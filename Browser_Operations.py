from selenium import webdriver
global browser,permision,tab
tab = 0
permision=False

def open_browser():
    global browser,permision
    browser = webdriver.Chrome(executable_path=r"chromedriver.exe")
    #wait = WebDriverWait(browser, 600)
    permision=True

def visit_website(site):
    global browser,permision,tab
    if permision==True:
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[tab])
        browser.get(site)
        tab +=1
    else:
        open_browser()
        browser.get(site)
        tab +=1

def closeTab():
    global browser
    try:browser.close()
    except Exception as e:print(e)

def swipe_up():
    global browser
    try:browser.execute_script("window.scrollTo(0, window.scrollY + 500)")
    except Exception as e:print(e)
    #browser.execute_script("window.scrollTo({}, {})".format(0,500))

def swipe_down():
    global browser
    try:browser.execute_script("window.scrollTo(window.scrollY, window.scrollY - 500)")
    except Exception as e:print(e)
   # browser.execute_script("window.scrollTo({}, {})".format(500,0))
