import opc
from time import sleep

client = opc.Client('localhost:7890')

led_list = [(0,0,0)]*360
print(led_list)

print(enumerate(led_list))
