import tkinter as tk
import ramSounder as rs

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = "RMS Plot",command =
                self.new_rms)
        self.button1.pack()
        self.frame.pack()
    def new_rms(self):
        rms1 = rs.RMS()
        rms1.userInputBase()
        rms1.userInputCounts()
        rms1.depthCountPlot()


def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
