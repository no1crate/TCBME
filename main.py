from pyautogui import *
from time import sleep as pause
from random import choice
messages = []
times = int(input("Number of messages:"))
for i in range(times):
    messages.append(input("What you want to say?"))
time = input("Delay? (0 for nothing)")
while True:
    if(time != ''):
        if('-' in time):
            time = 0
            break
        if("." in time):
            time = float(time)
            break
        elif(not "." in time):
            time = int(time)
            break
    if(time == ''):
        time = 0
        break
while True:
        if(time == 0):
            write(choice(messages))
            press("enter")
        if(time != 0):
            write(choice(messages))
            press("enter")
            pause(time)