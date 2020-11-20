#**************************************************************
# Import Modules
import time
import pandas as pd
import numpy as np
import BikeShare_Project_Functions as f
from os import system, name
from time import sleep
from collections import Counter
import sys as s

#**************************************************************
# Set global variables
city_data = { 'c': 'chicago.csv',
              'n': 'new_york_city.csv',
              'w': 'washington.csv' }
city_trans = { 'c': 'Chicago',
              'n': 'New York City',
              'w': 'Washington' }
month_list = { 1: 'Janaury',
              2: 'February',
              3: 'March',
              4: 'April',
              5: 'May',
              6: 'June',
              7: 'July',
              8: 'August',
              9: 'September',
              10: 'October',
              11: 'November',
              12: 'December' }
day_list = { 0: 'Monday',
              1: 'Tuesday',
              2: 'Wednesday',
              3: 'Thursday',
              4: 'Friday',
              5: 'Saturday',
              6: 'Sunday' }

filters = ''
merge_df = pd.DataFrame()
f_cities = ''
f_months = ''
f_days = ''
f_stats = ''


#**************************************************************
# Start Program
#**************************************************************

# Clear screen before running program
f.clear()


#**************************************************************
# Get Data Filters
#**************************************************************
filters = f.get_filters()

if filters == 'Error':
    s.exit()
else:
    cities = filters[0].split(',')
    months = filters[1].split(',')
    days = filters[2].split(',')
    stats = filters[3].split(',')

    #print('\nUser Inputs are: {}'.format(filters))
    #print('\nCity Filters are: {}'.format(cities))
    #print('\nMonths Filters are: {}'.format(months))
    #print('\nDays Filters are: {}'.format(days))
    #print('\nStats Filters are: {}'.format(stats))



#**************************************************************
# Load data into DataFrame
#**************************************************************
# Load data files into DataFrames
for city in cities:

    if 'a' in city.lower():

        for key, value in city_data.items():
            df = pd.read_csv(value)
            merge_df = merge_df.append(df)
            #print('Shape after {} DF: {}'.format(value, len(merge_df.index)))

    elif 'c' in city.lower():
        df = pd.read_csv(city_data[city])
        merge_df = merge_df.append(df)
        #print('Shape after C DF: {}'.format(len(merge_df.index)))

    elif 'n' in city.lower():
        df = pd.read_csv(city_data[city])
        merge_df = merge_df.append(df)
        #print('Shape after N DF: {}'.format(len(merge_df.index)))

    elif 'w' in city.lower():
        df = pd.read_csv(city_data[city])
        merge_df = merge_df.append(df)
        #print('Shape after W DF: {}'.format(len(merge_df.index)))

#print('Shape of Merge DF: {}'.format(len(merge_df.index)))


# *****************************************************************************
# Alter/append records to DataFrame
# *****************************************************************************

# convert the Start Time column to datetime
merge_df['Start Time'] = pd.to_datetime(merge_df['Start Time'])

# Add columns to DataFrame
merge_df['Month'] = merge_df['Start Time'].dt.month
merge_df['Day of Week'] = merge_df['Start Time'].dt.weekday
merge_df['Hour of Day'] = merge_df['Start Time'].dt.hour
merge_df['Trip Stations'] = merge_df['Start Station'] + ' [To] ' + merge_df['End Station']
if 'w' not in city.lower():
    merge_df['Gender']  = merge_df['Gender'].fillna('Undefined')
    merge_df['Birth Year']  = merge_df['Birth Year'].fillna(int(1900))


# *****************************************************************************
# Apply filters to DataFrame
# *****************************************************************************

# Apply month filter if requested by user
if int(months[0]) != 0:
#if '0' not in months:
    #print('Apply month filters: {} '.format(months))
    merge_df = merge_df[merge_df['Month'].isin(months)]

#print('Shape of Merge DF after Month filters: {}'.format(len(merge_df.index)))

# Apply day filter if requested by user
if int(days[0]) != 7:
#if '0' not in months:
    #print('Apply day filters: {} '.format(days))
    merge_df = merge_df[merge_df['Hour of Day'].isin(days)]

#print('Shape of Merge DF after Day filters: {}'.format(len(merge_df.index)))


# *****************************************************************************
# Display Chosen Filters to User
# *****************************************************************************
# Clear screen before displaying results
f.clear()

print('\n***************************\nData Filters\n***************************')

# Compile City Filters
if 'a' in city.lower():
    for key, value in city_trans.items():
        f_cities = f_cities + '[' + value + '] '
else:
    for city in cities:
        f_cities = f_cities + '[' + city_trans[city] + '] '

# Compile Month Filters
if '0' in months:
    for key, value in month_list.items():
        f_months = f_months + '[' + value + '] '
else:
    for month in months:
        f_months = f_months + '[' + month_list[int(month)] + '] '

# Compile Day Filters
if '7' in days:
    for key, value in day_list.items():
        f_days = f_days + '[' + value + '] '
else:
    for day in days:
        f_days = f_days + '[' + day_list[int(day)] + '] '


print('City Filters are: {}'.format(f_cities))
print('Month Filters are: {}'.format(f_months))
print('Day Filters are: {}'.format(f_days))


