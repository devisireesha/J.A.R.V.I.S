import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import webbrowser
import pyjokes
import time
import winsound
import cv2
import smtplib
from email.message import EmailMessage
import socket
import random
import os

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voice')
engine.setProperty('voice', voice[0])


def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        talk('Good morning sir..')
    elif 12 <= hour < 18:
        talk('Good Afternoon sir...')
    else:
        talk("Good Evening sir...")
        talk('initializing jaarvis')
        talk('jarvis installed successfully')
        talk('I am ready to take your commands')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening sir.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing sir.....")
        command = r.recognize_google(audio)
        print(f"Boss said: {command}\n")
    except Exception as e:
        print(e)
        print("Sir could you say that again...")
        talk('sorry boss could you say that again')
        return "None"
    return command


email_list = {
    # add these as your phonebook
    'nancy': 'nancy@gmail.com'
}
whatsapp_list = {  # same as here
    'nancy': 9889898998
}


def sendEmail(receiver, subject, message):
    socket.getaddrinfo('localhost', 8080)
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nancy@gmail.com', 'YourPasswordBoss:)')
    email = EmailMessage()
    email['From'] = 'nancy@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.close()


# Run Jarvis.

if __name__ == "__main__":

    wishme()

    while True:

        command = takecommand().lower()
        if 'wikipedia' in command:
            talk('Yes sir searching....')
            command = command.replace("Wikipedia", "")
            result = wikipedia.summary(command, sentences=1)
            talk('According to the wikipedia..')
            print(result)
            talk(result)

        elif 'play' in command:
            talk('Yes sir right away...')
            song = command.replace('play', '')
            talk('definately sir playing your song' + song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M%p')
            print(time)
            talk('sir the current time is' + time)

        elif 'girlfriend' in command:
            talk('no sir i am in relationship with python')

        elif 'siri' in command:
            talk('I kinda like siri but sir......do you have any suggestions ')

        elif 'seriously' in command:
            talk('yes sir.... i love her voice sir')

        elif 'shut up' in command:
            talk('okay sir not a problem')

        elif 'open google' in command:
            webbrowser.open("google.com")
            talk('Opening Google sir')

        elif 'open facebook' in command:
            webbrowser.open("facebook.com")
            talk('Opening Facebook sir')

        elif 'open stackoverflow' in command:
            webbrowser.open("stackoverflow.com")
            talk('Opening Stackoverflow sir')

        elif 'open whatsapp web' in command:
            webbrowser.open("Whatsapp Web")
            talk('Opening whatsapp web sir')

        elif 'open youtube' in command:
            webbrowser.open("Youtube")
            talk('Opening Youtube sir')

        elif 'joke' in command:
            talk(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif 'weather' in command:
            info = wikipedia.summary('weather', 1)
            print(info)
            talk(info)

        elif 'change your voice to female' in command:
            talk('Changing my voice to Female one sir...')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1])
            talk('sir ... changed my voice to female one')
            talk('and hows my new voice')

        elif ' change your voice to male' in command:
            talk('Changing my voice to male one sir...')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0])
            talk('sir ... changed my voice to male one')
            talk('and hows my new voice')

        elif 'stop clock' in command:
            talk('yes sir press start to start')
            talk('and stop to end the stopclock')
            choice = str(input("Enter start to start STOPCLOCK"))

            if choice == "start":
                starttimeH = datetime.datetime.now().hour
                starttimeM = datetime.datetime.now().min
                starttimeS = datetime.datetime.now().second

            choice2 = str(input("Enter stop to stop"))
            if choice2 == "stop":
                stoptimeH = datetime.datetime.now().hour
                stoptimeM = datetime.datetime.now().minute
                stoptimeS = datetime.datetime.now().second

            timetakenH = stoptimeH - starttimeH
            timetakenM = stoptimeM - starttimeM
            timetakenS = stoptimeS - starttimeS

            print("Time taken is")
            print(timetakenH)
            talk('Hours taken..')
            talk(timetakenH)
            print("Minutes taken is")
            print(timetakenM)
            talk('Minutes taken..')
            talk(timetakenM)
            print("Seconds taken is")
            print(timetakenS)
            talk('Seconds taken...')
            talk(timetakenS)

        elif 'countdown' in command:
            talk('sure sir......')
            talk('enter the seconds for countdown and press enter to start')


            def countdown(t):
                while t:
                    mins, secs = divmod(t, 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    print(timer, end="\r")
                    time.sleep(1)
                    t -= 1
                print("Time Up Sir...")
                talk('time up sir.....')
                winsound.PlaySound("*", winsound.SND_ALIAS)
                winsound.PlaySound("*", winsound.SND_ALIAS)


            t = input("Enter time in seconds:")
            countdown(int(t))

        elif 'set alarm' in command:
            talk('yes sir right away....')
            talk('please type the hours,to set the alarm sir...?')
            alarmH = int(input("What time do you want to wakeup?"))
            talk('At what minute sir....?')
            alarmM = int(input("At what Minute?"))
            talk('AM or PM sir?')
            amPm = str(input("am or pm?"))
            if (amPm == "pm"):
                alarmH = alarmH + 12
            while (1 == 1):
                if alarmH != datetime.datetime.now().hour or alarmM != datetime.datetime.now().minute:
                    pass
                else:
                    print("TIMEUPPPPP")
                    talk('sir time up sirrrrr')
                    talk('sir time upp')
                    winsound.PlaySound("*", winsound.SND_ALIAS)
                    winsound.PlaySound("*", winsound.SND_ALIAS)
                    winsound.PlaySound("*", winsound.SND_ALIAS)
                    winsound.PlaySound("*", winsound.SND_ALIAS)
                break

        elif 'open camera' in command:
            talk('yes sir right away....')
            print("Opening camera sir.....")
            talk('sir to close the camera press q on your keyboard')
            cam = cv2.VideoCapture(0)

            while cam.isOpened():
                ret, frame = cam.read()
                if cv2.waitKey(10) == ord('q'):
                    break
                cv2.imshow('camera', frame)

        elif 'activate motion capture' in command:
            print('Activating motion capture sir....')
            talk('activating motion capture sir....')
            talk('for Deactivating motion capture simply press q on your keyboard...')
            cam = cv2.VideoCapture(0)

            while cam.isOpened():
                ret, frame1 = cam.read()
                ret, frame2 = cam.read()
                diff = cv2.absdiff(frame1, frame2)
                gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
                blur = cv2.GaussianBlur(gray, (5, 5), 0)
                _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                dilated = cv2.dilate(thresh, None, iterations=3)
                contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                for c in contours:
                    if cv2.contourArea(c) < 2000:
                        continue
                        x, y, h, w = cv2.boundingRect(c)
                        cv2.rectangle(frame1, (x, y), (x + h, y + w), (0, 255, 0), 2)
                        winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)

                if cv2.waitKey(10) == ord('q'):
                    break
                cv2.imshow('Haula Cam', frame1)

        elif 'email' in command:
            try:
                talk('To whom should I sent the mail sir..?')
                name = takecommand()
                receiver = email_list[name]
                print(receiver)
                talk('sir what should I send as in subject ')
                subject = takecommand()
                talk('what would be the content to be sent sir')
                message = takecommand()
                sendEmail(receiver, subject, message)
                talk = 'Your Email has been sent sir...'
            except Exception as e:
                print(e)
                talk('I am sorry sir.. , I am not able to sent this Email')

        elif 'send whatsapp message' in command:
            talk('Yes sir absolutely...')
            try:
                talk('To whom should I send remember I can only sent, If the person is added to the dictionary sir ')
                to = takecommand()
                talk('what would be the message you want to send')
                content = takecommand()
                talk('at what hours do you want me to send ')
                when_H = takecommand()
                talk('at what minutes do you want me to send')
                when_M = takecommand()
                sendwhatsapp(to, content, when_H, when_M)
                pywhatkit.sendwhatmsg(to, content, when_H, when_M)
                talk('messsage sent sir')
            except Exception as e:
                print(e)
                talk('I am sorry sir...., I am not able to sent the message')

        elif 'shut down my' in command:
            talk('okay sir as you commanded')
            pywhatkit.shutdown(90)
            talk('the computer will be shutting down in less than t minus 90 seconds ')

        elif 'cancel shutdown' in command:
            talk('as you commanded to terminate shutdown')
            pywhatkit.cancelShutdown()
            talk('i have terminated the shutdown for you sir')
        elif 'Generate Password' in command:
            talk('Yes sir Generating Password in less than second')
            lower = 'abcdefghijklmnopqrstuvwxyz'
            upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            numbers = '1234567890'
            symbols = '[] {} : : " () @ # $ % '
            all = lower + upper + numbers + symbols
            length = 16
            password = "".join(random.sample(all, length))
            print(password)
        elif 'Thanks you' in command:
            talk('not a problem sir ')
            talk('its my responsibility sir')
        elif 'internet speed' in command:
            talk('yes sir right away')
            os.system('cmd /k "ping localhost"')
            talk(' the internet speed and the ping is displayed in the terminal')
        elif 'Rock paper scissors' in command:
            talk('yes sir type rock paper and scissors')
            talk('Installed the game')
            talk('remember type Quit with capital Q to Quit sir')
            game_list = ['Rock', 'Paper', 'Scissors']
            computer = c = 0
            command = p = 0
            print("Score : Computer" + str(c) + "Player" + str(p))
            run = True
            while run:
                computer_choice = random.choice(game_list)
                command = input("Rock, Paper, Scissor or Quit")
                if command == computer_choice:
                    print("Tie")
                elif command == 'Rock':
                    if computer_choice == 'Scissors':
                        print("You win!")
                        p += 1
                    else:
                        print("Computer win!")
                        c += 1
                elif command == 'Paper':
                    if computer_choice == 'Rock':
                        print("You win!")
                        p += 1
                    else:
                        print("Computer win!")
                        c += 1
                elif command == 'Scissor':
                    if computer_choice == 'Paper':
                        print("You win!")
                        p += 1
                    else:
                        print("Computer Win!")
                        c += 1
                elif command == 'Quit':
                    break
                else:
                    print("Wrong Command!")
            print("Player: " + command)
            print("Computer: " + computer_choice)
            print("")
            print("Score : Computer" + str(c) + "Player" + str(p))
            print("")
        elif 'light' in command:
            talk('turning the lamp on your left sir')
            talk('Turned the light sir as you commanded')
        elif 'light off' in command:
            talk('Turning the light off')
            talk('turned the light off sir as you commanded')
