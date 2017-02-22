#!/usr/bin/python
#author Amardeep Mishra

from __future__ import print_function
import time, sys, signal, atexit
from upm import pyupm_mpu9150 as sensorObj
from math import *
import time
import mraa
import dweepy
gyroscale=131
def main():
    gx_new=gy_new=gz_new=ax_new=ay_new=az_new=0
    #Defining Pwm pin
    pwm=mraa.Pwm(5)
    pwm.period_ms(20)
    pwm.enable(True)
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
    amar_sensor="mpu6050_sensor_data_amardeep_mishra"
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
        if(i<20):
            ax_new=ax_new+ax
            ay_new=ay_new+ay
            az_new=az_new+az
            aof_x=ax_new/i
            aof_y=ay_new/i
            aof_z=az_new/i
            gx_new=gx_new+gx
            gy_new=gy_new+gy
            gz_new=gz_new+gz
            gof_x=gx_new/i
            gof_y=gy_new/i
            gof_z=gz_new/i
            print("x_offset: ",gof_x, aof_x)
            print("y_offset: ",gof_y, aof_y)
            print("z_offset: ",gof_z, aof_z)
        else:
            g_actual_x=gx-gof_x
            g_actual_y=gy-gof_y
            g_actual_z=gz-gof_z
            gsx=g_actual_x/gyroscale
            gsy=g_actual_y/gyroscale
            gsz=g_actual_z/gyroscale
            a_actual_x=ax-aof_x
            a_actual_y=ay-aof_y
            a_actual_z=az-aof_z
        
            try:
                arx = (180/3.141592)*atan(ax/sqrt(pow(ay,2)+pow(az,2))) 
                ary = (180/3.141592)*atan(ay/sqrt(pow(ax,2)+pow(az,2)))
                arz = (180/3.141592)*atan(sqrt(pow(ay,2)+pow(ax,2))/az)
                if(i==20):
                    grx=arx
                    gry=ary
                    grz=arz
                else:
                    grx=grx+(tstep*gsx)
                    gry=gry+(tstep*gsy)
                    grz=grz+(tstep*gsz)
        
                rx = (0.96*arx)+(0.04*grx)
                ry = (0.96*ary)+(0.04*gry)
                rz = (0.96*arz)+(0.04*grz)
            except ZeroDivisionError:
                rx=0
                ry=0
                rz=0
        
            #print("filtered reading: roll: ",rx)
            #print("filtered reading: pitch: ",ry)
            #print("filtered reading: yaw",rz)
            #print("p :",g_actual_x, "l :",a_actual_x)
            #print("q :",g_actual_y, "m :",a_actual_y)
            #print("r :",g_actual_z,"n :",a_actual_z)
            
            dweet={"roll":rx,"pitch":ry,"yaw":rz}
            dweepy.dweet_for(amar_sensor,dweet)
            pwm.write(.019+.0005*(-ry))
        i+=1
        time.sleep(.1)
        
if __name__ == '__main__':
    amar_sensor="mpu6050_sensor_data_amardeep_mishra"
    main()
