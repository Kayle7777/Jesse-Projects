from os import *

#path = r'C:\\users\\jesse\\desktop\\PREWORK_AFH\\'

for x in range(11):
    folder = r"C:\users\jesse\desktop\PREWORK_AFH\Module-%s" % (x+1)
    makedirs(folder)
