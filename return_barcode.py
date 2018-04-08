import picamera
from subprocess import call
from datetime import datetime
from time import sleep
import os
import subprocess
#our file path
import serial
import types
import ir

while True:
        input=ir.detection()
	
        if input is 1:
                
                with picamera.PiCamera() as camera:
                        camera.resolution=(1280,720)
                        if input is 1:
                                camera.capture('img1.jpg')
                #os.system("python p1.py")
                os.system("python detect_barcode2_all.py")                
                #os.system("python detect_barcode3_all.py")
                #output = open( tmp_log_file, 'r' ).read()
                
                sleep(1)
        
	
