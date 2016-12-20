import numpy as np
import matplotlib
matplotlib.use("TkAgg")#set to work with tkinter. Could lead to bugs?
from matplotlib import pyplot as plt


def calcBulkDensity(rmsClass, rmsDepthVec, rmsCountVec):
        """uses the equation after Witt - Grundbau Taschenbuch """

        #Dictionary which holds different paramters for RMS type
        paramDict_Sa_OGW = {'light':[0.15, 0.26], 'heavy':[0.10, 0.435]}
        paramDict_Sa_UGW = {'light':[0.21, 0.23], 'heavy':[0.23, 0.380]}
        paramDict_SaGr_OGW = {'heavy':[-0.14, 0.550]}
        #Create a master-dictionary which keeps the others as a nested
        masterDict = {'SaOGW' : paramDict_Sa_OGW ,
                      'SaUGW' : paramDict_Sa_OGW ,
                      'SaGrOGW' : paramDict_SaGr_OGW}
        a1 = paramDict[paramD][0]
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
