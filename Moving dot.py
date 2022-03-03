import opc
import time



client = opc.Client('localhost:7890')


    
led_colour = [(255,0,0)]*360



print (enumerate(led_colour))
for item in enumerate(led_colour):
    time.sleep(0.01)
    print (item)
    if item[0]%1 == 0:
        led_colour = [(200,200,0)]*360
        r, g, b = item[1]
        r = r- 120
        


        new_colour =(r,g,b)
        led_colour[item[0]]= new_colour
    client.put_pixels(led_colour)
    client.put_pixels(led_colour)

client.put_pixels(led_colour)
client.put_pixels(led_colour)
print (led_colour)
