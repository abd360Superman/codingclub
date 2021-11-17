from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

#                  cx   cy
canvas.create_text(180, 100, text='This is some piece of text', fill='red', font=('Helvetica', 20))

tk.mainloop()
