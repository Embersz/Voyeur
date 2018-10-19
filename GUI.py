import time
import os
import subprocess
import tkinter as tk
import tkinter.messagebox as tm
from tkinter import *
from PIL import Image, ImageTk
from PIL import *
from PIL import Image
#from voyeur import *
from servosix import ServoSix
from time import sleep


global timestring
verDeg = 90.0
horDeg = 90.0
panDeg = 90.0
shift = 0.0
duration = 5

def slideShow():
    voyeurPreviewOFF()
    os.system("feh /home/pi/Desktop/Images/ -d -x -g 840x630+325+75 --cycle-once")
   
def bye():
    voyeurPreviewOFF()
    exit()
         
def up(ssV):
    global verDeg
    verDeg -= 5
    ssV.set_servo(2, verDeg)

def down(ssV):
    global verDeg
    verDeg += 5
    ssV.set_servo(2, verDeg)

def left(ssH):
    global horDeg
    horDeg += 5
    ssH.set_servo(1, horDeg)

def right(ssH):
    global horDeg
    horDeg -= 5
    ssH.set_servo(1, horDeg)

def center(ssH):
    print("gimbal centered")
    ssH.set_servo(1, 90)
    ssH.set_servo(2, 90)

def countdown(n):
    while n > 0:
        n = n - 1

def pan(ssP):
    print("inside count")
    global horDeg
    global shift
    shift = 1.0
    i = 0.0
    dir = 1
    while i < 84:
        countdown(100000)
        if horDeg > 110:
            dir = -1
        elif horDeg < 70:
            dir = 1
        horDeg += (shift * dir)
        print(horDeg)
        ssP.set_servo(1, horDeg)
        i += 1

def playVid():
    voyeurPreviewOFF()
    voyeurPlay();


