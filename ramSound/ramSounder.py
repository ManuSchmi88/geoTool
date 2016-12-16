#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Maybe the imports can go in the class? Is this better? so much I do not know..."""
import numpy as np
import matplotlib
matplotlib.use("TkAgg")#set to work with tkinter. Could lead to bugs?
from matplotlib import pyplot as plt
import soilCalc as sc

class RMS(object):
    """create a rammsounding class"""

    def __init__(self):
        """Initializes the rms-class and creates storage for depth and counts
        self.depth  = Array with 0.1m increments until end of rms
        self.counts = Array with same length as self.depth which stores countes per 0.1m """

        self.depth = []
        self.counts = []
        self.depthVec = []
        self.countVec = []

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

    def userInputCounts(self):
        """creates a vector with the corresponding rms-counts.
        Vector must have same length as depthVector"""

        tempCount = []

        for i in self.depthVec:
            while True:
                try:
                    inputString = "Counts at depth {}".format(self.depthVec[i])
                    tempCount.append(int(input("Counts at depth {:.2f}m: ".format(i))))
                    print("")
                except ValueError:
                    print("This is not a number you idiot. Try again!")
                else:
                    break

        self.countVec = tempCount.copy()

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

    def defGWLevel(self):
        """let user define a groundwater level."""
        while True:
            gwF = str(input("Did you measure Groundwaterlevel? "))
            if gwF == "y":
                inputStr = "Specify Groundwater level: "
                try:
                    self.gwLevel = float(input(inputStr))
                except ValueError:
                    print("This is not a number you idiot. Try again!")
                else:
                    break
            elif gwF == "n":
                print("Ok, nevermind than")
                break
            else:
                print("I did not unterstand that")


    def bulkDensity(self):
        """call soilCalc Module to add values for bulk density"""
        while True:
            bdf = str(input("Do you want to calculate bulk density of your profile (y/n) ?"))
            if bdf == "y":
                print('Ok. Calculating bulk density...')
                self.bd = sc.calcBulkDensity(self.rmsclass, self.depthVec,
                        self.countVec)
                break
            elif bdf == "n":
                print('Ok, I just sit here and do nothing.!')
                break
            else:
                print('I did not understand that')
                break
        if bdf == "y":
            while True:
                bdpF = str(input('Do you want to make a plot of the bulk density distribution (y/n) ?'))
                if bdpF == "y":
                    sc.plotBulkDensity(self.bd, self.depthVec)
                    break
                elif bdf == "n":
                    print('Well then, ok!')
                    break
                else:
                    print('I did not unterstand that')
