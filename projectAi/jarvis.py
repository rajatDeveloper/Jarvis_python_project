from math import perm
import pyttsx3
from requests.api import request
import speech_recognition as sr
import datetime
import os
import cv2 as cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit 
import smtplib
import sys
import pyjokes
import pyautogui
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import instaloader
import PyPDF2
import requests
from bs4 import BeautifulSoup
from pywikihow import WikiHow, search_wikihow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)
# engine.setProperty('rate',180) 

#run the str into adio
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#take command function which takes trhe command from user==>  voice ko text mai convert kr ta
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening......._______......_____")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=100000,phrase_time_limit=5)
    try :
        print("Recognition.......______........")
        query = r.recognize_google(audio,language='en-in')
        print(f" User said : {query}")
    except Exception as e :
        # speak("Say that again pls.....")
        return  "none"
    query = query.lower()    
    return query

#wish function which wish you according to time
def wish():
    hour = int(datetime.datetime.now().hour)
   
    if hour>=0 and hour<=12:
       speak(f"Good Morning Sir    ")
    elif hour>12 and hour<18:
        speak(f"Good Afternoon Sir ")     
    else:
        speak(f"Good evening Sir")    
    speak("I am Jarvis Sir , please tell me how i can help   ")    

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rajatdelldhiman@gmail.com','shashibala')
    server.sendmail('rajatdelldhiman@gmail.com',to,content)
    server.close()

def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=94eccacd717b4296ae58b6ffe3649daa"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news  is {head[i]}")  

def account_info():
    with open('data.txt','r') as rd:
        info = rd.read().split()
        email = info[0]
        password = info[1]
    return email , password   

