import netCDF4
import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sns


def combinePlot():
   plt.close('all')
   plt.style.use('seaborn-white')
   directory = os.getcwd() +'/files'
   os.chdir(directory)
   nColour = len(os.listdir(directory)) # use files in directory to determine number of colours required for gradient
   seq_col_brew = sns.cubehelix_palette(nColour, start=2, rot=0, dark=0, light=0.70, reverse=False) # define colour gradient
   sns.set_palette(seq_col_brew) # set colour gradient
   fig = plt.figure()
   ax = fig.add_subplot(111)
   axes = plt.gca()
   
   for file in os.listdir(directory):
      filename = os.fsdecode(file)
      if filename.endswith(".CDF"): 
         data  = netCDF4.Dataset(filename, mode='r')
         chrom = data['ordinate_values'][:]*1000                 # convert from mV to V
         yLim  = 100 # max(chrom)+5                                    # set plot y-axis limit to maximum value + 5
         runTime = int(data['actual_run_time_length'][:])/60     # convert seconds to minutes
         timeR   = np.linspace(0,runTime,len(chrom))             # create time array with same number of ordinate values from 0 to runTime 
         plt.plot(timeR, chrom, label=filename[0:10])             # plot and attach legend label with HPLC filename first 5 letters ([0:6])

   axes.set_ylim([0,yLim]) # Set y limits for graph
   plt.legend()
   plt.xticks(np.arange(min(timeR), max(timeR)+1, 2), rotation='vertical', visible=True) # define x-axis tick spacing (currently set at 2 [min])
   plt.xlabel('Retention time (min)')      # x-label
   plt.ylabel('Signal (mV)')               # y-label
   os.chdir('..')                          # change to directory of python file
   figname = 'plotCombined.png'            # file name for combined plots
   plt.savefig(figname, dpi=1000)          # save plot
   plt.show()                              # plot preview

combinePlot()