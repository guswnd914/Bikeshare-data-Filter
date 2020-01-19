import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which city? Choose from (chigaco, new york city, washington). Write the word EXACTLY pease. \n: ')
    city = city.lower()
    while city not in CITY_DATA:
        print('Wrong city. Do it again')
        city = input('Which city? :')
        city = city.lower()

    month = input("Which month? ex. january, march; \nIf you want all month, please type 'all'.\n : ")
    month = month.lower()
    while month not in ['all', 'january', 'february', 'march','april','may','june']:
        print('Wrong month. Do it again.')
        month = input('Which month? : ')
        month = month.lower()

    day = input("Which day? ex. monday, wednesday;\nif you want all day, please type 'all'.\n : ")
    day = day.lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] :
        print('Wrong day. Do it again.')
        day = input('Which day? :')
        day = day.lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    if city == 'chicago':
        df = pd.read_csv('chicago.csv')
    elif city == 'new york city':
        df = pd.read_csv('new_york_city.csv')
    else:
        df = pd.read_csv('washington.csv')

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    if month != 'all':
        months = ['january','february','march','april','may','june']
        month1 = months.index(month) + 1
        df = df[df['Start Time'].dt.month == month1]
    if day != 'all':
        df = df[df['Start Time'].dt.weekday_name == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January','February','March','April','May','June']
    common_month = df['Start Time'].dt.month.mode()[0]
    print('The most common month is :', months[common_month - 1])
    print()
    # TO DO: display the most common day of week
    print('The most common day of week is :', df['Start Time'].dt.weekday_name.mode()[0])
    print()

    # TO DO: display the most common start hour
    print('The most common start hour is :', df['Start Time'].dt.hour.mode()[0])
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is :', df['Start Station'].mode()[0])
    print('\n')
    # TO DO: display most commonly used end station
    print('The most commonly used end station is :', df['End Station'].mode()[0])
    print('\n')
    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip is : \n', (df['Start Station']+' , '+df['End Station']).mode()[0])
    print('\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    print('The total travel time is :', sum(df['Trip Duration']), ' seconds')
    print('\n')
    # TO DO: display mean travel time
    print('The mean travel time is :', df['Trip Duration'].mean(), ' seconds')
    print('\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    try:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        print('The counts of user types are :\n', df['User Type'].value_counts())
        print('\n')
        # TO DO: Display counts of gender

        print('The counts of gender are :\n', df['Gender'].value_counts())
        print('\n')
        # TO DO: Display earliest, most recent, and most common year of birth
        print('The earliest year of birth is : ', df['Birth Year'].min())
        print('The most recent year of birth is : ', df['Birth Year'].max())
        print('The most common year of birth is : ', df['Birth Year'].mode()[0])
    except KeyError:
        pass
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(file):
    asking = input("Would you like to see raw data? yes or no? :")
    asking = asking.lower()
    while asking not in ['yes', 'no']:
        asking = input("yes or no?")
        asking = asking.lower()
    x = 0
    while asking == "yes" :
        if x+5 > file.shape[0]:
            print('No data anymore!')
            break
        print(file.iloc[x : x+5, :])
        asking = input("More data? yes or no?")
        asking = asking.lower()
        x += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
