from tkinter import * # importing module
# if we would import turtle like
# from turtle import *
# instead of
# import turtle
# then we could write
# t = Pen()
# instead of
# t = turtle.Pen()

from tkinter import messagebox as mb # import message box as mb from tkinter
# instead of writing
# messagebox.func_name()
# we can write
# mb.func_name()

tk = Tk() # Creating a new tkinter window

def hello():
    #            Window title    Text to display
    mb.showinfo("Window title", "Text to display")

#            the graphical window  text on button    Function to call when button clicked
btn = Button(tk                  , text="click me",  command=hello                       )
btn.pack() # display button created

tk.mainloop() # executing the program until the window is removed
