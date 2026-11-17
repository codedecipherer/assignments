#worktime calculator
import numpy as np
import pandas as pd
import os
from IPython.display import display


first_name, last_name = input("Enter your first name and last name").split()

days = ["MON", "TUE", "WED", "THU", "FRI"]

time_table = {
              "hours_worked": [0,0,0,0,0],
              "wfh" : [False, False, False, False, False]
            }

timetable_df = pd.DataFrame(time_table)
timetable_df.index = days
timetable_df.columns.name = "day_of_the_week"


# def calculate_time(hours_worked, break_time):
#     break

def find_day(day):
    if "mon" in day:
        t_day = "MON"
    elif "tue" in day:
        t_day = "TUE"
    elif "wed" in day:
         t_day = "WED"
    elif "thu" in day:
         t_day = "THU"
    elif "fri" in day:
         t_day = "FRI"
    else:
        t_day = "None"
    return t_day

print("Welcome to the Apprentice Worktime Calculator for Leonardo Apprentices")
answer = input(""" What would you like to do? 
           Add in hours worked (A)
           Check your Worktime Chart (W)) """)
end = False
while end != True:
    if answer.lower() == "a":
        day = input("Enter the day of the week you would like to log: ").lower()
        hours_worked = float(input("Enter the amount of hours worked: "))
        break_time = float(input("Enter how long the break taken was: "))

        t_day = find_day(day)

        timetable_df.loc[t_day,"hours_worked"] = hours_worked
         
        end = True

        # calculate_time(hours_worked, break_time)




display(timetable_df)
# add hours worked to data frame
# ask for day of the week
# ask hours worked today
# how long break 
