import gc
#
def clear_all():
    # Clears all the variables from the workspace
    gl = globals().copy()
    for var in gl:
        if var in clean_env_var: continue
        del globals()[var]
    # Garbage collection:
    gc.collect()
#
import matplotlib.pyplot as plt
#
def close_plots():
  my_plots = plt.get_fignums()
  for j in my_plots:
    plt.close(plt.figure(j))
#
clean_env_var = dir()
clean_env_var.append('clean_env_var')

print(clean_env_var)

import numpy as np
import statsmodels.api as sm
import scipy.stats as stats
import scipy.optimize as optimize
import pandas as pd
#
import statsmodels.api as sm
#
cars = sm.datasets.get_rdataset("cars", "datasets")
print(cars.data.head())