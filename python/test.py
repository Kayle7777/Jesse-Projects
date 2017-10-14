from tkinter import *
import math as mathtools


def createWidgets(root, varlist=[]):
    root.title('infogrid with math calculations')
    root.grid()
    font=("Calibri", 12)
    # label,place,inputplace,math
    info=(
        (" ",(0,0),None),
        ("Multiply by 2:",(1,1),(1,2)),
        ("Divide by 2:", (2,1),(2,2)),
        ("",(3,1),None),
        ("Add 2:",(4,1),(4,2)),
        ("Subtract 2:",(5,1),(5,2)),
        ("Power of 2:",(6,1),(6,2)),
        ("",(7,1),None),
        ("Square Root:",(8,1),(8,2)),
        ("Multiply by 2 Again:",(9,1),(9,2)),
        (" ",(10,3),None),
        )


    list_of_widgets = []
    for text,lpos,ipos in info:
        if text:
            var=IntVar()
            varlist.append(var)
            var.set('')

        Label(root,text=text,font=font).grid(row=lpos[0],column=lpos[1])

        if ipos:
            Entry(root,textvariable=var,font=font).grid(row=ipos[0],column=ipos[1])
            list_of_widgets.append(ipos)

    print(list_of_widgets)

    def numberget(idx):
        print(list_of_widgets[idx]).get()

    numberget(1)


        #def callback():
            #print e.get()
        #b = Button(master, text="get", width=10, command=callback)


# access list of widgets below this line

#    for ipos in list_of_widgets:
#        if ipos:
#            Entry(root,status='disabled').pack(side=RIGHT)#,textvariable=eval(list_of_widgets[x,y].get() && mathlist))

root=Tk()
vl=[]
createWidgets(root,vl)
root.mainloop()
