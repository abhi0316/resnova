

import time
from Tkinter import *
     
root = Tk()
root.geometry('{}x{}'.format(900, 800))
     
mainframe = Frame(root)
mainframe.grid(column=2000, row=2000, sticky=(N, W, E, S))
mainframe.place(x=68,y=34)
best = StringVar()
best.set('start')
x1 = 12
Label(mainframe,height=10,width=10,textvariable=best,bg='#321000',fg='#000fff000',font=("Helvetica",x1)).grid(column=1,row=1)
x=0    
while True:
        x=x+1
        time.sleep(1.0)
        best.set('test # %d' % (x))
        mainframe.update()
root.mainloop() 

