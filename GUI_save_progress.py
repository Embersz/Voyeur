from tkinter import *
from voyeur import *
from PIL import *
import picamera
import time
from time import sleep
import tkinter.messagebox as tm


duration = 5

class LoginFrame(Frame):
    def __init__(self, master):
        
        super().__init__(master)
        
        #self.title("Login")
        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)

        if username == "russ" and password == "pass":
            tm.showinfo("Login info", "Welcome Russell")
            self.quit()
              
        elif username == "alvin" and password == "password":
            
            tm.showinfo("Login info", "Welcome Alvin")
            
        elif username == "jordan" and password == "password":
            
            tm.showinfo("Login info", "Welcome Jordan")    
            
        elif username == "max" and password == "password":
            
            tm.showinfo("Login info", "Welcome Max")    
        else:
            tm.showerror("Login error", "Incorrect username")
            exit(0)
        

#login = Tk()
#lf = LoginFrame(login)
#login.mainloop()


def test():
    print("hello")
    
def bye():
    exit(0)


def GUI():
    root = Tk()  # main window
    root.title("2018")
    root.geometry("210x380")
    
    #canvas = Canvas(root,width=25, height=25)
    #canvas.pack()
    #img=PhotoImage(file="/home/pi/Desktop/Voyeur20180726-152935.gif")
    #canvas.create_image(10,10)

    label1 = Label(root, text="Security Camera")
    label1.grid(row=0, column=0, columnspan =4)

    button1 = Button(root, text="Camera On", fg="green", width=22, command=lambda:voyeurPreviewON())
    button1.grid(row=1, column=0, columnspan =4)

    button2 = Button(root, text="Camera Off", fg="red", width=22, command=lambda:voyeurPreviewOFF())
    button2.grid(row=2, column=0, columnspan =4)

    button3 = Button(root, text="Take a Photo", width=22, command=lambda: voyeurPicture())
    button3.grid(row=3, column=0, columnspan =4)

    button4 = Button(root, text="Start Video Record", width=22, command=lambda: voyeurRecordON())
    button4.grid(row=4, column=0, columnspan =4)

    button5 = Button(root, text="Stop Video Record", width=22,  command=lambda: voyeurRecordOFF())
    button5.grid(row=5, column=0, columnspan =4)

    button6 = Button(root, text="Turn Motion Detection ON", width=22)
    button6.grid(row=6, column=0, columnspan =4)

    button7 = Button(root, text="Turn Motion Detection OFF", width=22)
    button7.grid(row=7, column=0, columnspan =4)
    
    button8 = Button(root, text="brighness +", width=9, command=lambda: voyeurBrightnessUP())
    button8.grid(row=8, column=0, columnspan =2)
    
    button9 = Button(root, text="brighness -", width=9, command=lambda: voyeurBrightnessDOWN())
    button9.grid(row=8, column=2, columnspan =2)

    button10 = Button(root, text="contrast +", width=9, command=lambda: voyeurContrastUP())
    button10.grid(row=9, column=0, columnspan =2)
    
    button11 = Button(root, text="contrast -", width=9, command=lambda: voyeurContrastDOWN())
    button11.grid(row=9, column=2, columnspan =2)
    
    button12 = Button(root, text="Exit", width=22, command = lambda: bye())
    button12.grid(row=10, column=0, columnspan =4)
    
    label2 = Label(root, text="-------------------------------------------------")
    label2.grid(row=11, column=0, columnspan =4)
    
    label3 = Label(root, text="SERVO CONTROLS")
    label3.grid(row=12, column=0, columnspan =4)
    
    button13 = Button(root, text = "UP", width = 3)
    button13.grid(row=13, column=0)
    button14 = Button(root, text = "DOWN", width = 3)
    button14.grid(row=13, column=1)
    button15 = Button(root, text = "LEFT", width = 3)
    button15.grid(row=13, column=2)
    button16 = Button(root, text = "RIGHT", width = 3)
    button16.grid(row=13, column=3)
    
    root.mainloop()  # display the GUI
    voyeurPreviewOFF()

test()
GUI()

