from __future__ import division

import opc
from time import sleep

score = 0
questions = 10

client = opc.Client('localhost:7890')

led_list = [(0,0,0)]*360
print(led_list)
print(enumerate(led_list))

print('Welcome to the Python Quiz')
answer=input('Ready to play? (yes/no) :')

value = input('''Press 1 to Start:'
              \t 1. Start
              Type number then Enter.''')

def func1(val):
        return val**val

while True:
    if (value.isdigit() == True):
        value = int(value)
        break
    else:
        value = input("invalid input, try again:")

if value == 1:
    print(func1(value))
    if answer.lower()=='yes':
        answer=input('Question 1: ')
        if answer.lower()=='a':
            score += 1
            print('Correct')
            led_colour = [(0,255,0)]*1
        else:
            print('Wrong: Answer is ')

client.put_pixels(led_colour)
            

answer=input('Question 2: ')
if answer.lower()=='a':
    score += 1
    print('Correct')
    led_colour = [(0,255,0)]*2
else:
    print('Wrong: Answer is ')

client.put_pixels(led_colour)


mark = (score/questions)*100
print('''
      Score:''', mark)

client.put_pixels(led_colour)
 
