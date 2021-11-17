from tkinter import *
tk = Tk()

# canvas
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

#                       x   y   width  height
canvas.create_rectangle(10, 10, 50   , 50   )

# few more rects
canvas.create_rectangle(10, 60, 300, 120)
canvas.create_rectangle(10, 150, 50, 200)

tk.mainloop()
