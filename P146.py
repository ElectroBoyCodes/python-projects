# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:46:40 2022

@author: ElectronicsBoy
"""

from tkinter import *

window = Tk(screenName="C146: The Fibonacci flower:   ")
window.geometry("400x400")

labelSeries = Label(master=window, text="Fibonacci Series:")
labelFlower = Label(master=window)
labelSpiral = Label(master=window)

def genFibonacii():
    num = int(entryNumberToGenInput.get())
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

entryNumberToGenInput = Entry(master=window, text="10")
buttonShowSeries = Button(master=window, text="Show Fibonacci Series", command=genFibonacii)

entryNumberToGenInput.pack()
buttonShowSeries.pack()
labelSeries.pack()
labelFlower.pack()
labelSpiral.pack()

window.mainloop()