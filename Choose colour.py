from __future__ import division

import opc
from time import sleep

from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

client = opc.Client('localhost:7890')

led_list = [(0,0,0)]*360
print(led_list)
print(enumerate(led_list))



           
ttk.Label(frm, text='''Choose colour:'
              /t 1. Red
              /t 2. Blue
              /t 3. Yellow
              /t 4. Green
              /t 5. White''').grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

value = input('''Choose colour:''')

def func1(val):
    return val**val

while True:
    if (value.isdigit() == True):
        value = int(value)
        break
    else:
        value = input("invalid:")

if value == 1:
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

client.put_pixels(led_colour)

root.mainloop()
