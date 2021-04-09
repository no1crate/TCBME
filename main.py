from pyautogui import *
from time import sleep as pause
from random import choice
messages = ["Hola", "Como estas?", "Como te llamas?", "Cual es tu twitter?", "Tenes youtube", "A que horas haces streams?", "Cuando haces streams?", "Todo bien?"]
time = input("Cada cuanto quieres que se envie?")
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