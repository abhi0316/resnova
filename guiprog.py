from Tkinter import *
import time

root = Tk()
root.wm_title("resnova")
root.geometry('{}x{}'.format(900, 800))
root.configure(background="#4682B4")

mainframe1 = Frame(root)
mainframe1.grid(column=2000, row=2000, sticky=(N, W, E, S))
mainframe1.place(x=50,y=130)
best1 = StringVar()
best = StringVar()
best.set('start')
best1.set('start')

x1 = 30
Label(mainframe1,height=2,width=10,textvariable=best1,bg='white',fg='black',font=("Times New Roman",x1)).grid(column=1,row=1)

mainframe2 = Frame(root)
mainframe2.grid(column=2000, row=2000, sticky=(N, W, E, S))
mainframe2.place(x=610,y=130)
best = StringVar()
best.set('start')
x1 = 30
Label(mainframe2,height=2,width=10,textvariable=best,bg='white',fg='black',font=("Times New Roman",x1)).grid(column=1,row=1)

mainframe3 = Frame(root)
mainframe3.grid(column=2000, row=2000, sticky=(N, W, E, S))
mainframe3.place(x=50,y=500)
best = StringVar()
best.set('start')
x1 = 30
Label(mainframe3,height=2,width=10,textvariable=best,bg='white',fg='black',font=("Times New Roman",x1)).grid(column=1,row=1)


mainframe = Frame(root)
mainframe.grid(column=2000, row=2000, sticky=(N, W, E, S))
mainframe.place(x=610,y=500)
best = StringVar()
best.set('start')
x1 = 30
Label(mainframe,height=2,width=10,textvariable=best,bg='white',fg='black',font=("Times New Roman",x1)).grid(column=1,row=1)


root.minsize(width=900, height=700)
root.maxsize(width=900, height=700)


w1 = Label(root, text="PCB ANALYSER")
w1.config(font=("Times New Roman",30),foreground="black",background="#4682B4")
w1.pack()

w2 = Label(root, text="Expected")
w2.config(height=1,width=14,font=("Times New Roman",20),background="#4682B4",foreground="white")
w2.place(x=53,y=95)
w3 = Label(root, text="Completed")
w3.config(height=1,width=14,font=("Times New Roman",20),background="#4682B4",foreground="white")
w3.place(x=53,y=465)
w4 = Label(root, text="Ratio")
w4.config(height=1,width=14,font=("Times New Roman",20),background="#4682B4",foreground="white")
w4.place(x=613,y=95)
w4 = Label(root, text="Time")
w4.config(height=1,width=14,font=("Times New Roman",20),background="#4682B4",foreground="white")
w4.place(x=613,y=465)
x=0    
i=0
while True:
        x=x+1
        time.sleep(1.0)
        mainframe1.update()
        Label(mainframe1,height=2,width=10,textvariable=best1,bg='white',fg='black',font=("Times New Roman",30)).grid(column=1,row=1)

        if x%12 ==0:
            i=i+1
            best1.set(i)
            Label(mainframe1,height=2,width=10,textvariable=best1,bg='red',fg='black',font=("Times New Roman",30)).grid(column=1,row=1)

            







            





root.mainloop()

