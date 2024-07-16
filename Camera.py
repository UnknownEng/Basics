from djitellopy import tello
import cv2  #Import Image Processing Library

me = tello.Tello()  #caling tello function from tello library

me.connect()           #connect tello
print("Drone Connected Succesfully")
print(me.get_battery())   #print battery

me.streamon() #Acess camera

while True:
    img = me.get_frame_read().frame  #start video capturing
    #img = cv2.resize(img, (10 , 10)) #resize
    cv2.imshow("Image", img) #showing image to us

    cv2.waitKey(200) #time to capture image

me.land() #land drone
print("Action Suceesfully Completed")