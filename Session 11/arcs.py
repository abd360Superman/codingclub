from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

# create an arc   top-x  top-y bottom-x bottom-y  degrees turn   make it look like an arc
canvas.create_arc(10   , 10   , 200    , 80     , extent=45    , style=ARC              ) # 45 degrees arc
canvas.create_arc(10   , 80   , 200    , 160    , extent=90    , style=ARC              ) # 90 degrees arc
canvas.create_arc(10   , 160  , 200    , 240    , extent=135   , style=ARC              ) # 135 degrees arc
canvas.create_arc(10   , 240  , 200    , 320    , extent=180   , style=ARC              ) # semi circle
canvas.create_arc(10   , 320  , 200    , 400    , extent=359   , style=ARC              ) # circle

tk.mainloop()
