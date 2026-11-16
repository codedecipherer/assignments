#worktime calculator
import numpy as np
import pandas as pd
import os

first_name, last_name = input("Enter your first name and last name").split()

time_table = {"day_of_the week": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
              "hours_worked":[],
              "wfh": []
            }

timetable = pd.DataFrame(time_table)

print(timetable)
# add hours worked to data frame
# ask for day of the week
# ask hours worked today
# how long break 
