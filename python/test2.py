from tkinter import *

gridloc = []

for x in range(0,25):
    for y in range(0,25):
        gridloc.append((x,y))

root = Tk()
root.grid()

for b in gridloc:
    Button(root, text="O").grid(row=b[0],column=b[1])

root.mainloop()
