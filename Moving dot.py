import opc                              # import opc code
import time



client = opc.Client('localhost:7890')


    
led_colour = [(255,0,0)]*360            # led colour r,g,b values



print (enumerate(led_colour))
for item in enumerate(led_colour):       # enumerate creates a list of tuples with contents of each element and index
    time.sleep(0.01)
    print (item)
    if item[0]%1 == 0:
        led_colour = [(200,200,0)]*360
        r, g, b = item[1]                # this points to the second element in item in the (R,G,B) tuple
        r = r- 120                       # tells how much r to change from current led colour values
        g = g - 120                      # tells how much g to change from current led colour values
        b = b - 120                      # tells how much b to change from current led colour values


        new_colour =(r,g,b)
        led_colour[item[0]]= new_colour
    client.put_pixels(led_colour)
    client.put_pixels(led_colour)

client.put_pixels(led_colour)
client.put_pixels(led_colour)             # update leds
print (led_colour)
