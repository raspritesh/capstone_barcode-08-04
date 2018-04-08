import picamera
from subprocess import call
from datetime import datetime
from time import sleep

#our file path
filepath="/home/pi/Desktop/cookie/timestamp/"
pictot=4
piccount=0

while piccount<pictot:
	currenttime=datetime.now()
	pictime=currenttime.strftime("%Y.%m.%d-%H%M%S")
	picname=pictime+'.jpg'
	completefilepath=filepath+picname

	with picamera.PiCamera() as camera:
		camera.resolution=(1280,720)
		camera.capture(completefilepath)
		print("We have taken a picture")
	timestampmsg=currenttime.strftime("%Y.%m.%d-%H%M%S")
	timestampcmd="/usr/bin/convert "+ completefilepath + " -pointsize 36 -fill red -annotate +700+650 ' " + timestampmsg +" ' "+completefilepath
	call([timestampcmd],shell=True)
	print "we hv timestamped our picture"
	piccount+=1
	sleep(5)

	