def read_pdf():
    book = open("pdf_book.pdf",'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"total numbers of pages in this file is {pages}")
    speak("sir please enter the page number to read out :  ")   
    pg = int(input("please enetr the page number : "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

    


# if __name__ =='__main__':

    
def main_run():    
    wish()
    while True:
    # if 1:

        query = takecommand().lower()
    #LOGIC BUILDING TASKS
        if 'open notepad' in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        elif"hellow" in query :
            speak("hellow sir , how I can help you ")
        elif'how are you' in query:
            speak("i am fine sir , how is you day ")        
        elif 'open visual studio code' in query:
            npath = r"C:\Users\rajat\AppData\Local\Programs\Microsoft VS Code\code.exe"
            os.startfile(npath)
        elif 'open pycharm' in query:
            npath = r"C:\Program Files\JetBrains\PyCharm Community Edition 2021.1.1\bin\pycharm64.exe"
            os.startfile(npath)
        elif 'open typing master' in query:
            npath = r"C:\Program Files (x86)\TypingMaster\tmaster.exe"
            os.startfile(npath)
        elif 'open command prompt' in query:
            os.startfile('C:\\Windows\\system32\\cmd.exe')
        elif 'open camera' in query :
            cap = cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50) 
                if k==27:
                   break
            cap.release()
            cv2.destroyAllWindows()

        elif 'play music' in query:
            music_dir = 'R:\\music hindi'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)      
            os.startfile(os.path.join(music_dir,rd))

        elif 'ip address' in query:
            ip = get(r'https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif  'wikipedia' in query:    
            speak("searching  wikipedia ...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia ")
            speak(results)
            # print(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("yes i opened it ....") 

        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")
            speak("yes i opened it ....")

        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com")
            speak("yes i opened it ....")

        elif 'open google' in query:
            speak("Sir what should i search on google")
            cm = takecommand().lower() 
            webbrowser.open(f"{cm}")
            speak("yes i opened it ....")

        elif 'open linked in' in query:
            webbrowser.open("www.linkedin.com")
            speak("yes i opened it ....")

        elif 'open whatsapp' in query:
            webbrowser.open(r"https://web.whatsapp.com/")
            speak("yes i opened it ....")

        elif 'open gmail' in query:
            webbrowser.open("www.gmail.com")
            speak("yes i opened it ....")

        elif 'open stack overflow' in query:
            webbrowser.open("www.stackoverflow.com")
            speak("yes i opened it ....")  
    #website opeming 
        elif 'open my website' in query:
            webbrowser.open(r"https://rajatdelldhiman.wixsite.com/rdsoftware")
            speak("yes i opened it ....")
    #wahtsapp boot
        elif 'send whatsapp message' in query:
            try:
                speak("Enter the mobile number to whome message to be sent ")
                num = input()
                speak("please speak your message")
                msg = takecommand()
                ptimehr = int(datetime.datetime.now().hour) 
                ptimemin = int(datetime.datetime.now().minute)+2
                kit.sendwhatmsg(f"+91{num}",msg,ptimehr,ptimemin)
                speak("sir i send the message on given number ")
            except Exception as e:
                speak(e)
                speak("Unable to snd the whatsapp message , sorry sir ")    

    #song on youtube
        elif 'play music on youtube'in query:
            speak("speak the song name which you want to listen")
            sg = takecommand()
            kit.playonyt(sg)
    # email boot
        elif 'email to' in query:
            try:
                speak("what should I say ?")
                datamsg = takecommand().lower()
                speak("To whom i send this mail Sir please input the username or id  ")
                emailnam=input() 
                sendEmail(emailnam,datamsg)
                speak("Mail has been sent sucessfully")
            except Exception as e:
                   print(e) 
                   speak("sorry sir I am unable to send the the mail")
    # sleep of jarvis commnd 
        
            #closing application 
        elif 'close notepad' in query :
            speak("ok sir closing notpad ")
            os.system("taskkill /f /im notepad.exe")
    # seting alarm 
        elif 'set alarm' in query :
            time_now = int(datetime.datetime.now().hour)
            speak("sir please input the time for alarm ")
            time_user = int(takecommand())
            if time_now == time_user :
                music = r'R:\music hindi'
                songs_alarm = os.listdir(music)
                os.startfile(os.path.join(music,songs_alarm[3]))
                #joke in english
        elif 'tell me a joke'in query:
            joke = pyjokes.get_joke()
            speak(joke)
            #shutdiown
        elif 'shut down the system' in query:
            os.system("shutdown /s /t 5")    

        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")

        elif 'sleep the system' in query:
            os.system("rundll32.exe powrprof.dll,setSuspendState 0,1,0")       

        #switch the window
        elif 'switch the window' in query :
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            #not in gui
        elif'temperature' in query:
            speak("sir in which city you want to know the temperture , please input the name")    
            search = input("enter the city name : ")
            url = f"https://www.google.com/search?q=temperture in {search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f" current temperture in {search} is {temp}")
        elif 'want to search something special' in query or 'want to know something'in query or  'special mod'in query:
            speak("sir special mod is activated , you can ask anything how why  ")
            while True:
                speak("please ask anything , what you want to know")
                how = takecommand()
                try:
                    if 'exit this special mod' in how or 'exit this mod' in how:
                        speak("ok sir , special mod is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        print(how_to[0])
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir i am unable to find this ")
        elif'how much power left' in query or 'how much power we have'in query or 'battery'in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")
        elif'internet speed' in query:
            import speedtest
            speak("sir wait for little bit time , i am checking ")
            st = speedtest.Speedtest()
            dI= st.download()
            uI= st.upload()
            speak(
                f"sir we have {dI} bit per second downloading speed and {uI} bit per second uploading speed")

        elif 'tell me news' in query:
            speak("please wait sir for whill serching for news ")
            news()
    #tweet automation just tweet only by voice command
        elif 'tell my location' in query or 'where i am' in query:
            speak("wait sir , let me check")
            try:
                ip_loc = get(r'https://api.ipify.org').text
                print(ip_loc)
                url2 ='https://get.geojs.io/v1/ip/geo/'+ip_loc+'.json'
                geo_requests = requests.get(url2)
                geo_data = geo_requests.json()
                city = geo_data['city']
                # state = geo_data['state']  
                country = geo_data['country']
                speak(f"sir i am not sure , but i think we are in {city} city of {country} country")
            except Exception as e :
                speak("i am unable to find , to to low network")    
 
    #instagram profile check and not downoloading
        elif 'instagram profile'in query or 'profile on instagram'in query :
            speak('please enter the username of profile correctly ')
            name = input("Enter the username : ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(4)
            # speak(f'sir would you like to download profile picture of user {name} , say yes and no ')
            speak("sir i am downloading the profile picture")
            
            mod = instaloader.Instaloader()
            mod.download_profile(name,profile_pic_only=True)
            speak("sir i am done , profile picture is downloaded in same folder, now i am ready to take the next command")
            
        
        elif 'read pdf'in query or 'read my pdf'in query :
            read_pdf()

        elif 'hide all files' in query or 'hide folder'in query or 'visible for everyone'in query:
            speak("sir please tell me you weant to hide the files or folder or want to make visible for everyone ")        
            condition = takecommand().lower()
            if 'hide' in condition :
                speak("input the location")
                userLoc = input("input the location :")
                os.chdir(userLoc)
                os.system("attrib +h /s /d")
                speak('sir  i have hide the all files from repected location')
                os.chdir(r'R:\projectAi')#to get back to present dir as working dir
            elif 'visible' in condition:
                speak("input the location")
                userLoc = input("input the location :")
                os.chdir(userLoc)
                os.system("attrib -h /s /d")
                speak('sir  i have made  all files visible ')
                os.chdir(r'R:\projectAi')
            elif 'leave it' in condition:
                speak("ok sir ,i am ready for next command ")   



    # # tweet boot or tweeet
    #     elif'can you tweet for me' in query or 'can you make post on tweet':
 

    #         email, password = account_info()
    #         speak("sir what i can tweet for you ")
    #         tweet = takecommand().lower()

    #         options = Options()
    #         options.add_argument("start-maximized")
    #         driver = webdriver.Chrome(options=options)

    #         driver.get(r'https://twitter.com/login')
    #         email_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
    #         passward_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
    #         login_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div'
    #         time.sleep(2)

    #         driver.find_element_by_xpath(email_xpath).send_keys(email)
    #         time.sleep( 0.5)
    #         driver.find_element_by_xpath(passward_xpath).send_keys(password)
    #         time.sleep(0.5)
    #         driver.find_element_by_xpath(login_xpath).click()
    #         time.sleep(0.5)

    #         tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
    #         type_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
    #         post_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span'
    #         time.sleep(2)
    #         driver.find_element_by_xpath(tweet_xpath).click()
    #         time.sleep(0.5)
    #         driver.find_element_by_xpath(type_xpath).send_keys(tweet)
    #         time.sleep(0.5)
    #         driver.find_element_by_xpath(post_xpath).click()
    #         time.sleep(0.5)
        elif 'you can sleep' in query:
            speak("thanks for using me sir , i am going to sleep")
            break
         


#         speak("sir , do you have any other work  ")    
if __name__ == '__main__':
     while True:
        permission = takecommand()
        if "wake up" in permission:
            main_run()
        elif 'good bye' in permission or 'you can stutdown' in permission or 'goodbye' in permission:
            speak("Thanks you sir , for using me  meet  you later ")    
            exit()
