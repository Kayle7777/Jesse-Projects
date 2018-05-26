from os import *

#path = r'C:\\users\\jesse\\desktop\\PREWORK_JDW\\'

for x in range(11):
    folder = r"C:\users\jesse\desktop\PREWORK_JDW\Module-%s" % (x+1)
    makedirs(folder)
