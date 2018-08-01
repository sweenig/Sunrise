# Sunrise Alarm Clock
In an earlier post, I shared my code for how I shed light inside my closet early in the morning. If my wife and I got up at the same time, I'd use this for an ambient light alarm clock. This type of clock is more gentle. However, since I get up well before my wife, I use it instead to gently light my closet while I'm doing the early morning ninja routine.

Two options exist: Sense HAT and Unicorn HAT. 

The only thing that really has to change between the two is the import and object declaration, which if you declare it with the name UH like the other script, means nothing else changes.

One nice thing about using the SenseHAT instead of the simpler UnicornHat is that the SenseHAT provides some environmental sensors which could be used for other home automation projects. For example, you could string a humidity sensor over into the bathroom and whenever the humidity of the sensor is higher than what is detected by the SenseHAT (plus some margin), you could trigger a relay to turn on the bathroom vent fan. Also, you could use the humidity and temperature sensors to trigger an IFTTT recipe to provide an extra input to your Nest controlled air conditioner. It's possible you could use the accelerometer to plot seismic activity in the area (not sure about this one but it should be theoretically possible).
