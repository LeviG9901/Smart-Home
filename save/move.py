import time,datetime
import RPi.GPIO as GPIO
import mysql.connector
import os
 
 
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
 print("ready")

 while GPIO.input(GPIO_PIR)==1:

   Current_State  = 0
   

 
 while 1:
     
   time.sleep(0.5)
   
   mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="callheni",
      database="DB_CPU"
   )
     
   mycursor = mydb.cursor()
   mycursor.execute("SELECT movesensor FROM test2 WHERE ID=12 ")

   myresult = mycursor.fetchall()

   y=str(myresult)
   y=(y.strip('('','')''['']'))
   y=int(y)
   print ("lekerdez",y)
   move=y
   
   
   
   if move==1:
    #time.sleep(0.005)
    Current_State = GPIO.input(GPIO_PIR)

    if Current_State==1 and Previous_State==0:


      mycursor = mydb.cursor()

      sql = "INSERT INTO move (time) VALUES (%s)"
      val = (datetime.datetime.now(),)
      mycursor.execute(sql, val)
      mydb.commit()

      print(mycursor.rowcount, "record inserted.")
      print (y)
      os.system("echo -e 'Subject: Riasztás\r\n\r\nRiasztás!' |msmtp --debug --from=default -t gvardian.levente@gmail.com")
      while y!=0:
       os.system("omxplayer 2.mp3 -o alsa")
 
       mydb = mysql.connector.connect(
       host="localhost",
       user="root",
       passwd="callheni",
       database="DB_CPU"
       )
     
       mycursor = mydb.cursor()
       mycursor.execute("SELECT movesensor FROM test2 WHERE ID=12 ")

       myresult = mycursor.fetchall()

       y=str(myresult)
       y=(y.strip('('','')''['']'))
       y=int(y)
       print ("lekerdez1",y)
       move=y
       
       
      Previous_State=1
    elif Current_State==0 and Previous_State==1:

     
     
      mycursor = mydb.cursor()

      sql = "INSERT INTO move (time) VALUES (%s)"
      val = (datetime.datetime.now(),)
      mycursor.execute(sql, val)

      mydb.commit()

      print(mycursor.rowcount, "record inserted.")
      os.system("echo -e 'Subject: Riasztás\r\n\r\nRiasztás!' |msmtp --debug --from=default -t gvardian.levente@gmail.com")
      while y!=0:
       os.system("omxplayer 2.mp3 -o alsa")

       mydb = mysql.connector.connect(
       host="localhost",
       user="root",
       passwd="callheni",
       database="DB_CPU"
       )
     
       mycursor = mydb.cursor()
       mycursor.execute("SELECT movesensor FROM test2 WHERE ID=12 ")

       myresult = mycursor.fetchall()

       y=str(myresult)
       y=(y.strip('('','')''['']'))
       y=int(y)
       print ("lekerdez2",y)
       move=y



      Previous_State=0

 

except KeyboardInterrupt:

 print ("  Quit")
 GPIO.cleanup()
 
 
 




