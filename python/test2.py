from tkinter import *

gridloc = []

for x in range(0,5):
    for y in range(0,5):
        gridloc.append((x,y))

root = Tk()
root.grid()

for b in gridloc:
    Button(root, text="O",).grid(row=b[0],column=b[1])

blista = []
for a in enumerate(gridloc):
    blista.append(a)
buttonList = [i[0] for i in blista]
print(buttonList)

#def callback:
#    for x in ButtonList

root.mainloop()
