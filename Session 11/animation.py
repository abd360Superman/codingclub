import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

# create a polygon
canvas.create_polygon(10, 10, 10, 60, 50, 35)

while True:
    for x in range(0, 60):
        # move the canvas, to make it look like that the shape is moving
        canvas.move(1, 5, 5)
        # update display on tk window
        tk.update()
        time.sleep(0.05)

    for x in range(0, 60):
        canvas.move(1, -5, -5)
        tk.update()
        time.sleep(0.05)

tk.mainloop()
