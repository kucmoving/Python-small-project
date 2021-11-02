from tkinter import *
import tkinter as tk
#---------------Setting-----------------------------
BLACK = "#000000"
timeformat = "00:00"
job = None
#---------------Setup window------------------------
window = Tk()
window.title("Time Counter")
window.minsize(width=350, height=100)
window.config(padx=0, pady=0, bg=BLACK)
#---------------fucntion---------------------------
def reset():
    time_label.config(text="00:00")
    system_label.config(text="Reset! Please input again.",bg="black")
    start_but.config(state="normal")
    global job
    window.after_cancel(job)    ####remeber to use after_cancel function, and global variable

def get_input():
    time = time_entry.get()
    realtime = (int(time[0:2])) * 60 + (int(time[3:5]))    ####to slice the string input
    countdown(realtime)

def countdown(time_sec):
    system_label.config(text="System: Counting...", bg="black", fg="Green")
    if time_sec > 0:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        time_label.config(text=f'{timeformat}')
        global job                                           #######import global variable, in order to stop it when u need
        job = window.after(1000, countdown, time_sec - 1)
        start_but.config(state="disable")

    else:
        time_label.config(text=f'00:00')
        system_label.config(text="System: Time's up!", bg="yellow", fg="Green")
        start_but.config(state="normal")
########################UI################################################################
title_label = Label(text="Let's count down!",bg="black", fg="white", font=("Arial",20,"bold")).place(x=60,y=20)
time_entry = Entry(highlightthickness=0,width=20)
time_entry.insert(0,"01:00")
time_entry.focus()
time_entry.place(x=60,y=70)

time_label = Label(text=f"{timeformat}", bg="black", fg="yellow", font=("Helevetica",30,"bold"))
time_label.place(x=60,y=90)

start_but = Button(text="Start", highlightthickness=0, command=get_input)
start_but.place(x=220, y=70)
reset_but = Button(text="Reset", highlightthickness=0, command=reset)
reset_but.place(x=220, y=100)

system_label = Label(text="System: Waiting for your input^^", bg="black", fg="yellow")
system_label.place(x=60,y=150)

window.mainloop()
####'NoneType' object has no attribute 'config' , you have to split the place/ grid / pack
