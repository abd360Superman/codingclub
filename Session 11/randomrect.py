from tkinter import *
import random

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

# a random rectangle function
def random_rectangle(width, height):
    x1 = random.randrange(width) # Gets a random number between 0 and number provided (number provided cannot come in random result)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2)

for x in range(0, 100):
    # Calling function
    random_rectangle(400, 400)


tk.mainloop()
