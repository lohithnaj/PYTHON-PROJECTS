from tkinter import Tk #module to create a window
from tkinter import Label #module to write into the tkinter window
import time

root = Tk() # root variable is where the tkinter window is there
root.title("Clock")# title of the root

def present_time():
    display_time = time.strftime("%I:%M:%S %p")#strrftime to display current time,%p for am or pm
    digi_clock.config(text=display_time)#config  to what text we want to write or display into digi_clock
    digi_clock.after(1000,present_time)
digi_clock = Label(root, font=("arial", 125),bg="blue",fg="white" ) #To write into tkinter window,bg=background color,fg=font color
digi_clock.pack()
present_time()
root.mainloop() #used to display the output and should be written in all programs to close