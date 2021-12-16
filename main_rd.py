from ctypes import string_at
from instaloader.exceptions import QueryReturnedBadRequestException
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
# import pywhatkit as kit 
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
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
from PyQt5.uic import loadUiType
from guiFile import Ui_MainWindow
import operator
import requests
from bs4 import BeautifulSoup
from pywikihow import WikiHow, search_wikihow



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

#run the str into adio
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#take command function which takes trhe command from user==>  voice ko text mai convert kr ta


#wish function which wish you according to time
def wish():
    hour = int(datetime.datetime.now().hour)
    # min = int(datetime.datetime.now().min)
    # amPm = datetime.datetime.now().astimezone
    if hour>=0 and hour<=12:
       speak(f"Good Morning Sir   ")
    elif hour>12 and hour<18:
        speak(f"Good Afternoon Sir   ")
    else:
        speak(f"Good evening Sir  ")
    speak("I am Jarvis Sir , please tell me how i can help   ")    

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rajatdelldhiman@gmail.com','passward')
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

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        # self.TaskExecution()

    def run(self):
        # self.TaskExecution()
        speak("please say wake up to continue sir ")
        while True:
            self.query = self.takecommand()
            if'wake up' in self.query or 'are you there' in self.query:
                self.TaskExecution()


    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......._______......_____")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=10000, phrase_time_limit=5)
        try:
            print("Recognition.......______........")
            self.query = r.recognize_google(audio, language='en-in')
            print(f" User said : {self.query}")
        except Exception as e:
            speak("Say that again please.....")
            return "none"
        self.query = self.query.lower()     
        return self.query

    def TaskExecution(self):

        wish()
        while True:
        

            self.query = self.takecommand().lower()
    
            if 'open notepad' in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)
            elif"hellow" in self.query :
                speak("hellow sir , how I can help you ")
            elif'how are you' in self.query:
                speak("i am fine sir , how is your day ")                        
            elif 'open visual studio code' in self.query:
                npath = r"C:\Users\rajat\AppData\Local\Programs\Microsoft VS Code\code.exe"
                os.startfile(npath)
            elif 'open pycharm' in self.query:
                npath = r"C:\Program Files\JetBrains\PyCharm Community Edition 2021.1.1\bin\pycharm64.exe"
                os.startfile(npath)
            elif 'open typing master' in self.query:
                npath = r"C:\Program Files (x86)\TypingMaster\tmaster.exe"
                os.startfile(npath)
            elif 'open command prompt' in self.query:
                os.startfile('C:\\Windows\\system32\\cmd.exe')
            elif 'open camera' in self.query :
                cap = cv2.VideoCapture(0)
                speak("sir mobile camera will opened soon ")
                while True:
                    ret,img = cap.read()
                    cv2.imshow('webcam',img)
                    k = cv2.waitKey(50) 
                    if k==27:
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif 'play music' in self.query:
                music_dir = 'R:\\music hindi'
                songs = os.listdir(music_dir)
                rd = random.choice(songs)      
                os.startfile(os.path.join(music_dir,rd))

            elif 'ip address' in self.query:
                ip = get(r'https://api.ipify.org').text
                speak(f"your ip address is {ip}")

            elif  'wikipedia' in self.query:    
                speak("searching  wikipedia ...")
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query,sentences=2)
                speak("According to wikipedia ")
                speak(results)
                # print(results)

            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
                speak("yes i opened it ....") 

            elif 'open facebook' in self.query:
                webbrowser.open("www.facebook.com")
                speak("yes i opened it ....")

            elif 'open instagram' in self.query:
                webbrowser.open("www.instagram.com")
                speak("yes i opened it ....")

            elif 'open google' in self.query:
                speak("Sir what should i search on google")
                cm =self.takecommand().lower() 
                webbrowser.open(f"{cm}")
                speak("yes i opened it ....")

            elif 'open linked in' in self.query:
                webbrowser.open("www.linkedin.com")
                speak("yes i opened it ....")

            elif 'open whatsapp' in self.query:
                webbrowser.open(r"https://web.whatsapp.com/")
                speak("yes i opened it ....")

            elif 'open gmail' in self.query:
                webbrowser.open("www.gmail.com")
                speak("yes i opened it ....")

            elif 'open stack overflow' in self.query:
                webbrowser.open("www.stackoverflow.com")
                speak("yes i opened it ....")  

            elif 'open my website' in self.query:
                webbrowser.open(r"https://rajatdelldhiman.wixsite.com/rdsoftware")
                speak("yes i opened it ....")

            elif 'send whatsapp message' in self.query:
                try:
                    speak("Enter the mobile number to whome message to be sent ")
                    num = input()
                    speak("please speak your message")
                    msg = self.takecommand()
                    ptimehr = int(datetime.datetime.now().hour) 
                    ptimemin = int(datetime.datetime.now().minute)+2
                    kit.sendwhatmsg(f"+91{num}",msg,ptimehr,ptimemin)
                    speak("sir i send the message on given number ")
                except Exception as e:
                    speak(e)
                    speak("Unable to snd the whatsapp message , sorry sir ")    


            elif 'play music on youtube'in self.query:
                speak("speak the song name which you want to listen")
                sg = self.takecommand()
                kit.playonyt(sg)

            elif 'email to' in self.query:
                try:
                    speak("what should I say ?")
                    datamsg = self.takecommand().lower()
                    speak("To whom i send this mail Sir please input the username or id  ")
                    emailnam=input() 
                    sendEmail(emailnam,datamsg)
                    speak("Mail has been sent sucessfully")
                except Exception as e:
                    print(e) 
                    speak("sorry sir I am unable to send the the mail")

            elif 'you can sleep' in self.query or 'no thanks'in self.query:
                speak("thanks for using me sir , i am going to sleep sir")    
                break
                #starting listening loop
            elif'goodbye'in self.query or 'good bye' in self.query or'shutdown yourself' in self.query:
                speak("thank you sir for using me , meet you later , goodbye sir ")    
                exit()
            elif 'close notepad' in self.query :
                speak("ok sir closing notpad ")
                os.system("taskkill /f /im notepad.exe")
                #mobi;le cam 
            elif 'open mobile camera' in self.query or'opne phone camera' in self.query:
                import numpy as np
                import urllib.request
                URL = "http://192.168.43.1:8080/shot.jpg"
                try:
                    while True: 
                        img_arr= np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint10)
                        img = cv2.imdecode(img_arr,-1)
                        cv2.imshow('IPWebcam',img)
                        q = cv2.waitKey(1)
                        if q ==ord("q"):
                            break;

                        cv2.destroyAllWindows()
                except Exception as e:
                    speak("sorry sir  i am unable to open mobile camera because of low network ")

            # elif 'set alarm' in self.query :
            #     time_now = int(datetime.datetime.now().hour)
            #     speak("sir please input the time for alarm ")
            #     time_user = input("enter the time exaple 21:2  : ")
            #     if time_now == time_user :
            #         music = r'R:\music hindi'
            #         songs_alarm = os.listdir(music)
            #         os.startfile(os.path.join(music,songs_alarm[3]))
            #         #joke in english
            elif 'tell me a joke'in self.query:
                joke = pyjokes.get_joke()
                speak(joke)
                #shutdiown
            elif 'shut down the system' in self.query:
                os.system("shutdown /s /t 5")    

            elif 'restart the system' in self.query:
                os.system("shutdown /r /t 5")

            elif 'sleep the system' in self.query:
                os.system("rundll32.exe powrprof.dll,setSuspendState 0,1,0")       

            #switch the window
            elif 'switch the window' in self.query :
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
            elif 'tell me news' in self.query:
                speak("please wait sir for whill serching for news ")
                news()

            elif 'tell my location' in self.query or 'where i am' in self.query:
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
    

            elif 'instagram profile'in self.query or 'profile on instagram'in self.query :
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
               
               
                #this is not done in other file -- this is for oral cal.
            elif'do some calculation'in self.query or "can you calculate" in self.query:
                r = sr.Recognizer()        
                with sr.Microphone() as source:
                    speak("say what you want to calculate , example 3 plus 7")
                    print("listtening...........")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string= r.recognize_google(audio)
                print(my_string)    
                def get_operator_fn(op):
                    return{
                        '+':operator.add,
                        '-':operator.sub,
                        '*':operator.mul,
                        '/':operator.__truediv__,
                    }[op]
                def eval_binary_expr(op1,oper,op2):
                    op1,op2 = int(op1),int(op2)    
                    return get_operator_fn(oper)(oper,op2)
                speak("your result is ")
                speak(eval_binary_expr(*(my_string.split())))

            elif'temperature' in self.query:
                speak("sir in which city you want to know the temperture , please input the name")    
                search = input("enter the city name : ")
                url = f"https://www.google.com/search?q=temperture in {search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f" current temperture in {search} is {temp}")
            elif 'want to search something special' in self.query or 'want to know something'in self.query or  'special mod'in self.query:
                speak("sir special mod is activated , you can ask anything how why  ")
                while True:
                    speak("please ask anything , what you want to know")
                    how = self.takecommand()
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

            elif'how much power left' in self.query or 'how much power we have'in self.query or 'battery'in self.query:
                import psutil
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"sir our system have {percentage} percent battery")

            elif'internet speed' in self.query:
                import speedtest
                speak("sir wait for little bit time , i am checking ")
                st = speedtest.Speedtest()
                dI= st.download()
                uI= st.upload()
                speak(
                    f"sir we have {dI} bit per second downloading speed and {uI} bit per second uploading speed")
            
            elif 'volume up' in self.query:
                pyautogui.press("volumeup")
                speak("sir i have done volume up , now i am ready for next command")
            elif 'volume down' in self.query:
                pyautogui.press("volumedown")
                speak("sir i have done volume down, now i am ready for next command")
            elif 'volume mute' in self.query or 'mute' in self.query:
                pyautogui.press("volumemute")  
                speak("sir i have done volume mute , now i am ready for next command") 
            # going set the alarm usimg myalarm pakage
                
            elif 'set alarm' in self.query:
                # speak("sir please tell me the time to set alarm , for example set alarm to 5:33 am")
                speak("sir input the timing such as 5:33 PM")
                tt = input("input timing  : ")
                # tt = self.takecommand()
                # tt = tt.replace("set alarm to ","")
                # tt = tt.replace(".","")
                # tt = tt.upper()
                import MyAlarm
                MyAlarm.alarm(tt)



            #code to snd sms
            elif'send sms'in self.query or 'send sms message' in self.query:
                speak("we are going to send sms sir soon")
                # import twilio  
                from twilio.rest import Client


               
                account_sid = 'ACef7039b169a9599f5045a2707b502faa'
                auth_token = '8008f2d251caeb6718c58e33a1be1614'#use your own id 
                client = Client(account_sid, auth_token)
                speak("sir please speak ,what is message that need to send  ")
                data_msg = self.takecommand().lower()
                
                # num_snd = int(input("Enter the phone number  : "))
                message = client.messages \
                    .create(
                        body=f'{data_msg}',
                        from_='+18508087104',
                        to='+918607749965'
                    )
                print(message.sid)
                speak("sir sms is send , now i am ready to take next command")
            elif'make a call' in self.query or 'call now' in self.query:
                speak("sir soon , we are going to make a call ")
                # import twilio
                from twilio.rest import Client

                account_sid = 'ACef7039b169a9599f5045a2707b502faa'
                auth_token = '8008f2d251caeb6718c58e33a1be1614'  # use your own id i have to change it before uploading
                client = Client(account_sid, auth_token)
                speak("sir please speak ,what should narrate during call ")
                data_call = self.takecommand().lower()

                message = client.calls \
                    .create(
                        twiml=f'<Rresponse><Say> {data_call} </Say></Rresponse>', 
                        from_='+18508087104',
                        to='+918607749965'
                    )
                print(message.sid)
                speak("sir call is done  , now i am ready to take next command")

            
           
            elif 'read pdf'in self.query or 'read my pdf'in self.query :
                read_pdf()

            elif 'hide all files' in self.query or 'hide folder'in self.query or 'visible for everyone'in self.query:
                speak("sir please tell me you weant to hide the files or folder or want to make visible for everyone ")        
                condition = self.takecommand().lower()
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




            elif'can you tweet for me' in self.query or 'can you make post on tweet' in self.query:
    

                email, password = account_info()
                speak("sir what i can tweet for you ")
                tweet = self.takecommand().lower()

                options = Options()
                options.add_argument("start-maximized")
                driver = webdriver.Chrome(options=options)

                driver.get(r'https://twitter.com/login')
                email_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
                passward_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
                login_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div'
                time.sleep(2)

                driver.find_element_by_xpath(email_xpath).send_keys(email)
                time.sleep( 0.5)
                driver.find_element_by_xpath(passward_xpath).send_keys(password)
                time.sleep(0.5)
                driver.find_element_by_xpath(login_xpath).click()
                time.sleep(0.5)

                tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
                type_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
                post_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span'
                time.sleep(2)
                driver.find_element_by_xpath(tweet_xpath).click()
                time.sleep(0.5)
                driver.find_element_by_xpath(type_xpath).send_keys(tweet)
                time.sleep(0.5)
                driver.find_element_by_xpath(post_xpath).click()
                time.sleep(0.5)
        


            speak("sir , do you have any other work  ")    

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.startTask) 
        self.ui.pushButton_3.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie(r"C:/Users/rajat/OneDrive/Desktop/main.gif") 
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(r"C:/Users/rajat/OneDrive/Desktop/staus.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText(label_date)


app = QApplication(sys.argv)
guiFile = Main()
guiFile.show()
exit(app.exec_())
