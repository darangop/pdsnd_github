# script Bike Share Data
# author: Diego Fernando Arango Perez
# Udacity - Python
# proyect #2

# import librarys
import time
import pandas as pd
import numpy as np

#The Datasets
#Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

#Start Time (e.g., 2017-01-01 00:07:57)
#End Time (e.g., 2017-01-01 00:20:53)
#Trip Duration (in seconds - e.g., 776)
#Start Station (e.g., Broadway & Barry Ave)
#End Station (e.g., Sedgwick St & North Ave)
#User Type (Subscriber or Customer)
#The Chicago and New York City files also have the following two columns:
#Gender
#Birth Year

# import datasets

DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    specify a city

    Returns:
        (str) city - name of the city
        (str) month - name of the month
        (str) day - name of the day
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    while True:
        cities= ['chicago','new york city','washington']
        city= input("\n Which city would you like to analyse? (Chicago, New york city, Washington) \n").lower()
        if city in cities:
            break
        else:
            print("\n Please enter a valid city name")    


    # get user input for month (january, february, ... , june or none)
    while True:
        months= ['January','February','March','April','June','May','None']
        month = input("\n Which month would you like to consider? (January, February, March, April, May, June)? Type 'None' for no month filter\n").title()
        if month in months:
            break
        else:
            print("\n Please enter a valid month")    


    # get user input for day of week (monday, tuesday, ... sunday or none)
    while True:
        days= ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','None']
        day = input("\n Which day of the week would you like to consider? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)? Type 'None' for no day filter \n").title()         
        if day in days:
            break
        else:
            print("\n Please enter a valid day")    
    


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data city

    Args:
        (str) city - name of the city
        (str) month - name of the month
        (str) day - name of the day
    Returns:
        df - Pandas DataFrame
    """

    
    # load data
    df = pd.read_csv(DATA[city])

    # column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month
    if month != 'None':
        # index of the months
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)+1
    
        # filter by month
        df = df[df['month']==month] 

    # filter by day
    if day != 'None':
        # create the new dataframe
        df = df[df['day_of_week']==day]

    return df


def time_stats(df,month,day):
    """most frequent times of travel."""

    print('\nMost Frequent Times of Travel\n')
    start_time = time.time()

    # most common month
    if month =='None':
        pop_month= df['month'].mode()[0]
        months= ['January','February','March','April','May','June']
        pop_month= months[pop_month-1]
        print("most Popular month",pop_month)


    # most common day
    if day =='None':
        pop_day= df['day_of_week'].mode()[0]
        print("most Popular day",pop_day)


    # most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    pop_hour=df['Start Hour'].mode()[0]
    print("popular Hour is {}:00 hrs".format(pop_hour))


    print("\ntime in %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """most popular stations and trip."""
    print('\nMost Popular Station and Trip\n')
    start_time = time.time()

    # most commonly first station
    pop_start_station= df['Start Station'].mode()[0]
    print("most commonly Station is {}".format(pop_start_station))


    # most commonly end station
    pop_end_station= df['End Station'].mode()[0]
    print("most commonly End Station is {}".format(pop_end_station))

    # most frequent start station and end station
    df['combination']=df['Start Station']+" "+"to"+" "+ df['End Station']
    pop_com= df['combination'].mode()[0]
    print("most frequent Start and End Station  {} ".format(pop_com))


    print("\ntime in %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """the total and average trip duration."""

    print('\nTrip Duration...\n')
    start_time = time.time()

    # total travel time
    total_duration=df['Trip Duration'].sum()
    minute,second=divmod(total_duration,60)
    hour,minute=divmod(minute,60)
    print("total trip time: {} hour(s) {} minute(s) {} second(s)".format(hour,minute,second))
    
    # avg travel time
    average_duration=round(df['Trip Duration'].mean())
    m,sec=divmod(average_duration,60)
    if m>60:
        h,m=divmod(m,60)
        print("total duration: {} hour(s) {} minute(s) {} second(s)".format(h,m,sec))
    else:
        print("total duration: {} minute(s) {} second(s)".format(m,sec))

    print("\ntime in %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """user stats."""

    print('\nUser Stats...\n')
    start_time = time.time()

    # counts of user types
    user_counts= df['User Type'].value_counts()
    print("user types:\n",user_counts)


    # counts of gender
    if city.title() == 'Chicago' or city.title() == 'New York City':
        gender_counts= df['Gender'].value_counts()
        print("\ncounts of gender:\n",gender_counts)
    
    # earliest, most recent, and most common year
        earliest= int(df['Birth Year'].min())
        print("\noldest user is born of the year",earliest)
        most_recent= int(df['Birth Year'].max())
        print("youngest user is born of the year",most_recent)
        common= int(df['Birth Year'].mode()[0])
        print("users are born of the year",common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def raw_data (df):
    """Displays the data due filteration.
    5 rows will added in each press"""
    print('press enter to see row data, press no to skip')
    x = 0
    while (input()!= 'no'):
        x = x+5
        print(df.head(x))

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


