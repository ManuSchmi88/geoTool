import tkinter as tk
import tkinter.ttk as ttk
import ramSounder as rs

class Test:
   def __init__(self):
      self.wi = tk.Tk()
      self.make_interface()
      self.treeList = []
      self.depthV = []
      self.countV = []

   def make_interface(self):
      
      #set up title 
      self.wi.title('RMS Plotter')
      self.wi.config(background='white')
    
      #Set up tree-viewtable for depths and counts
      header = ['Depth' , 'Counts']
      self.treel = ttk.Treeview(columns = header, show = 'headings')
      self.treel.grid(row = 1, column = 0)
      for col in header:
          self.treel.heading(col, text=col.title())

      #Set up Labels for Entry-Fields for Depth and Counts
      tk.Label(self.wi, text = 'Rammsondier Plotter').grid(row=0 , column = 0)
      tk.Label(self.wi, text = 'Depth').grid(row=2, column=1)
      tk.Label(self.wi, text = 'Counts').grid(row=3,column=1)

      #Set up Entry-Fields for Depth and Counts
      self.e1 = tk.Entry(self.wi)
      self.e2 = tk.Entry(self.wi)
      self.e1.grid(row = 2, column = 2)
      self.e2.grid(row = 3, column = 2)

      #set up "submit" button
      self.b1 = tk.Button(self.wi, text = 'Enter',
              command = self.submitDepthCounts).grid(row = 4, column = 2)

      #set up select button for bugfixing
      self.b2 = tk.Button(self.wi, text = 'Select',
              command = self.plotDepthCounts).grid(row = 5, column = 2)

   def submitDepthCounts(self):
      self.nDep = self.e1.get()
      self.nCou = self.e2.get()
      self.treel.insert('','end',values = (self.nDep,self.nCou))
      #This gets called everytime the button is pressed and updates the vectors
      self.createVecs()

   def createVecs(self):
      self.depthV.append(int(self.nDep))
      self.countV.append(int(self.nCou))

   def selectAndPrint(self):
      selItem = self.treel.focus()
      dictItem = self.treel.item(selItem)
      print('Your selected values are: {}'.format(dictItem['values']))

   def plotDepthCounts(self):
      rms = rs.RMS()
      rms.depthVec = self.depthV
      rms.countVec   = self.countV
      rms.depthCountPlot()

def main():
    d = Test()
    d.wi.mainloop()
if __name__ == "__main__":
    main()
