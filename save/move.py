import time,datetime
import RPi.GPIO as GPIO
import mysql.connector
 
 
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="callheni",
  database="DB_CPU"
)


GPIO.setmode(GPIO.BCM) 
GPIO_PIR = 7
GPIO.setup(GPIO_PIR,GPIO.IN)    

 
Current_State  = 0
Previous_State = 0
try:


 while GPIO.input(GPIO_PIR)==1:

   Current_State  = 0
   
   print ("  Ready")
 #stop_time=time.time()


 while True :

   time.sleep(0.005)
   Current_State = GPIO.input(GPIO_PIR)

   if Current_State==1 and Previous_State==0:

     #start_time=time.time()
    # print (datetime.datetime.now(),)

     mycursor = mydb.cursor()

     sql = "INSERT INTO move (time) VALUES (%s)"
     val = (datetime.datetime.now(),)
     mycursor.execute(sql, val)

     mydb.commit()

     print(mycursor.rowcount, "record inserted.")
     



    # print ("  Moving ",)

    # idle_time=int(start_time-stop_time)

    # print (" (Idle time : " + str(idle_time) + " secs)")

  

     Previous_State=1

   elif Current_State==0 and Previous_State==1:



    # stop_time=time.time()

    #print (datetime.datetime.now(),)
     
     
     mycursor = mydb.cursor()

     sql = "INSERT INTO move (time) VALUES (%s)"
     val = (datetime.datetime.now(),)
     mycursor.execute(sql, val)

     mydb.commit()

     print(mycursor.rowcount, "record inserted.")
     
     

    # print ("  Standby  "),

    # elapsed_time=int(stop_time-start_time)

    # print (" (Elapsed time : " + str(elapsed_time) + " secs)")

     Previous_State=0

 

except KeyboardInterrupt:

 print ("  Quit")
 GPIO.cleanup()
 
 
 




