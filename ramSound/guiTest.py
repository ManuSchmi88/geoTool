import tkinter as tk
import ramSounder as Rs
def PressBut():
    rms1 = Rs.RMS()
    rms1.userInputBase()
    rms1.userInputCounts()
    rms1.depthCountPlot()

def submit():
    if entr1.get() == "Hello":
        print("Hello to you to!")

#This creates a first "canvas" of tkinter which we can use to build up around
#and also gives it a label with some text.
root1 = tk.Tk()
label1 = tk.Label(root1,
        text = "Hey Dirt-Diggers!",
        fg = "red",
        font = "Times")
label1.pack()
#This creates a button object which calles a function
Butt1 = tk.Button(root1, text = "Plot Rms", command = PressBut)
Butt1.pack()
#Play around with entry fields
entr1 = tk.Entry(root1)
entr1.pack()
Butt2 = tk.Button(root1,text = "submit", command = submit)
Butt2.pack()
#This is somehow needed.
root1.mainloop()