# *****************************************************************************
# Display popular travel time data
# *****************************************************************************

print('\n***************************\nPopuler Travel Time of Travel\n***************************')

# Display travel data if requested by user
if any(x in stats for x in [str(0), str(1)]):

    # Display most common month data
    # Creating a counter object
    count = Counter(merge_df['Month'])
    cntr = 1
    # Calling a method of Counter object(count)
    disply_txt = count.most_common(3)
    print('\n== The most common month(s) for bike rentals are: =========================================')
    for item in disply_txt:
        print('\t{} - {} with a total of {} records'.format(cntr, month_list[item[0]], item[1]))
        cntr += 1

    # Display most common day of week
    # Creating a counter object
    count = Counter(merge_df['Day of Week'])
    cntr = 1
    # Calling a method of Counter object(count)
    disply_txt = count.most_common(3)
    print('\n== The most common day(s) of the week for bike rentals are: ================================')
    for item in disply_txt:
        print('\t{} - {} with a total of {} records'.format(cntr, day_list[item[0]], item[1]))
        cntr += 1

    # Display most common hour of day
    # Creating a counter object
    count = Counter(merge_df['Hour of Day'])
    cntr = 1
    # Calling a method of Counter object(count)
    disply_txt = count.most_common(3)
    print('\n== The most common hour(s) of the day for bike rentals are: ================================')
    for item in disply_txt:
        print('\t{} - {} with a total of {} records'.format(cntr, item[0], item[1]))
        cntr += 1


# *****************************************************************************
# Display popular trip data
# *****************************************************************************

print('\n***************************\nPopuler Stations and Trip\n***************************')

if any(x in stats for x in [str(0), str(2)]):

    # Display most common start station
    # Creating a counter object
    count = Counter(merge_df['Start Station'])
    cntr = 1
    # Calling a method of Counter object(count)
    disply_txt = count.most_common(3)
    print('\n== The most common start station(s) for bike rentals are: =========================================')
    for item in disply_txt:
        print('\t{} - {} with a total of {} records'.format(cntr, item[0], item[1]))
        cntr += 1

    # Display most common end station
    # Creating a counter object
    count = Counter(merge_df['End Station'])
    cntr = 1
    # Calling a method of Counter object(count)
    disply_txt = count.most_common(3)
    print('\n== The most common end station(s) for bike rentals are: ================================')
    for item in disply_txt:
        print('\t{} - {} with a total of {} records'.format(cntr, item[0], item[1]))
        cntr += 1

    # Display most common trip data
    # Creating a counter object
    count = Counter(merge_df['Trip Stations'])
    cntr = 1
    # Calling a method of Counter object(count)
    disply_txt = count.most_common(3)
    print('\n== The most common trip(s) for bike rentals are: ================================')
    for item in disply_txt:
        print('\t{} - {} with a total of {} records'.format(cntr, item[0], item[1]))
        cntr += 1


# *****************************************************************************
# Display travel time data
# *****************************************************************************

print('\n***************************\nTrip Duration\n***************************')

if any(x in stats for x in [str(0), str(3)]):

    # Display total travel time
    print('\n== The Total Trip Duration is: =========================================')
    print('\t{} Minutes'.format(float(merge_df['Trip Duration'].sum()/60)))

    print('\n== The Average Trip Duration is: =========================================')
    print('\t{} Minutes'.format(float(merge_df['Trip Duration'].mean())/60))


# *****************************************************************************
# Display user data
# *****************************************************************************

print('\n***************************\nUser Info\n***************************')

if any(x in stats for x in [str(0), str(4)]):
    # Display user type breakdown
    print('\n== The User Type Summary is: =========================================')
    print(merge_df['User Type'].value_counts())

    if 'w' in city.lower():
        print('\nNo Gender/Birth Year data available for Washington')
    else:
        # Display gender breakdown
        print('\n== The Gender Summary is: =========================================')
        print(merge_df['Gender'].value_counts())

        # Display most common month data
        print('\n== The earliest birth year is: =========================================')
        print('\t{}'.format(int(merge_df['Birth Year'].min())))

        print('\n== The most recent birth year is: =========================================')
        print('\t{}'.format(int(merge_df['Birth Year'].max())))

        # Display most common birth year

        # Create DF to filter our 1900 values (replaced NaN w/ 1900)
        by_df = merge_df[merge_df['Birth Year'] != 1900]
        # Creating a counter object
        count = Counter(by_df['Birth Year'])
        cntr = 1
        # Calling a method of Counter object(count)
        disply_txt = count.most_common(3)
        print('\n== The top 3 most common birth years for bike rentals are: ================================')
        for item in disply_txt:
            print('\t{} - {} with a total of {} records'.format(cntr, int(item[0]), item[1]))
            cntr += 1

# Add a line return after displaying stats
print('\n')
 

# *****************************************************************************
# Display raw data if requested by user
# *****************************************************************************
start_record = 0
end_record = 5

while f.display_raw_data() is True:
    print(df[start_record : end_record])
    start_record  = start_record + 5
    end_record = end_record + 5


# Add some line returns after program completes
print('\n\n')
# *****************************************************************************
