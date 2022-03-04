import opc                                    # import opc code
from time import sleep
import colorsys

client = opc.Client('localhost:7890')

from tkinter import *                         # import tkinter
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()


ttk.Button(frm, text="Start", command=root.destroy).grid(column=1, row=0) # create button called start in column 1 row 0





led_list = [(0,0,0)]*360                       # list of 360 tuples, each containing R,G,B values.
fade_amount = 50                               # size of each fade step.

s = 1.0                                        # maximum colour
v = 10.0                                       # maximum brightness



for hue in range(10000):                       # maximum colour range
    rgb_fractional = colorsys.hsv_to_rgb(hue/360.0, s, v)
    r_float = rgb_fractional[0]
    g_float = rgb_fractional[1]
    b_float = rgb_fractional[2]


    for led in enumerate(led_list):
        r = led[1]
        
        fade_amount = -fade_amount              # if it has - change directions from the next iteration.


    rgb = (r_float*255, g_float*255, b_float*255)
    client.put_pixels([rgb]*360)
    sleep(0.01)                                 # 1ms delay
    client.put_pixels(led_list)                 # send list to lights
    root.mainloop()

