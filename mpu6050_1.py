#!/usr/bin/python
#author Amardeep Mishra(IIT Madras) 08/01/2017
#I have modified the upm/mpu60x0.py to calculate angles.In order to use this code one must have upm installed 

from __future__ import print_function
import time, sys, signal, atexit
from upm import pyupm_mpu9150 as sensorObj
from math import *
import time
def main():
    # Instantiate an MPU60X0 on I2C bus 0
    sensor = sensorObj.MPU60X0()
    t=time.time()
    gyroscale=131
    ## Exit handlers ##
    # This function stops python from printing a stacktrace when you hit control-C
    def SIGINTHandler(signum, frame):
        raise SystemExit

    # This function lets you run code on exit
    def exitHandler():
        print("Exiting")
        sys.exit(0)

    # Register exit handlers
    atexit.register(exitHandler)
    signal.signal(signal.SIGINT, SIGINTHandler)

    sensor.init()

    x = sensorObj.new_floatp()
    y = sensorObj.new_floatp()
    z = sensorObj.new_floatp()
    i=1
    while (1):
        tprev=t
        t=time.time()
        tstep=(t-tprev)
        sensor.update()
        sensor.getAccelerometer(x, y, z)
        ax=sensorObj.floatp_value(x)
        ay=sensorObj.floatp_value(y)
        az=sensorObj.floatp_value(z)
        
        sensor.getGyroscope(x, y, z)
        gx=sensorObj.floatp_value(x)
        gy=sensorObj.floatp_value(y)
        gz=sensorObj.floatp_value(z)

        gsx=gx/gyroscale
        gsy=gy/gyroscale
        gsz=gz/gyroscale
        
        try:
            arx = (180/3.141592) * atan(ax / sqrt(pow(ay, 2) + pow(az, 2))) 
            ary = (180/3.141592) * atan(ay / sqrt(pow(ax, 2) +pow(az, 2)))
            arz = (180/3.141592) * atan(sqrt(pow(ay,2) + pow(ax,2)) / az)
            if(i==1):
                grx=arx
                gry=ary
                grz=arz
            else:
                grx=grx+(tstep*gsx)
                gry=gry+(tstep*gsy)
                grz=grz+(tstep*gsz)
        
            rx = (0.96 * arx) + (0.04 * grx)
            ry = (0.96 * ary) + (0.04 * gry)
            rz = (0.96 * arz) + (0.04 * grz)
        except ZeroDivisionError:
            rx=0
            ry=0
            rz=0
        print("filtered reading: roll: ",rx)
        print("filtered reading: pitch: ",ry)
        print("filtered reading: yaw",rz)
        
        time.sleep(.1)

if __name__ == '__main__':
    main()
