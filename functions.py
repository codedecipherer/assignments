#calculates total weekly hours and flexi(extra) hours worked
def calculate_flexi_time(df):
    #extra hours initialised to 0
    flexi_time = 0.0
    #uses .sum method to add up all numbers in the hours_worked column
    total_hours = float(df["hours_worked"].sum())
    #calculates if user has any extra hours 
    hours_left = 37 - total_hours

    #checks if the variable is negative, if so extra hours are added to flexi time
    if hours_left < 0:
        flexi_time -=hours_left
        hours_left = 0.0
    #displays values
    print(f"You have worked {total_hours:.1f}hrs this week")
    print(f"You have {hours_left:.1f}hrs left to work this week")
    print(f"You have {flexi_time:.1f}hrs of flexi time")

#finds the correct day of the week using 'in' to see if input contains the substring
def find_day(day):
    #checks if variable contains substring
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
        
#enters all user's input passed into function, into the dataframe
def modify_timetable(df,t_day, hours_worked, wfh, break_time, fn, ln):
    #display's user's full name
    print(f'{fn} {ln}\'s timesheet:')
    #calculates total time worked for the day
    total_time = hours_worked - break_time
    #using the .loc function to enter specific values, into row and column
    df.loc[t_day,"hours_worked"] = total_time
    df.loc[t_day,"wfh"] = wfh
    df.loc[t_day,"break_time"] = break_time
