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
movie_database_small = movie_database.head(50)

#Testing that it worked
#print(ch_0_conversion_rates.head(5))
#print(movie_database_small)

#create time_schedule
time_schedule = (ch_A_schedule.iloc[:, :1])
time_schedule_small = time_schedule.head(204)

#print(time_schedule)

#Pull movie, take run time and divide into time intervals

#Pull movie, take run time and divide into time intervals
for i in movie_database_small:
  num_slots = movie_database_small['runtime_with_ads'] / 5

#
# let x_it = movie i runs in time slot t

for i in movie_database_small:
    for t in time_schedule_small: 
        sum(x_it) == 204

from pulp import LpVariable, LpProblem, LpMaximize

# Create a sample problem
model = LpProblem("Optimization_Problem", LpMaximize)

# Define a decision variable x_i,t for indices i and t
# Here, `lowBound` and `upBound` set the bounds if needed, `cat` defines the type (e.g., continuous)
i_values = [1, 2, 3]  # Example values for i
t_values = [1, 2]     # Example values for t

# Create a dictionary of decision variables
x = {(i, t): LpVariable(f"x_{i}_{t}", lowBound=0, cat="Continuous") for i in i_values for t in t_values}

