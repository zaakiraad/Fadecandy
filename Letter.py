import opc                              # import opc code
import time



client = opc.Client('localhost:7890')

led_colour = [(0,0,0)]*360

led_colour[20] = (255,255,0)
led_colour[21] = (255,255,0)
led_colour[22] = (255,255,0)
led_colour[23] = (255,255,0)
led_colour[24] = (255,255,0)
led_colour[25] = (255,255,0)
led_colour[26] = (255,255,0)
led_colour[27] = (255,255,0)
led_colour[28] = (255,255,0)
led_colour[29] = (255,255,0)
led_colour[88] = (255,255,0)
led_colour[146] = (255,255,0)
led_colour[204] = (255,255,0)
led_colour[262] = (255,255,0)
led_colour[320] = (255,255,0)
led_colour[321] = (255,255,0)
led_colour[322] = (255,255,0)
led_colour[323] = (255,255,0)
led_colour[324] = (255,255,0)
led_colour[325] = (255,255,0)
led_colour[326] = (255,255,0)
led_colour[327] = (255,255,0)
led_colour[328] = (255,255,0)
led_colour[329] = (255,255,0)



client.put_pixels(led_colour) 
