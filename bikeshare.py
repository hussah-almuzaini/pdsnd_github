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
    
    city =''
    while ( city !='chicago' and city !='new york city' and city != 'washington'):
        print("enter city")
        city = (input()).lower()
        


    # TO DO: get user input for month (all, january, february, ... , june)
    print("enter month")
    month = input().lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print("enter day")

    day = input().lower()

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    print('Most common month: ', common_month)


    # TO DO: display the most common day of week
    day_of_week = df['day_of_week'].mode()[0]

    print('Most common day of week: ', day_of_week)

    # TO DO: display the most common start hour
    Start_Time = df['Start Time'].mode()[0]

    print('Most common Start Time : ', Start_Time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Time = df['Start Time'].mode()[0]

    print('Most common Start Time: ', Start_Time)

    # TO DO: display most commonly used end station
    End_Time = df['End Time'].mode()[0]
    print('Most common End Time: ', End_Time)

    # TO DO: display most frequent combination of start station and end sta
    print('Most common End Time: ', End_Time)

    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time-------------
    total_travel_time = df['Trip Duration'].sum()

    print("total travel time: ",total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time=df["Trip Duration"].mean()
    print("mean travel time : ",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print("counts of user types", user_types)


    # TO DO: Display counts of gender
    try:
        
        Gender = df['Gender'].value_counts()

        print("counts of gender",Gender)
    except:
        print("no gender coulmn ")
        

    # TO DO: Display earliest, most recent, and most common year of birth ------------------
    try:
        earliest = df['Birth Year'].min()
        print("earliest Birth Year ",earliest)
        
        recent = df['Birth Year'].max()
        print("earliest Birth Year ",recent)
        
        common_year = df['Birth Year'].mode()[0]
        print("common Birth Year ",common_year)
    except:
        print("no birth coulmn ")
        
        
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def view_data(df) :
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
