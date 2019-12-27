import sqlite3
import urllib
from sqlite3 import Error
import datetime
import webbrowser
import wikipedia
from pygame import mixer
import speech_recognition as sr
import smtplib
import tkinter
import random
import re
from chatterbot import ChatBot
chatbot = ChatBot("JIM")
import pyttsx3
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart

# For Making Tables and Connection Establishment(16-62)
def sql_connection_to_todo():
    try:
        con = sqlite3.connect('todos.db')
        return con
    except Error:
        print(Error)

def sql_table_todo(con):
    cursorObj = con.cursor()
    cursorObj.execute("create table if not exists todo(task text)")
    con.commit()



def sql_connection_to_timetable():
    try:
        con = sqlite3.connect('timetables.db')
        return con
    except Error:
        print(Error)

def sql_table_timetable(con):
    cursorObj = con.cursor()
    cursorObj.execute("create table if not exists timetable(job text,timeInHours text,day text)")
    con.commit()



def sql_connection_to_password():
    try:
        con = sqlite3.connect('passwords.db')
        return con
    except Error:
        print(Error)

def sql_table_password(con):
    cursorObj = con.cursor()
    cursorObj.execute("create table if not exists password(appSite text,pwd text)")
    con.commit()


# con = sql_connection_to_password()
# sql_table_password(con)
# con = sql_connection_to_timetable()
# sql_table_timetable(con)
# con = sql_connection_to_todo()
# sql_table_todo(con)


# Database Operations for all three(65-127)
def sql_insert_table_in_todo(con, text):
    cursorObj = con.cursor()
    txt = (text,)
    cursorObj.execute("INSERT INTO todo(task) VALUES(?)", txt)
    con.commit()

def sql_play_todo(con):
    count = 0
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM todo")
    rows = cursorObj.fetchall()
    for row in rows :
        print(row)

def sql_delete_from_todo(con,tex):
    cursorObj = con.cursor()
    text = (tex,)
    cursorObj.execute("delete from todo where task=(?)", text)
    con.commit()




def sql_insert_table_in_timetable(con, job, time, day):
    cursorObj = con.cursor()
    txt = (job, time, day,)
    cursorObj.execute("INSERT INTO timetable(job,timeInHours,day) VALUES(?,?,?)", txt)
    con.commit()

