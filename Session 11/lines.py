from tkinter import *
tk = Tk()

# making a canvas on which we can draw
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

# Drawing a line from (0, 0) to (500, 500)
canvas.create_line(0, 0, 500, 500)

tk.mainloop()
