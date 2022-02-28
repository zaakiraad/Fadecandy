from __future__ import division

import opc
from time import sleep

score = 0

client = opc.Client('localhost:7890')

led_list = [(0,0,0)]*360
print(led_list)

print(enumerate(led_list))

print('Welcome to the Python Quiz')

value = input('''Press S to Start:'
              \t S. Start
              Type letter then Enter.''')

def funcS(val):
    return val**val

while True:
    if value.isdigit == True:
        value = int(value)
        break
    else:
        value = input("invalid input, try again:")

if value == S:
    if answer.lower()=='yes':
        answer=input('Question 1: What is your Favourite programming language?')
    if answer.lower()=='python':
        score += 1
        print('correct')


 
