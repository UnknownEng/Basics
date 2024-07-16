from djitellopy import tello
from time import sleep
me = tello.Tello()
me.connect()

print (me.get_battery())

me.takeoff()

# first try

me.send_rc_control(0,0,0,0)
sleep(1)

me.send_rc_control (0,50,0,0)
sleep(1)

me.send_rc_control (50,0,0,0)
sleep(1)

me.send_rc_controll (0,-50,0,0)
sleep(1)

me.send_rc_controll (-50,0,0,0)
sleep(1)

me.send_rc_control(0,0,0,0)
sleep(1)

me.land()
print("Run Sucessfull")

    