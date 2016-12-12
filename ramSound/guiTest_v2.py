import tkinter as tk
import tkinter.ttk as ttk

class Test:
   def __init__(self):
      self.wi = tk.Tk()
      self.make_interface()

   def make_interface(self):
      self.wi.title('RMS Plotter')
      self.wi.config(background='lavender')
      
      tk.Label(self.wi, text = 'Hello').grid(row=0)
      tk.Label(self.wi, text = 'Sexy').grid(row=1)

      self.e1 = tk.Entry(self.wi)
      self.e2 = tk.Entry(self.wi)

      self.e1.grid(row = 0, column = 1)
      self.e2.grid(row = 1, column = 1)

def main():
    d = Test()
    d.wi.mainloop()
if __name__ == "__main__":
    main()
