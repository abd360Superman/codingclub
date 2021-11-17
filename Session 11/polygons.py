from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

# polygon             x1  y1   x2   y2  x3   y3   fill      outline    
canvas.create_polygon(10, 10,  100, 10, 100, 110, fill="", outline="black")
canvas.create_polygon(200, 10, 240, 30, 120, 100, 140, 120, fill="", outline="black")

tk.mainloop()
