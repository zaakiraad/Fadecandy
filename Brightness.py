import opc
from time import sleep
import colorsys

from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()


ttk.Button(frm, text="Start", command=root.destroy).grid(column=1, row=0)



client = opc.Client('localhost:7890')

led_list = [(0,0,0)]*360
fade_amount = 50

s = 1.0
v = 10.0



for hue in range(10000):
    rgb_fractional = colorsys.hsv_to_rgb(hue/360.0, s, v)
    r_float = rgb_fractional[0]
    g_float = rgb_fractional[1]
    b_float = rgb_fractional[2]


    for led in enumerate(led_list):
        r = led[1]
        
        fade_amount = -fade_amount


    rgb = (r_float*255, g_float*255, b_float*255)
    client.put_pixels([rgb]*360)
    sleep(0.01)
    client.put_pixels(led_list)
    root.mainloop()

