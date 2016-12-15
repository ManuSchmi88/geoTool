#!/usr/bin/env python
# -*- coding: utf-8 -*-

class soil():
    """Class that incorportates the soil parameter.
    Important input will be:
        - Groundwater depth
        - Type of soil """
    def __init__(self):

        """initializes needed containers"""

        #Can be tuple? Don't change after set-up
        self.type = ()
        self.gwD  = ()

    def initStrati(self):
        """Asks the user if he want to specify a stratigraphy"""

        inputStr = "Do you want to specify a stratigraphy (y/n) ?"
        callFlag = input(inputStr)

    def stratiProfiler(self):
