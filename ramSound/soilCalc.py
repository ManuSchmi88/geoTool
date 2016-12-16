import numpy as np
import matplotlib
matplotlib.use("TkAgg")#set to work with tkinter. Could lead to bugs?
from matplotlib import pyplot as plt


def calcBulkDensity(rmsClass, rmsDepthVec, rmsCountVec):
        """uses the equation after "Witt - Grundbau Taschenbuch" """

        #Dictionary which holds different paramters for RMS type
        paramDict = {'light':[0.25, 0.1] , 'medium':[0.35, 0.2] , 'heavy':[0.4, 0.4]}
        a1 = paramDict[rmsClass][0]
        a2 = paramDict[rmsClass][1]
        depthVec = rmsDepthVec
        Id = a1 + a2 * np.log(rmsCountVec)
        return Id
   
def plotBulkDensity(bulkDensity, depthVec):

        """Create a nice plot of depth vs. counts"""
        fig, ax = plt.subplots(figsize=[8,9])
        profile = plt.plot(bulkDensity,depthVec,'r-',linewidth=1.5)
        plt.xlim([0,max(bulkDensity)+1])
        plt.ylim([max(depthVec),0])
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
