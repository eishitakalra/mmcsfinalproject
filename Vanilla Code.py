# Attempt 1 at basic code assigning a movie/ads spaces to a schedule

import numpy as np
import math 
import pandas as pd
import scipy as sp

# read in files 
ch_0_conversion_rates = pd.read_csv('/workspaces/mmcsfinalproject/channel_0_conversion_rates.csv')
ch_0_schedule = pd.read_csv('/workspaces/mmcsfinalproject/channel_0_schedule.csv')
ch_1_conversion_rates = pd.read_csv('/workspaces/mmcsfinalproject/channel_1_conversion_rates.csv')
ch_1_schedule = pd.read_csv('/workspaces/mmcsfinalproject/channel_1_schedule.csv')
ch_2_conversion_rates = pd.read_csv('/workspaces/mmcsfinalproject/channel_2_conversion_rates.csv')
ch_2_schedule = pd.read_csv('/workspaces/mmcsfinalproject/channel_2_schedule.csv')
ch_A_schedule = pd.read_csv('/workspaces/mmcsfinalproject/channel_A_schedule.csv')
movie_database = pd.read_csv('/workspaces/mmcsfinalproject/movie_database.csv')

#Testing that it worked
print(ch_0_conversion_rates.head(5))
