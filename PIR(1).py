


import time,datetime

import RPi.GPIO as GPIO

 

GPIO.setmode(GPIO.BCM)

 


GPIO_PIR = 9

 

print "PIR Module Holding Time Test (CTRL-C to exit)"

 



GPIO.setup(GPIO_PIR,GPIO.IN)    

 

Current_State  = 0

Previous_State = 0

try:

 

 print "Waiting for PIR to settle ..."

 


 while GPIO.input(GPIO_PIR)==1:

   Current_State  = 0

 

 print "  Ready"

 stop_time=time.time()


 while True :

   time.sleep(0.005)

  

 

   Current_State = GPIO.input(GPIO_PIR)

 

   if Current_State==1 and Previous_State==0:

     # PIR is triggered

     start_time=time.time()

     print datetime.datetime.now(),

     print "  Moving ",

     idle_time=int(start_time-stop_time)

     print " (Idle time : " + str(idle_time) + " secs)"


     Previous_State=1

   elif Current_State==0 and Previous_State==1:


     stop_time=time.time()

     print datetime.datetime.now(),

     print "  Standby  ",

     elapsed_time=int(stop_time-start_time)

     print " (Elapsed time : " + str(elapsed_time) + " secs)"

     Previous_State=0

 

except KeyboardInterrupt:

 print "  Quit"


 GPIO.cleanup()
