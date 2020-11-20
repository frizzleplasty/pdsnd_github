
import time
import pandas as pd
import numpy as np
from os import system, name
from time import sleep
import sys as s

#**************************************************************
# Define function that gets data filters
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("\
==============================================================\n \
Enter the first letter of the City you would like query.\n\n \
To select more than one city, put a comma in between selections.\n \
        A for All Cities\n \
        C for Chicago\n \
        N for New York City\n \
        W for Washington\n \n \
Select City(ies): ")

    #Check for valid city values
    city_split = city.split(',')
    for value in city_split:
        #print('Value is {} and Len is {}'.format(value, len(value)))
        if value.lower() not in ('a','c','n','w'):
            clear()
            print('Ending Program.\nIncorrect City Value Entered: {}\n'.format(value))
            sleep(2)
            s.exit()
            return 'Error'

        elif value.lower() in ('a') and len(city) > 1:
            clear()
            print('Ending Program.\nOnly one value can be entered when selecting all cites\n'.format(value))
            sleep(2)
            s.exit()
            return 'Error'


    # get user input for month (all, january, february, ... , june)
    month = input("\n\
==============================================================\n \
Enter the number for month(s) you would like to query.\n\n \
To select more than one month, put a comma in between selections.\n \
        0 for All\n \
        1 for January       2 for February\n \
        3 for March         4 for April\n \
        5 for May           6 for June\n \
        7 for July          8 for August\n \
        9 for September     10 for October\n \
        11 for November     12 for December\n \n \
Select Month(s): ")

    #Check for valid month values
    month_split = month.split(',')
    for value in month_split:
        #print('Value is {} and Len is {}'.format(value, len(value)))
        if is_int(value) == False:
            clear()
            print('Ending Program.\nOnly integers are allowed for months. Invalid value: {}\n'.format(value))
            sleep(2)
            s.exit()
            return 'Error'

        elif 0 < int(value) > 12:
            clear()
            print('Ending Program.\nPlease enter value between 0 and 12 for months. Invalid value: {}\n'.format(value))
            sleep(2)
            s.exit()
            return 'Error'

        elif value == '0' and len(month) > 1:
            clear()
            print('Ending Program.\nOnly one value can be entered when selecting all months. Invalid value: {}\n'.format(value))
            sleep(2)
            s.exit()
            return 'Error'

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\n\
==============================================================\n \
Enter the number for day(s) you would like to query.\n\n \
To select more than one day, put a comma in between selections.\n \
        7 for All\n \
        0 for Monday       1 for Tuesday\n \
        2 for Wednesday    3 for Thursday\n \
        4 for Friday       5 for Saturday\n \
        6 for Sunday\n \n \
Select Days(s): ")

    #Check for valid day values
    day_split = day.split(',')
    for value in day_split:
        #print('Value is {} and Len is {}'.format(value, len(value)))
        if is_int(value) == False:
            clear()
            print('Ending Program.\nOnly Integers are allowed for days. Invalid value: {}\n'.format(value))
            sleep(2)
            s.exit()
            return 'Error'

        elif 0 < int(value) > 7:
            clear()
            print('Ending Program.\nPlease enter value between 0 and 7 for days. Invalid value: {}\n'.format(value))
            sleep(2)
            s.exit()
            return 'Error'

        elif value == '7' and len(day) > 1:
            clear()
            print('Ending Program.\nOnly one value can be entered when selecting all days. Invalid value: {}\n'.format(value))
            sleep(2)
            s.exit()
            return 'Error'

    # get user input for stats returned
    stat = input("\n\
==============================================================\n \
Enter the number for stat(s) you would like to query.\n\n \
To select more than one stat, put a comma in between selections.\n \
        0 for All\n \
        1 for Popular Time of Travel\n \
        2 for Popular Stations and Trips\n \
        3 for Trip Duration\n \
        4 for User info\n \n \
Select Stat(s): ")

    #Check for valid day values
    stat_split = stat.split(',')
    for value in stat_split:
        #print('Value is {} and Len is {}'.format(value, len(value)))
        if is_int(value) == False:
            clear()
            print('Ending Program.\nOnly Integers are allowed for stats. Invalid value: {}\n'.format(value))
            sleep(2)
            s.exit()
            return 'Error'

        elif 0 < int(value) > 4:
            clear()
            print('Ending Program.\nPlease enter value between 0 and 4 for stats. Invalid value: {}\n'.format(value))
            sleep(2)
            s.exit()
            return 'Error'

        elif value == '0' and len(stat) > 1:
            clear()
            print('Ending Program.\nOnly one value can be entered when selecting all stats. Invalid value: {}\n'.format(value))
            sleep(2)
            s.exit()
            return 'Error'

    #print('-'*40)
    #return city
    return city.lower(), month.lower(), day.lower(), stat.lower()

#**************************************************************
# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#**************************************************************
# define check integer function
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#**************************************************************
# Ask if user would like to see raw data
def display_raw_data():
    view_data = input("\nWould you like to view 5 lines of raw data? Y/N: ")
    valid_values = ('n','y')

    #If string is more that 1 char, fail validation
    if len(view_data) > 1:
        print('\nInvalid value entered\n')
        display_raw_data()

    #Check if value entered is valid, fail validation if not
    if any (x in view_data.lower() for x in valid_values):
        print('')
    else:
        print('\nInvalid value entered\n')
        display_raw_data()

    if 'y' in view_data.lower():
        return True
    else:
        return False
