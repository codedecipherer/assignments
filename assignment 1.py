#worktime calculator
import numpy as np
import pandas as pd
import os

first_name, last_name = input("Enter your first name and last name").split()

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
time_table = {"day_of_the week": [],
              "hours_worked[": [],
              "wfh" : []
            }

timetable_df = pd.DataFrame()

print(timetable_df.to_markdown())
# add hours worked to data frame
# ask for day of the week
# ask hours worked today
# how long break 
