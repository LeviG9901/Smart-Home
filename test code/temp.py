# ** malnasuli.hu 2018 **
import time
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
    time.sleep(1)
GPIO.cleanup()