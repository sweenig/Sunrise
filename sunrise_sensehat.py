from sense_hat import SenseHat
import time
 
s = SenseHat()
#s.low_light = True
 
midnight = [25, 25, 112] #possible future color during night time
targetcolor = [253, 94, 83] #this is the color of the sunrise. I picked one. Modify as needed [R,G,B]
duration = 6400 #this is the total amount of time that the sun should take to rise, there are 64 LEDs and they each cycle through from 1 to 100, so 6400 gets you 1 second per LED. If you want a faster sunrise, lower this number
dayduration = 900 #this is the total amount of time that the sun should stay risen (900s = 15min)
def drawsun(brightness): #function to draw all 64 pixels at a specified percentage of the final color.
        red = targetcolor[0] * brightness / 100 #calculate the R value for the given progress between 0 and the target R value.
        green = targetcolor[1] * brightness / 100 #calculate the G value for the given progress between 0 and the target G value.
        blue = int(targetcolor[2] * brightness / 100) #calculate the B value for the given progress between 0 and the target B value.
        for y in range(8): #cycle through every row
                for x in range(8): #cycle through every column
                        s.set_pixel(x,y,red,green,blue) #set the pixel
                        time.sleep(duration/6400) #wait before moving on
try:
        print "Sun rising..."
        for a in range(1,101): #cycle through the brightness levels from 1 to 100
                drawsun(a)
                print "Brightness: ", str(a)
        print "Sun up."
        time.sleep(dayduration) #let the sun shine in!
        print "Sun setting..."
        for b in range(99,-1,-1): #cycle through the brightness levels back down to 0
                drawsun(b)
except:
        print("terminated manually")
