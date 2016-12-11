from tkinter import *
from ramSounder import *
#This creates a window-instance in the object "win"
win = Tk()
win.title("Rammsounder")
fr1 = Frame(win, height=50, width=50)
fr1.pack()
#creates a button in the parent windows "win" and some text
b1 = Button(win,text = "New rms")
b1.pack() #"packs" the button on its parent window
def newRmsBut() :
    rms1 = RMS()
    rms1.userInputBase()
    rms1.userInputCounts()
b1.configure(command = newRmsBut)
b1.mainloop()
