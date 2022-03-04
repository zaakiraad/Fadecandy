import opc                              # import opc code
from time import sleep

client = opc.Client('localhost:7890')

led_list = [(0,0,0)]*360                # list of 360 tuples, with R,G,B values
fade_amount = 50                        # size of every fade step
print(led_list)
print(enumerate(led_list))


while True:
    for led in enumerate(led_list):     # enumerate creates a list of tuples that contain index and contents of each element
        
                                   
        r,g,b = led[1]                  # points to the second element in led in the (R,G,B) tuple
        
        r = r+fade_amount
        g = g+fade_amount
        b = b+fade_amount

        new_colour = (r,g,b)            
        led_list[led[0]] = new_colour
        

        if r >=255 or r <= 0:
            fade_amount = -fade_amount  # if it has - change directions from the next iteration.
            

    client.put_pixels(led_list)     # update leds
    sleep(.01)                      # sleep for 1ms
    







