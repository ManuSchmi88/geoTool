"""Maybe the imports can go in the class? Is this better? so much I do not know..."""
import numpy as np
import matplotlib.pyplot as plt
    

class RMS(object):
    """create a rammsounding class"""

    def __init__(self):
        """Initializes the rms-class and creates storage for depth and counts
        self.depth  = Array with 0.1m increments until end of rms
        self.counts = Array with same length as self.depth which stores countes per 0.1m """
                
        self.depth = []
        self.counts = []
        
    def rmsClassify(self):
        """"Asks the user to define which sort of rammsounding they did:
        Light, Medium or Heavy"""
        
        classDict = {'l' : 'light' , 'm' : 'medium' , 'h' : 'heavy'}
        cV = -9999
        
        while True :
            cV = input("Sort of ramsounding ?(type 'l' for light, 'm' for medium, 'h' for heavy) : ")
            if cV == "m":
                break
            elif cV == "l":
                break
            elif cV == "h":
                break
            else:
                print("I did not understand that.")
        self.rmsclass = classDict[cV]
        
    
    def userInputBase(self):
        """This is the main input function which asks the user about stuff"""
        
        while True:
            try:
                self.startDepth = float(input("Where did you start counting?  "))
            except ValueError:
                print("I need a number to work, sir.")
            else:
                break
                
        while True:
            try:
                self.endDepth   = float(input("How deep is your rms?  "))
            except ValueError:
                print("I need a number to work, sir.")
            else:
                break
                
        self.depthLength = self.endDepth - self.startDepth
        self.depthVec = np.arange(self.startDepth,self.endDepth+0.1, 0.1)
        self.deepen()
        
    def userInputCounts(self):
        """creates a vector with the corresponding rms-counts.
        Vector must have same length as depthVector"""
        
        tempCount = []
        
        for i in self.depthVec:
            while True:
                try:
                    inputString = "Counts at depth {}".format(self.depthVec[i])
                    tempCount.append(int(input("Counts at depth {:f}:  ".format(i))))
                except ValueError:
                    print("This is not a number you idiot. Try again!")
                else:
                    break
        
        self.countVec = tempCount.copy()
        
    def deepen(self):
        """Calculates depth-vector and appends it to self.depth"""

        self.depthLength = self.endDepth - self.startDepth
        self.depthVec = np.arange(self.startDepth,self.endDepth+0.1, 0.1)
        
    def depthCountPlot(self):
        """Create a nice plot of depth vs. counts"""
        fig, ax = plt.subplots(figsize=[8,9])
        profile = plt.plot(self.countVec,self.depthVec,'r-',linewidth=1.5)
        plt.xlim([0,max(self.countVec)+5])
        plt.ylim([max(self.depthVec),0])
        #Moves the label and the ticks to top of the plot
        ax.xaxis.set_ticks_position('top')
        ax.xaxis.set_label_position('top')
        #Axis label and format
        ax.xaxis.set_label_text("RMS Counts", fontsize = 21)
        ax.yaxis.set_label_text("Depth [m]", fontsize = 19)
        ax.tick_params(labelsize = 11)
        #Shows Grid
        plt.grid()
        plt.show()
