import tkinter as tk
import ramSounder as Rs
def PressBut():
   rms1 = Rs.RMS()
   rms1.userInputBase()
   rms1.userInputCounts()
   rms1.depthCountPlot()

root1 = tk.Tk()
Butt1 = tk.Button(root1, text = "Plot Rms", command = PressBut)
Butt1.pack()
root1.mainloop()
