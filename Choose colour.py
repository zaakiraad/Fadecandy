from __future__ import division

import opc                                            # import opc code
from time import sleep

from tkinter import *                                 # import tkinter
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

client = opc.Client('localhost:7890')

led_list = [(0,0,0)]*360
print(led_list)
print(enumerate(led_list))                            # enumerate creates a list of tuples that contain index and contents of each element

print('''Choose colour:'
              1. Red
              2. Blue
              3. Yellow
              4. Green
              5. White''')
           
ttk.Label(frm, text='''Choose colour:'
              1. Red
              2. Blue
              3. Yellow
              4. Green
              5. White''').grid(column=0, row=0)     # show GUI in new tab on tkinter
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0) # create button that stops code

value = input('''Choose colour:''')

def func1(val):
    return val**val

while True:
    if (value.isdigit() == True):               # isdigit returns true if all characters are digits or it is false
        value = int(value)
        break
    else:
        value = input("invalid:")

if value == 1:                                  # typed number starts code in if value
    print('red')
    led_colour = [(255,0,0)]*360

if value == 2:
    print('blue')
    led_colour = [(0,0,255)]*360

if value == 3:
    print('yellow')
    led_colour = [(255,255,0)]*360

if value == 4:
    print('green')
    led_colour = [(0,255,0)]*360

if value == 5:
    print('white')
    led_colour = [(255,255,255)]*360

client.put_pixels(led_colour)                 # update led colour

root.mainloop()
