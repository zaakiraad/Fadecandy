import opc
from time import sleep

client = opc.Client('localhost:7890')

led_list = [(0,0,0)]*360
fade_amount = 50
print(led_list)
print(enumerate(led_list))


while True:
    for led in enumerate(led_list):
        
                                   
        r,g,b = led[1]
        
        r = r+fade_amount
        g = g+fade_amount
        b = b+fade_amount

        new_colour = (r,g,b)            
        led_list[led[0]] = new_colour
        

        if r >=255 or r <= 0:
            fade_amount = -fade_amount
            

    client.put_pixels(led_list)
    sleep(.01)
    







