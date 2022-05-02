# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:17:57 2022

@author: ElectronicsBoy
"""

from tkinter import *

window = Tk(screenName="C146: The Fibonacci flower:   ")
window.geometry("400x400")

labelSeries = Label(master=window, text="Fibonacci Series:")
labelFlower = Label(master=window)
labelSpiral = Label(master=window)

def genFibonacii():
    num = 10
    last = 0
    now = 1
    sum = 0
    counter = 1
    
    while counter <= num:
        labelSeries["text"] = str(sum) + " "
        counter += 1
        last = now
        now = sum
        sum = last + now
    labelFlower["text"] = "Flower is fully bloomed"
    labelSpiral["text"] = "Spirals in right direction are, " + str(last) + ", and spirals in left direction are, " + str(now) + ".\nTotal spirals are " + str(sum)
        
buttonShowSeries = Button(master=window, text="Show Fibonacci Series", command=genFibonacii)
buttonShowSeries.pack()
labelSeries.pack()
labelFlower.pack()
labelSpiral.pack()

window.mainloop()