def sql_play_timetable(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM timetable")
    rows = cursorObj.fetchall()
    for row in rows :
        print(row)

def sql_delete_from_timetable(con,tex):
    cursorObj = con.cursor()
    text = (tex,)
    cursorObj.execute("delete from timetable where job=(?)",text)
    con.commit()



def sql_insert_table_in_password(con, appSite,pwd):
    cursorObj = con.cursor()
    txt = (appSite,pwd,)
    cursorObj.execute("INSERT INTO password(appSite,pwd) VALUES(?,?)", txt)
    con.commit()

def sql_play_password(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM password")
    rows = cursorObj.fetchall()
    for row in rows :
        print(row)

def sql_delete_from_password(con,tex):
    cursorObj = con.cursor()
    text = (tex,)
    cursorObj.execute("delete from password where appSite=(?)",text)
    con.commit()






import pyowm
engine = pyttsx3.init()

greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
question = ['How are you?', 'How are you doing?', 'how are you']
responses = ['Okay', "I'm fine"]
var1 = ['who made you', 'who created you']
var2 = ['I_was_created_by_right_in_his_computer.','xyz', 'Some_guy_whom_i_never_got_to_know.']
var3 = ['what time is it', 'what is the time', 'time']
var4 = ['who are you', 'what is you name']
cmd1 = ['open browser', 'open google']
cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
cmd4 = ['open youtube', 'i want to watch a video']
cmd5 = ['tell me the weather', 'weather', 'what about the weather']
cmd6 = ['exit', 'close', 'goodbye', 'nothing']
cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?']
colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
cmd8 = ['what is you favourite colour', 'what is your favourite color']
cmd9 = ['thank you']
repfr9 = ['youre welcome', 'glad i could help you']
cmd10 = ['open email', 'send email']
cmd11 = ['play me a game']
cmd12 = ['play songs', 'play me a song']

while True:
    now = datetime.datetime.now()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell me something:")
        audio = r.listen(source)
        try:
            print("You said:- " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say('I didnt get that. Rerun the code')
            engine.runAndWait()
        if r.recognize_google(audio) in greetings:
            random_greeting = random.choice(greetings)
            print(random_greeting)
            engine.say(random_greeting)
            engine.runAndWait()
        elif r.recognize_google(audio) in question:
            engine.say('I am fine')
            engine.runAndWait()
            print('I am fine')
        elif r.recognize_google(audio) in "chat":
            while True:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                            print("Speak: ")
                            audio = r.listen(source)
                            try:
                                audToTxt = r.recognize_google(audio)
                                if(str(audToTxt)=="bye"):
                                    break
                                print("getting passed " + audToTxt)
                                response = chatbot.get_response(str(audToTxt))
                                print("getting played " + (str(response)))
                                engine.say(str(response))
                                engine.runAndWait()
                            except:
                                print("Time Over,Thanks")

        elif r.recognize_google(audio) in "to do":
            while True:
                con = sql_connection_to_todo()
                sql_table_todo(con)
                sql_play_todo(con)
                engine = pyttsx3.init()
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Tell me to add, remove or play the task:")
                    audio = r.listen(source)
                    try:
                        print("You said:- " + r.recognize_google(audio))
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                        engine.say('I didnt get that. Rerun the code')
                        engine.runAndWait()
                    if r.recognize_google(audio) in "add":
                        engine.say("What is the task")
                        engine.runAndWait()
                        with sr.Microphone() as source2:
                            audio2 = r.listen(source2)
                            toSave = r.recognize_google(audio2)
                        sql_insert_table_in_todo(con, str(toSave))
                        engine.say("saved sucessfully")
                        engine.runAndWait()
                        # exit(0)
                    if r.recognize_google(audio) in "remove":
                        engine.say("What task to delete")
                        engine.runAndWait()
                        with sr.Microphone() as source2:
                            audio2 = r.listen(source2)
                            toDelete = r.recognize_google(audio2)
                        sql_delete_from_todo(con, str(toDelete))
                        engine.say("removed sucessfully")
                        engine.runAndWait()
                        # exit(0)
                    if r.recognize_google(audio) in "play":
                        engine.say("YOUR tasks are:")
                        cursorObj = con.cursor()
                        cursorObj.execute("SELECT * FROM todo")
                        rows = cursorObj.fetchall()
                        for row in rows:
                            engine.say(row)
                        engine.say("All the best")
                        engine.runAndWait()
                        # exit(0)
                    if r.recognize_google(audio) in "done":
                        engine.say("Bye")
                        engine.runAndWait()
                        break

        elif r.recognize_google(audio) in "time table":
            while True:
                con = sql_connection_to_timetable()
                sql_table_timetable(con)
                sql_play_timetable(con)
                engine = pyttsx3.init()
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Tell me to add, remove or play:")
                    audio = r.listen(source)
                    try:
                        print("You said:- " + r.recognize_google(audio))
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                        engine.say('I didnt get that. Rerun the code')
                        engine.runAndWait()
                    if r.recognize_google(audio) in "add":
                        engine.say("What is the job")
                        engine.runAndWait()
                        with sr.Microphone() as source2:
                            engine.say("job")
                            engine.runAndWait()
                            audio2 = r.listen(source2)
                            job = r.recognize_google(audio2)
                            engine.say("what is the time and day for the job")
                            engine.say("time")
                            engine.runAndWait()
                            audio2 = r.listen(source2)
                            time = r.recognize_google(audio2)
                            engine.say("day")
                            engine.runAndWait()
                            audio2 = r.listen(source2)
                            day = r.recognize_google(audio2)
                        sql_insert_table_in_timetable(con, str(job), str(time), str(day))   #job, time, day
                        engine.say("saved sucessfully")
                        engine.runAndWait()
                        # exit(0)
                    if r.recognize_google(audio) in "remove":
                        engine.say("What job to remove")
                        engine.runAndWait()
                        with sr.Microphone() as source2:
                            audio2 = r.listen(source2)
                            toDelete = r.recognize_google(audio2)
                        sql_delete_from_timetable(con, str(toDelete))
                        engine.say("delete sucessfully")
                        engine.runAndWait()
                        # exit(0)
                    if r.recognize_google(audio) in "play":
                        engine.say("YOU have to do :")
                        cursorObj = con.cursor()
                        cursorObj.execute("SELECT * FROM timetable")
                        rows = cursorObj.fetchall()
                        for row in rows:
                            engine.say(row[0]+" in " + row[1] + " on "+row[2])
                        engine.say("All the best")
                        engine.runAndWait()
                        # exit(0)
                    if r.recognize_google(audio) in "done":
                        engine.say("Bye")
                        engine.runAndWait()
                        break


        elif r.recognize_google(audio) in "password":
            while True:
                con = sql_connection_to_password()
                sql_table_password(con)
                sql_play_password(con)
                engine = pyttsx3.init()
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Tell me to save delete or play:")
                    audio = r.listen(source)
                    try:
                        print("You said:- " + r.recognize_google(audio))
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                        engine.say('I didnt get that. Rerun the code')
                        engine.runAndWait()
                    if r.recognize_google(audio) in "save":
                        engine.say("What is the App name and password")
                        engine.runAndWait()
                        with sr.Microphone() as source2:
                            print("Appname")
                            audio2 = r.listen(source2)
                            appName = r.recognize_google(audio2)
                            print("password")
                            audio2 = r.listen(source2)
                            password = r.recognize_google(audio2)
                        sql_insert_table_in_password(con, str(appName), str(password))   #appName and password
                        engine.say("saved sucessfully")
                        engine.runAndWait()
                        # exit(0)
                    if r.recognize_google(audio) in "delete":
                        engine.say("What password to delete")
                        engine.runAndWait()
                        with sr.Microphone() as source2:
                            audio2 = r.listen(source2)
                            toDelete = r.recognize_google(audio2)
                        sql_delete_from_password(con, str(toDelete))
                        engine.say("deleted sucessfully")
                        engine.runAndWait()
                        # exit(0)
                    if r.recognize_google(audio) in "play":
                        engine.say("YOUR tasks are:")
                        cursorObj = con.cursor()
                        cursorObj.execute("SELECT * FROM password")
                        rows = cursorObj.fetchall()
                        for row in rows:
                            engine.say("Your "+row[0]+" password is "+row[1])
                        engine.say("Your passwords are now completely safe and secure")
                        engine.runAndWait()
                        # exit(0)
                    if r.recognize_google(audio) in "done":
                        engine.say("Bye")
                        engine.runAndWait()
                        break



        elif r.recognize_google(audio) in var1:
            engine.say('I was made by xyz')
            engine.runAndWait()
            reply = random.choice(var2)
            print(reply)


        elif r.recognize_google(audio) in cmd9:
            print(random.choice(repfr9))
            engine.say(random.choice(repfr9))
            engine.runAndWait()


        elif r.recognize_google(audio) in cmd7:
            print(random.choice(colrep))
            engine.say(random.choice(colrep))
            engine.runAndWait()
            print('It keeps changing every micro second')
            engine.say('It keeps changing every micro second')
            engine.runAndWait()


        elif r.recognize_google(audio) in cmd8:
            print(random.choice(colrep))
            engine.say(random.choice(colrep))
            engine.runAndWait()
            print('It keeps changing every micro second')
            engine.say('It keeps changing every micro second')
            engine.runAndWait()


        elif r.recognize_google(audio) in cmd2:
            mixer.init()
            mixer.music.load("C:\\Users\\PRAJA\\Music\\TujheKitna.wav")
            mixer.music.play()


        elif r.recognize_google(audio) in var4:
            engine.say('I am edza your personal AI assistant')
            engine.runAndWait()


        elif r.recognize_google(audio) in cmd4:
            webbrowser.open('www.youtube.com')
        elif r.recognize_google(audio) in cmd6:
            print('see you later')
            engine.say('see you later')
            engine.runAndWait()
            exit()


        elif r.recognize_google(audio) in cmd5:
            owm = pyowm.OWM('d476d23a98383540baff0988e2f2ceeb')
            sf = owm.weather_at_place('Nagpur, IN')
            weather = sf.get_weather()
            temp = "temprature is " + str(weather.get_temperature('fahrenheit')['temp'])
            print(temp)
            engine.say(temp)
            engine.runAndWait()


        elif r.recognize_google(audio) in var3:
            print("Current date and time : ")
            print(now.strftime("The time is %H:%M"))
            engine.say(now.strftime("The time is %H:%M"))
            engine.runAndWait()


        elif r.recognize_google(audio) in cmd1:
            webbrowser.open('www.google.com')


        elif r.recognize_google(audio) in cmd3:
            jokrep = random.choice(jokes)
            engine.say(jokrep)
            engine.runAndWait()


        elif  r.recognize_google(audio) in cmd10:
            email_user = 'abxyz1311@gmail.com'
            #email_send = 'bobde.praja@gmail.com'

            engine.say("Enter the details")
            engine.runAndWait()
            #engine.say("Enter the senders email")
            #engine.runAndWait()
            #print("enter senders email")
           # x = r.listen(source)
            #email_user = r.recognize_google(x).replace(" ", "").lower()
           #print("You said:- " + email_user)
            engine.say("Enter the receivers email")
            engine.runAndWait()
            print("enter receivers email")
            y = r.listen(source)
            email_send = r.recognize_google(y).replace(" ", "").lower()
            print("You said:- " + email_send)
            engine.say("Enter the subject")
            engine.runAndWait()
            print("enter the subject")
            z = r.listen(source)
            Subject = r.recognize_google(z).lower()
            print("You said:- " + Subject)
            engine.say("Enter the body")
            engine.runAndWait()
            print("enter the body")
            w = r.listen(source)
            body = r.recognize_google(w).lower()
            print("You said:- " + body)
            mag = MIMEMultipart()
            mag['From'] = email_user
            mag['To'] = email_send
            mag['Subject'] = Subject
            mag.attach(MIMEText(body, 'plain'))
            text = mag.as_string()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_user, 'abcde@135')
            engine.say("Your email sent successfully")
            engine.runAndWait()
            server.sendmail(email_user, email_send, text)

            server.quit()
        elif r.recognize_google(audio) in cmd11:

            colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
                       'Yellow', 'Orange', 'White', 'Purple', 'Brown']
            score = 0

            # the game time left, initially 30 seconds.
            timeleft = 30


            # function that will start the game.
            def startGame(event):

                if timeleft == 30:
                    # start the countdown timer.
                    countdown()

                    # run the function to
                # choose the next colour.
                nextColour()

                # Function to choose and


            # display the next colour.
            def nextColour():

                # use the globally declared 'score'
                # and 'play' variables above.
                global score
                global timeleft

                # if a game is currently in play
                if timeleft > 0:

                    # make the text entry box active.
                    e.focus_set()

                    # if the colour typed is equal
                    # to the colour of the text
                    if e.get().lower() == colours[1].lower():
                        score += 1

                    # clear the text entry box.
                    e.delete(0, tkinter.END)

                    random.shuffle(colours)

                    # change the colour to type, by changing the
                    # text _and_ the colour to a random colour value
                    label.config(fg=str(colours[1]), text=str(colours[0]))

                    # update the score.
                    scoreLabel.config(text="Score: " + str(score))

                    # Countdown timer function


            def countdown():

                global timeleft

                # if a game is in play
                if timeleft > 0:
                    # decrement the timer.
                    timeleft -= 1

                    # update the time left label
                    timeLabel.config(text="Time left: "
                                          + str(timeleft))

                    # run the function again after 1 second.
                    timeLabel.after(1000, countdown)

                    # Driver Code


            # create a GUI window
            root = tkinter.Tk()

            # set the title
            root.title("COLORGAME")

            # set the size
            root.geometry("375x200")

            # add an instructions label
            instructions = tkinter.Label(root, text="Type in the colour"
                                                    "of the words, and not the word text!",
                                         font=('Helvetica', 12))
            instructions.pack()

            # add a score label
            scoreLabel = tkinter.Label(root, text="Press enter to start",
                                       font=('Helvetica', 12))
            scoreLabel.pack()

            # add a time left label
            timeLabel = tkinter.Label(root, text="Time left: " +
                                                 str(timeleft), font=('Helvetica', 12))

            timeLabel.pack()

            # add a label for displaying the colours
            label = tkinter.Label(root, font=('Helvetica', 60))
            label.pack()

            # add a text entry box for
            # typing in colours
            e = tkinter.Entry(root)

            # run the 'startGame' function
            # when the enter key is pressed
            root.bind('<Return>', startGame)
            e.pack()

            # set focus on the entry box
            e.focus_set()

            # start the GUI
            root.mainloop()


        elif r.recognize_google(audio) in cmd12:

            # get audio from microphone
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Which song you wanna listen:")
                engine.say("Which song you wanna listen:")
                engine.runAndWait()
                audio = r.listen(source)

            # get the text from audio
            msg = r.recognize_google(audio)

            # song name from user
            song = urllib.parse.urlencode({"search_query": msg})
            print(song)

            # fetch the ?v=query_string
            result = urllib.request.urlopen("http://www.youtube.com/results?" + song)
            print(result)

            # make the url of the first result song
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', result.read().decode())
            print(search_results)

            # make the final url of song selects the very first result from youtube result
            url = "http://www.youtube.com/watch?v=" + search_results[0]

            # play the song using webBrowser module which opens the browser
            # webbrowser.open(url, new = 1)
            webbrowser.open_new(url)



        else:
            engine.say("please wait")
            engine.runAndWait()
            print(wikipedia.summary(r.recognize_google(audio)))
            engine.say(wikipedia.summary(r.recognize_google(audio)))
            engine.runAndWait()
            userInput3 = input("or else search in google")
            webbrowser.open_new('www.google.com/search?q=' + userInput3)



# import speech_recognition as sr
# import pyttsx3
# from chatterbot import ChatBot
# import os
# from chatterbot.trainers import ListTrainer
# engine = pyttsx3.init()
# chatbot = ChatBot("JIM")
# r = sr.Recognizer()
# #
# # trainer = ListTrainer(chatbot)
# # for files in os.listdir('./english/'):
# #     data=open('./english/'+files,'r').readlines()
# # trainer.train(data)
#
#
#
# while True:
#     with sr.Microphone() as source:
#         print("Speak: ")
#         audio = r.listen(source)
#         try:
#             audToTxt = r.recognize_google(audio)
#             print("getting passed " + audToTxt)
#             response = chatbot.get_response(str(audToTxt))
#             print("getting played " + (str(response)))
#             engine.say(str(response))
#             engine.runAndWait()
#         except:
#             print("Time Over,Thanks")








