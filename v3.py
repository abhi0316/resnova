#!/usr/bin/python2
#import RPi.GPIO as GPIO
from Tkinter import *
import time

PASSWORD = "3333"
input_pin = 14
bounce_time = 0.500
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
rem_text = "REMAIN:"
rem_hl = "red"#"#8888FF"
tim_row = 3
tim_text = "TIMER:"
tim_hl = "yellow"
ent_row = 4
psd_row = 4

nr = 4 #number of rows
eh = 7 #entry height

nfd = 10.67 +5
lfd = 20 +5
efd = 90 
pfd = 90

num_font = ("Helvetica", int(screen_width/nfd), "bold")
label_font = ("Helvetica", int(screen_width/lfd), "bold")
entry_font = ("Helvetica", int(int(screen_width)/efd), "bold")
passwd_font = ("Helvetica", int(int(screen_width)/pfd), "bold")

num_width = 6
label_width = 11

num_anchor = E
label_anchor = W
entry_anchor = E
passwd_anchor = W

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

def chk_entry_char(char, full):
    print(char)
    if( (char.isdigit() or not full) and len(full)<7):
        print("Valid!")
        return True
    print("Not Valid!")
    return False

passwdVal = StringVar()
passwdEntry = Entry(mainFrame, state=DISABLED, fg=bg_color, disabledbackground=bg_color, highlightthickness=0, font=entry_font, show='*',  bd=0, relief="solid", textvariable=passwdVal, validate="key")
passwdEntry['validatecommand'] = (passwdEntry.register(chk_entry_char), '%S', '%P')
passwdEntry.grid(column=0, row=psd_row, sticky=passwd_anchor)

totalVal  = StringVar()
totalEntry = Entry(mainFrame, state=DISABLED, fg=bg_color, disabledbackground=bg_color, highlightthickness=0, font=entry_font,  bd=0, relief="solid", textvariable=totalVal, validate="key")
totalEntry['validatecommand'] = (totalEntry.register(chk_entry_char), '%S', '%P')
totalEntry.grid(column=1, row=ent_row, sticky=entry_anchor)

def toStr(num):
    if( num>=0 and num<=999999 ):
        thou = num//1000
        ones = num%1000
        if( thou ):
            return str(thou)+","+str(num)[-3:]
        else:
            return str(ones)

def update_vars():
    global total
    global count
    global remain
    if( total-count>=0 ):
        remain = total-count
    else:
        remain = 0    
    totalNum.set(toStr(total))
    countNum.set(toStr(count))
    remainNum.set(toStr(remain))
    global timer_val
    print("Timer Var:", timer_val, time.time())
    seconds = timer_val%60
    total_minutes = int(timer_val/60)
    hours = int(total_minutes/60)
    minutes = total_minutes%60
    timer_str = "{}:{:0=2}:{:0=2}".format(hours, minutes, seconds)
    timeVar.set(timer_str)

def quit_program(*args):
    #GPIO.cleanup()
    root.destroy()

def focus_passwd(*args):
    passwdEntry.config(state=NORMAL) #bg=tot_hl, fg=bg_color)
    passwdEntry.focus_set()
    passwdVal.set("")
    
def focus_entry(*args):
    totalEntry.config(state=NORMAL)#, bg=tot_hl, fg=bg_color)
    totalEntry.focus_set()
    totalVal.set("")

def cancel_entries(*args):
    totalVal.set("")
    passwdVal.set("")
    totalEntry.config(state=DISABLED)#, bg=bg_color, fg=tot_hl)
    passwdEntry.config(state=DISABLED)
    mainFrame.focus_set()

def set_total(var):
    print var
    global total
    global count
    global remain
    if( var == "count" ):
        if( len(totalVal.get())<7 and totalVal.get().isdigit() ):
            count = int(totalVal.get())
                
    elif( var == "total" ):
        if( len(totalVal.get())<7 and totalVal.get().isdigit() ):
            total = int(totalVal.get())
            #count=0
            #remain = total
            
    update_vars()
    cancel_entries()

def update_timer():
    global root
    global timer_val
    global timer_state
    update_vars()
    if timer_state:
        timer_val += 1
        root.after(1000, update_timer)
    
def reset_timer():
    global timer_val
    timer_val = 0
    update_vars()

def toggle_timer_state():
    global timer_state
    if timer_state:
        timer_state = False
        update_vars()
    else:
        timer_state = True
        update_timer()

def context_check(event):
    if totalEntry['state'] == DISABLED and passwdEntry['state'] == NORMAL and passwdVal.get() == PASSWORD:
        if event.char == '\r':
            cancel_entries()
            focus_entry()
        elif event.char == '/':
            cancel_entries()
            reset_timer()
        elif event.char == '*':
            cancel_entries()
            toggle_timer_state()
    elif totalEntry['state'] == NORMAL and passwdEntry['state'] == DISABLED:
        if event.char == '\r':
            set_total("total")
        else:
            set_total("count")
    elif totalEntry['state'] == DISABLED and passwdEntry['state'] == DISABLED and event.char == '.':
        focus_passwd()
    else:
        cancel_entries()

update_vars()
root.bind('<Control-q>', quit_program)
root.bind('<KP_Decimal>', context_check)
root.bind('<KP_Enter>', context_check)#lambda event: set_total("total"))
root.bind('<KP_Subtract>', cancel_entries)
root.bind('<KP_Add>', context_check)#lambda event: set_total("count"))
root.bind('<KP_Multiply>', context_check)
root.bind('<KP_Divide>', context_check)

def clear_hl(*args):
    countNumLabel.config(bg=bg_color)

def count_up():
    global remain
    global count
    print("Rising Edge Detected!")
    if( remain ):
        remain -= 1
    else:
        countNumLabel.config(bg=cnt_hl)
        root.after(100, clear_hl)
    count += 1
    update_vars()

#GPIO code      
"""
GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

last_rise = time.time()

def record_rise(channel):
    GPIO.remove_event_detect(channel)
    GPIO.add_event_detect(input_pin, GPIO.FALLING, check_tdiff)
    global last_rise
    last_rise = time.time()

def check_tdiff(channel):
    GPIO.remove_event_detect(channel)
    GPIO.add_event_detect(input_pin, GPIO.RISING, record_rise)
    global last_rise
    if time.time()-last_rise > bounce_time:
        count_up()

GPIO.add_event_detect(input_pin, GPIO.FALLING, check_tdiff)
"""
"""#Refresh code
refresh1 = "blue"
refresh2 = "black"
refreshLabel = Label(mainFrame, bg=refresh1, text="  ")
refreshLabel.grid(column=0, row=ent_row, sticky=W)
def refresh_hdmi(*args):
    refreshLabel.config(bg=args[0])
    if(args[0]==refresh1):
        root.after(1000, refresh_hdmi, refresh2)
    elif(args[0]==refresh2):
        root.after(1000, refresh_hdmi, refresh1)

root.after(1000, refresh_hdmi, refresh1)"""


#main loop
root.mainloop()
