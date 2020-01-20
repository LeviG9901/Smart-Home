import mysql.connector
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)




mydb = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="callheni",
    database="DB_CPU"
)

templimit = 0

while 1:
    tempfile = open("/sys/bus/w1/devices/28-0416869d5aff/w1_slave")
    thetext = tempfile.read()
    tempfile.close()
    # get the temperature
    tempdata = thetext.split("\n")[1].split(" ")[9]
    temperature = float(tempdata[2:])
    temperature = temperature / 1000
    # print out the temperature
    print (temperature)
    time.sleep(3)


    if temperature<templimit:
        GPIO.output(17,GPIO.HIGH)
    else:
        GPIO.output(17,GPIO.LOW)


    mycursor = mydb.cursor()

    val=(temperature, )
    sqltemp = "UPDATE test2 SET szam= %s WHERE ID=12 "
    mycursor.execute(sqltemp, val)
    mydb.commit()
 
    
    mycursor.execute("SELECT templimit FROM test2 WHERE ID=12 ")
    
    myresult = mycursor.fetchall()
    
    x=str(myresult)
    x=(x.strip('('','')''['']'))
    x=int(x)
    print (x)
    templimit=x

print(mycursor.rowcount, "record inserted.")