# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:31:33 2022

@author: ElectronicsBoy
"""

from tkinter import * # Import everything from the module tkinter

window = Tk(screenName="Hello, World!")
window.geometry("640x480");

resultLabel = Label(window, text="test")

def add():
    result = 4 + 1
    resultLabel["text"] = result
addButton   = Button(master=window, text="Add", command=add)

resultLabel.pack()
addButton.pack()

window.mainloop()