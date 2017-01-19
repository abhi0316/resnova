#!/usr/bin/python2
#import gpiozero
from Tkinter import *
import time
import os
import datetime
time1 = ''
BACKUP_FILE = "values.backup"
PASSWORD = "7528"
input_pin = 14
bounce_time = 2.000
root = Tk()
root.resizable(width=FALSE, height=FALSE)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry('{}x{}'.format(screen_width, screen_height))
root.title("PCB COUNT")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

bg_color = "#000000"
fg_color = "#000000"
tot_row = 0
tot_text = "TARGET:"
tot_hl = "white"#"#FF5555"
cnt_row = 1
cnt_text = "ACHIEVED:"
cnt_hl = "yellow"#"#55FF55"
rem_row = 2
rem_text = "REMAINING:"
rem_hl = "red"#"#8888FF"
tim_row = 3
tim_text = "TIMER:"
tim_hl = "yellow"
ent_row = 4
psd_row = 4
npcb_text = "{} UNITS PER PCB"
npcb_hl = "red"
npcb_row = 4

nr = 4 #number of rows
eh = 8 #entry height

nfd = 10.67 +5
lfd = 20 +5
efd = 90 
pfd = 90

num_font = ("Helvetica", int(screen_width/nfd), "bold")
label_font = ("Helvetica", int(screen_width/lfd), "bold")
entry_font = ("Helvetica", int(int(screen_width)/efd), "bold")
passwd_font = ("Helvetica", int(int(screen_width)/pfd), "bold")

num_width = 7
label_width = 11

num_anchor = E
label_anchor = W
entry_anchor = E
passwd_anchor = W
npcb_anchor = W

num_padx = 50

""" Frame that holds all"""
mainFrame = Frame(root, background=bg_color, width=screen_width, height=screen_height)
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
mainFrame.rowconfigure(0, minsize=screen_height/nr-eh)
mainFrame.rowconfigure(1, minsize=screen_height/nr-eh)
mainFrame.rowconfigure(2, minsize=screen_height/nr-eh)
mainFrame.rowconfigure(3, minsize=screen_height/nr-eh)
mainFrame.rowconfigure(4)
mainFrame.columnconfigure(0, minsize=screen_width/2)
mainFrame.columnconfigure(1, minsize=screen_width/2)

totalLabel = Label(mainFrame, bg=bg_color, fg=tot_hl, width=11, anchor=label_anchor, text=tot_text, font=label_font)
totalLabel.grid(column=0, row=tot_row, sticky=label_anchor)

countLabel = Label(mainFrame, bg=bg_color, fg=cnt_hl, width=11, anchor=label_anchor, text=cnt_text, font=label_font)
countLabel.grid(column=0, row=cnt_row, sticky=label_anchor)

remainLabel = Label(mainFrame, bg=bg_color, fg=rem_hl, width=11, anchor=label_anchor, text=rem_text, font=label_font)
remainLabel.grid(column=0, row=rem_row, sticky=label_anchor)

timeLabel = Label(mainFrame, bg=bg_color, fg=tim_hl, width=11, anchor=label_anchor, text=tim_text, font=label_font)
timeLabel.grid(column=0, row=tim_row, sticky=label_anchor)

# Total PCB number display
global total
total = 0
global totalNum
totalNum = StringVar()
totalNumLabel = Label(mainFrame, bg=bg_color, fg=tot_hl, font=num_font, textvariable=totalNum, width=num_width, padx=num_padx, anchor=num_anchor)
totalNumLabel.grid(column=1, row=tot_row, sticky=num_anchor)

global count
count = 0
global countNum
countNum = StringVar()
countNumLabel = Label(mainFrame, bg=bg_color, fg=cnt_hl, font=num_font, textvariable=countNum, width=num_width, padx=num_padx, anchor=num_anchor)
countNumLabel.grid(column=1, row=cnt_row, sticky=num_anchor)

global remain
remain = 0
global remainNum
remainNum = StringVar()
remainNumLabel = Label(mainFrame, bg=bg_color, fg=rem_hl, font=num_font, textvariable=remainNum, width=num_width, padx=num_padx, anchor=num_anchor)
remainNumLabel.grid(column=1, row=rem_row, sticky=num_anchor)

global timer_val
timer_val = 0
global timer_state
timer_state = False
global timeVar
timeVar = StringVar()
timeVarLabel = Label(mainFrame, bg=bg_color, fg=tim_hl, font=num_font, textvariable=timeVar, width=num_width, padx=num_padx, anchor=num_anchor)
timeVarLabel.grid(column=1, row=tim_row, sticky=num_anchor)



def update_var():
    totalNum.set("00")
    remainNum.set("00")
    countNum.set("00")
    

def time_check():
    time.sleep(5)
    
def time_update():
        global i
        global ti
        global time1
        global time4    
        time.sleep(1)
        time2 = time.strftime('%H:%M:%S')
        ti=ti+1
        if ti%12 ==0:
            i=i+1
            totalNum.set(i)
            totalNumLabel.update()

        time3 = time.strftime('%H')
        time4 = time.strftime('%M')
        if time3 =='23' and time4 == '09':
            time_check()


        if time2 != time1:
            time1 = time2
            timeVar.set(time1)
           
        totalNumLabel.after(200,time_update)  	


ti =0
i=0
    
    
update_var()            
    
time_update()

root.mainloop()
