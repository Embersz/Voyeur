import os
import time
from picamera import *
from subprocess import call
from time import sleep

voyeur = PiCamera()
global timestring

def voyeurPreviewON():  
    print("Preview: ON")
    voyeur.brightness = 50
    voyeur.contrast = 50
    voyeur.rotation = 0
    voyeur.start_preview(fullscreen=False, window=(325, 75, 840, 650))      #500, 200, 640, 480
    return

def voyeurPreviewOFF():
    voyeur.stop_preview()
    return


def voyeurPicture():
    timeString = time.strftime("%Y%m%d-%H%M%S")
    voyeur.capture('/home/pi/Desktop/Images/Voyeur%s.jpg' % timeString)
    return


def voyeurRecordON():
    global timestring
    timestring = time.strftime("%Y%m%d-%H%M%S")
    print ("recording started with time: ", timestring)
    voyeur.start_recording('/home/pi/Desktop/Video/Video1.h264')
    return

def voyeurRecordOFF():
    voyeur.stop_recording()
    global timestring
    print("Recording stopped with timestring: ", timestring)
    os.system("ffmpeg -framerate 30 -i /home/pi/Desktop/Video/Video1.h264 -c copy /home/pi/Desktop/Video/newvid%s.mp4" % timestring)
    print("here")
    return

def voyeurPlay():
    global timestring
    print("Playing recording: newvid",timestring)
    os.system("omxplayer /home/pi/Desktop/Video/newvid%s.mp4" % timestring)
    return

def voyeurBrightnessUP():
    voyeur.brightness += 2
    return


def voyeurBrightnessDOWN():
    voyeur.brightness -= 2
    return

def voyeurContrastUP():
    voyeur.contrast += 2
    return

def voyeurContrastDOWN():
    voyeur.contrast -= 2
    return

def widescreen():
    voyeur.resolution = (1024, 768)
    
def normal():
    voyeur.resolution = (1280, 720)

def rotate():
    voyeur.rotation += 90

    