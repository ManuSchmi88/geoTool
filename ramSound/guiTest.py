import tkinter as tk
import tkinter.ttk as ttk
import ramSounder as Rs

class MainProgramm(tk):
    
   def __init__(self):
      '''
      Constructor
      '''
      self.root = tk.Tk()
      self.frame = tk.Frame(self.root)
      self.frame.pack()
      self.title('Simple RMS Plotter')

   def user_interface(self):
      '''
      Initialize the user interface we all need and deserve
      '''
      #Create Treeview and List for Stuff and stuff
      self.countList = []
      header = ['Depth [m]' , 'Counts']
      self.treeL = ttk.Treeview(columns = header, show = 'headings')
      self.treeL.grid(in_ = self.frame) 
      for col in header:
         self.tree.heading(col, text=col.title())
      for item in self.countlist:
         self.tree.insert('', 'end', values=item)

      #Create Buttons and more stuff and stuff
      self.but1 = tk.Button(self.root,text = 'Enter',command = submit)
      self.but1.pack()
      
      #Create entry lists and more stuff
      self.entr1 = tk.Entry(self.root)
      self.entr1.pack()
  
   def submit():
      addToList(self.entr1.get())

   def addToList(self):
      listAdder = (self.entr1.get())
      self.countList.append(listAdder)
      for item in self.countList:
         self.treeV.insert('', 'end', values  = item)
      print(listAdder)

   def end():
      self.root.mainloop()

#This is somehow needed.
def main():
    d = MainProgramm()

if __name__  == '__main__':
    main()
