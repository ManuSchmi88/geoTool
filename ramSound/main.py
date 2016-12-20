""" Main script which runs the functions for one ramsounding"""

import ramSounder as rs
import soilCalc as sc

def main():

    rms1 = rs.RMS()
    rms1.rmsClassify()
    rms1.chooseSoilType()
    rms1.userInputBase()
    rms1.userInputCounts()
    rms1.depthCountPlot()
    rms1.bulkDensity()

if __name__ == '__main__':
    main()
