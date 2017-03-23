import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sciopt

#Load CSV Columns
sweep_csv_file = '../MeasurementData/VariableSpeedSweep.csv'
sweep_df = pd.read_csv(sweep_csv_file, sep='\t', header=1)
sweep_matrix_rows = sweep_df.as_matrix()
sweep_matrix_columns = sweep_matrix_rows.transpose()
magnetCurrent, lockin1, lockin2, time = sweep_matrix_columns

#Numerical Analysis
magnetCurrentDiffs = np.ediff1d(magnetCurrent)
lockin1Diffs = np.ediff1d(lockin1)
lockin2Diffs = np.ediff1d(lockin2)
timeDiffs = np.ediff1d(time)
magnetCurrentTimeDeriv = magnetCurrentDiffs / timeDiffs

#Plot Data
plt.plot(time, magnetCurrent)
plt.show()
plt.plot(time, lockin1)
plt.show()
plt.plot(time, lockin2)
plt.show()
plt.plot(time[1:], magnetCurrentTimeDeriv)
plt.show()
