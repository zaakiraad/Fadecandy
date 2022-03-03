from __future__ import division

import opc
from time import sleep

score = 0
questions = 5

client = opc.Client('localhost:7890')

led_list = [(0,0,0)]*360
print(led_list)
print(enumerate(led_list))

print('Welcome to the Fadecandy Quiz')
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
    if answer.lower()=='yes':
        answer=input('Question 1: How many LEDs are there?  ')
        if answer.lower()=='360':
            score += 1
            print('Correct')
            led_colour = [(0,255,0)]*1
        else:
            print('Wrong: Answer is 360')
client.put_pixels(led_colour)

            

answer=input('Question 2: What coding program is this?  ')
if answer.lower()=='python':
    score += 1
    print('Correct')
    led_colour = [(0,255,0)]*2
else:
    print('Wrong: Answer is python ')

client.put_pixels(led_colour)


answer=input('Question 3: What repository is used?  ')
if answer.lower()=='github':
    score += 1
    print('Correct')
    led_colour = [(0,255,0)]*3
else:
    print('Wrong: Answer is github ')

client.put_pixels(led_colour)


answer=input('Question 4: What question number is this?  ')
if answer.lower()=='4':
    score += 1
    print('Correct')
    led_colour = [(0,255,0)]*4
else:
    print('Wrong: Answer is 4 ')

client.put_pixels(led_colour)


answer=input('Question 5: What has a face and two hands but no arms or legs?  ')
if answer.lower()=='clock':
    score += 1
    print('Correct')
    led_colour = [(0,255,0)]*5
else:
    print('Wrong: Answer is clock ')

client.put_pixels(led_colour)


mark = (score/questions)*100
print('''
                                 Score %:''', mark)
print('                          Thank you for playing!')


client.put_pixels(led_colour)
 
