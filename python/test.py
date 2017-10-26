from tkinter import *
import math as mathtools

root=Tk()
frame1 = Frame(root, bd=10,padx=15,pady=15,bg="blue")
frame1.grid(row=0,column=0,rowspan=9,columnspan=2)

def callback(field_name, string_var):
    string_val = string_var.get();
    value = int(string_val);

    if field_name == 'Add 2:' and value :
        print('post', field_name, value + 2)

def validateNumeric(new_value):
    print(new_value)
    if new_value == "":
        return True
    try:
        int(new_value)
        return True
    except ValueError:
        return False


def createWidgets(root, varlist=[]):
    root.title('infogrid with math calculations')
    root.grid()
    font=("Calibri", 12)
    # label,place,inputplace
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
        ("Test",(1,4),(1,5)),
        ("Test",(2,4),(2,5)),
        (" ",(3,4),(None)),
        ("Test",(4,4),(4,5)),
        ("Test",(5,4),(5,5)),
        ("Test",(6,4),(6,5)),
        (" ",(7,4),(None)),
        ("Test",(8,4),(8,5)),
        ("Test",(9,4),(9,5)),
        )

#    columns=[]
#    for x in range(20):
#        y = info[x[1[1]]]
#        columns.append()

    list_of_widgets = []



    for text,lpos,ipos in info:

        if text:
            var=StringVar(0)
            varlist.append(var)
            var.set('')
            var.trace("w", lambda tclname, tclindex, mode, var=var, name=text: callback(name, var))

        Label(root, text=text, font=font).grid(row=lpos[0], column=lpos[1])

        if ipos:
            vcmd = (root.register(validateNumeric), '%P')
            Entry(root, textvariable=var, font=font, validate="key", vcmd=vcmd).grid(row=ipos[0], column=ipos[1])
            list_of_widgets.append(ipos)

    print(list_of_widgets)


#    Label(root, text=" ").grid(row=0, column=3, rowspan=9, padx=25)

vl=[]
createWidgets(root,vl)
root.mainloop()
