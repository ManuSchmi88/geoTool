import numpy as np
import matplotlib
matplotlib.use("TkAgg")#set to work with tkinter. Could lead to bugs?
from matplotlib import pyplot as plt

class soilCalc():
    """This class will handle the calculation of the different soil paramters.
    I guess this is a good thing to keep in a class ? Because of the
    different parameters for different rms locations?
    But think about moving it just in a function script and add the values to the
    rms.class... maybe better?"""

    def __init__(self):
        """So far this method is shit. We need to change a1 and a2
        according to different soil types, rms-type and groundwater..."""

        self.a1 = 0.15
        self.a2 = 0.21

    def bulkDensity(self,rmsDepthVec, rmsCountVec):
        """uses the equation after "Witt - Grundbau Taschenbuch" """

        self.depthVec = rmsDepthVec
        self.Id = self.a1 + self.a2 * np.log(rmsCountVec)

    def plotBulkDensity(self):

        """Create a nice plot of depth vs. counts"""
        fig, ax = plt.subplots(figsize=[8,9])
        profile = plt.plot(self.Id,self.depthVec,'r-',linewidth=1.5)
        plt.xlim([0,max(self.Id)])
        plt.ylim([max(self.depthVec),0])
        #Moves the label and the ticks to top of the plot
        ax.xaxis.set_ticks_position('top')
        ax.xaxis.set_label_position('top')
        #Axis label and format
        ax.xaxis.set_label_text("Bulk Density", fontsize = 21)
        ax.yaxis.set_label_text("Depth [m]", fontsize = 19)
        ax.tick_params(labelsize = 11)
        #Shows Grid
        plt.grid()
        plt.show()