def GUI():
    #from voyeur import *
    import voyeur
    root = tk.Tk()  # main window
    root.title("Team 1 - San Marcos")
    root.geometry("1270x650+0+0")  

    label1 = Label(root, text="Security Camera")
    label1.grid(row=0, column=0, columnspan=4)
    

    button1 = Button(root, text="Camera On", width=22, command=lambda: voyeurPreviewON())
    button1.grid(row=1, column=0, columnspan=4)

    button2 = Button(root, text="Camera Off", width=22, command=lambda: voyeurPreviewOFF())
    button2.grid(row=2, column=0, columnspan=4)

    button3 = Button(root, text="Take a Photo", width=22, command=lambda: voyeurPicture())
    button3.grid(row=3, column=0, columnspan=4)
    
    button4 = Button(root, text="Slideshow - Images Folder", width=22, command=lambda: slideShow())
    button4.grid(row=4, column=0, columnspan=4)

    button5 = Button(root, text="Start Video Record", width=22, command=lambda: voyeurRecordON())
    button5.grid(row=5, column=0, columnspan=4)

    button6 = Button(root, text="Stop Video Record", width=22, command=lambda: voyeurRecordOFF())
    button6.grid(row=6, column=0, columnspan=4)

    button7 = Button(root, text="Play Last Recorded Video", width=22, command=lambda: playVid())  
    button7.grid(row=7, column=0, columnspan=4)

    button8 = Button(root, text=" 4:3 ", width=9, command=lambda: widescreen())
    button8.grid(row=8, column=0, columnspan=2)

    button9 = Button(root, text=" 16:9 ", width=9, command=lambda: normal())
    button9.grid(row=8, column=2, columnspan=2)

    button10 = Button(root, text="brightness +", width=9, command=lambda: voyeurBrightnessUP())
    button10.grid(row=9, column=0, columnspan=2)

    button11 = Button(root, text="brightness -", width=9, command=lambda: voyeurBrightnessDOWN())
    button11.grid(row=9, column=2, columnspan=2)

    button12 = Button(root, text="contrast +", width=9, command=lambda: voyeurContrastUP())
    button12.grid(row=10, column=0, columnspan=2)

    button13 = Button(root, text="contrast -", width=9, command=lambda: voyeurContrastDOWN())
    button13.grid(row=10, column=2, columnspan=2)

    button14 = Button(root, text="Exit", width=22, command=lambda: bye())
    button14.grid(row=11, column=0, columnspan=4)

    label2 = Label(root, text="-------------------------------------------------")
    label2.grid(row=12, column=0, columnspan=4)

    ss = ServoSix()
    ss.set_servo(1, 90)
    ss.set_servo(2, 90)

    label3 = Label(root, text=" ")
    label3.grid(row=13, column=0, columnspan=4)

    button13_1 = Button(root, text="90 deg", width=3, command=lambda: rotate())
    button13_1.grid(row=14, column=0)
    button19 = Button(root, text="Center", width=6, command=lambda: center(ss))
    button19.grid(row=14, column=1, columnspan=2)
    button20 = Button(root, text="Pan", width=3, command=lambda: pan(ss))
    button20.grid(row=14, column=3)

    label3 = Label(root, text="SERVO CONTROLS")
    label3.grid(row=13, column=1, columnspan=2)

    button13 = Button(root, text="UP", width=3, command=lambda: up(ss))
    button13.grid(row=15, column=0)
    button14 = Button(root, text="DOWN", width=3, command=lambda: down(ss))
    button14.grid(row=15, column=1)
    button15 = Button(root, text="LEFT", width=3, command=lambda: left(ss))
    button15.grid(row=15, column=2)
    button16 = Button(root, text="RIGHT", width=3, command=lambda: right(ss))
    button16.grid(row=15, column=3)
    
    label4 = Label(root, text="")
    label4.grid(row=16, column=1, columnspan=2)
    
    label5 = Label(root, text="Team Voyeur")
    label5.grid(row=17, column=1, columnspan=2)
    
    label6 = Label(root, text="")
    label6.grid(row=18, column=1, columnspan=2)
    
    label7 = Label(root, text="4398 SM Team #1")
    label7.grid(row=19, column=1, columnspan=2)
    
    label7 = Label(root, text="")
    label7.grid(row=20, column=1, columnspan=2)
    
    label7 = Label(root, text="<<< Authors >>>")
    label7.grid(row=21, column=1, columnspan=2)
    
    label8 = Label(root, text="Alvin Romualdo")
    label8.grid(row=22, column=1, columnspan=2)
    
    label9 = Label(root, text="Russell Bennight")
    label9.grid(row=23, column=1, columnspan=2)
    
    label10 = Label(root, text="Jordan Al Sahili")
    label10.grid(row=24, column=1, columnspan=2)
    
    label11 = Label(root, text="Maxwell Yi")
    label11.grid(row=25, column=1, columnspan=2)
    
    img = Image.open("/home/pi/Desktop/Under Construction/Spyguy")
    img = img.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image = img)
    panel.grid(row=17, column=0, columnspan=4)
    
    root.mainloop()  # display the GUI
    voyeurPreviewOFF()

#GUI()
class LoginFrame(Frame):
    def __init__(self, master):

        super().__init__(master)

        # self.title("Login")
        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        #self.checkbox = Checkbutton(self, text="Keep me logged in")
        #self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "russ" and password == "pass":
            tm.showinfo("Login info", "Welcome Russell")
            self.quit()

        elif username == "alvin" and password == "pass":
            tm.showinfo("Login info", "Welcome Alvin")

        elif username == "jordan" and password == "password":
            tm.showinfo("Login info", "Welcome Jordan")

        elif username == "max" and password == "password":
            tm.showinfo("Login info", "Welcome Max")
            
        elif username == "admin" and password == "admin":
            tm.showinfo("Login info", "Welcome Admin")
            
        else:
            tm.showerror("Login error", "Incorrect username")
            exit(0)
            
        #os.system("pyton pi_surveillance.py --conf conf.json") 
        #subprocess.call(["python", "pi_surveillance.py", "--conf", "conf.json"]) 
        GUI()
            
login = Tk()
login.title("Login")
login.geometry("220x100+600+300")
IF = LoginFrame(login)
login.mainloop()

