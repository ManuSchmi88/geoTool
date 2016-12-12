"""This is the main wrapping function for the rms - plotter"""

import ramSounder as rs

def main():
   rms1 = rs.RMS()
   rms1.userInputBase()
   rms1.userInputCounts()
   rms1.depthCountPlot()
   

if __name__ == "__main__":
    main()
