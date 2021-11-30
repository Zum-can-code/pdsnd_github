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

    city = ''

    while city != 'chicago' and city != 'washington' and city!= 'new york city':
        city = input("Which city would you like to explore: chicago, new york city or washington? ").lower()
        if city == 'chicago' or city == 'washington' or city == 'new york city':
            print('Your Selected city: ', city)
        else:
            print("Invalid city: please double check your input (valid inputs - chicago, new york city or washington")

    # TO DO: get user input for month (all, january, february, ... , june)

    month = ''

    while month != 'All' and month != 'Jan' and month != 'Feb' and month != 'Mar' and month != 'Apr' and month != 'May' and month != 'Jun':
        month = input("Which month are you interested in? All, Jan, Feb, Mar, Apr, May, Jun? ").title()
        if month == 'All' or month == 'Jan' or month == 'Feb' or month == 'Mar' or month == 'Apr' or month == 'May' or month == 'Jun':
            print('Your Selected month: ', month)
        else:
            print("Invalid month: please double check your input (valid inputs - All, Jan, Feb, Mar, Apr, May, Jun")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = ''

    while day != 'All' and day != 'Monday' and day != 'Tuesday' and day != 'Wednesday' and day != 'Thursday' and day != 'Friday' and day != 'Saturday' and day != 'Sunday':
        day = input("Which day are you interested in? All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday? ").title()
        if day == 'All' or day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday' or day == 'Sunday':
            print('Your Selected day: ', day)
        else:
            print("Invalid day: please double check your input (valid inputs - All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday")


    print('-'*40)
    return city, month, day

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

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
    df['start_hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    time.sleep(3)

    # TO DO: display the most common month
    mode_month = df['month'].mode().iloc[0]
    print('    Most popular month (as number): {}'.format(mode_month))
    time.sleep(1)

    # TO DO: display the most common day of week
    mode_day = df['day_of_week'].mode().iloc[0]
    print('    The most popular day: {}'.format(mode_day))
    time.sleep(1)

    #TO DO: display the most common start hour
    mode_hour = df['start_hour'].mode().iloc[0]
    print('    The most popular start hour: {}'.format(mode_hour))
    time.sleep(1)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    time.sleep(1)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    time.sleep(3)

    #TO DO: display most commonly used start station
    mode_sstation = df['Start Station'].mode().iloc[0]
    print('    Most commonly used start station: {}'.format(mode_sstation))
    time.sleep(1)

    # TO DO: display most commonly used end station
    mode_estation = df['End Station'].mode().iloc[0]
    print('    Most commonly used end station: {}'.format(mode_estation))
    time.sleep(1)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip combination'] = df['Start Station'] + ' TO ' + df['End Station']
    mode_combo = df['trip combination'].mode().iloc[0]
    print('    The most frequent combination of start and end station was: {}'.format(mode_combo))
    time.sleep(1)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    time.sleep(1)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    time.sleep(3)

    # TO DO: display total travel time
    total_tt_sec = df['Trip Duration'].sum()
    total_tt_hours = total_tt_sec/3600
    print('    The total travel time was (in seconds): {}'.format(total_tt_sec))
    time.sleep(1)
    print('    The total travel time was (in hours): {}'.format(total_tt_hours))
    time.sleep(1)

    # TO DO: display mean travel time
    mean_tt_sec = df['Trip Duration'].mean()
    mean_tt_hours = mean_tt_sec/360
    print('    The average travel time was (in seconds): {}'.format(mean_tt_sec))
    time.sleep(1)
    print('    The average travel time was (in hours): {}'.format(mean_tt_hours))
    time.sleep(1)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    time.sleep(1)

 #---------------------------------------------------------------------------------------------------------------------------------------------------------------

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    time.sleep(3)

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('    Number of users per user type: \n{}\n'.format(user_type_count))
    time.sleep(1)

    #TO DO: Display counts of gender
    print('    Number of male and female users:')
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('\n{}\n'.format(gender_count))
    else:
        print('Gender data not available in dataframe\n')

    time.sleep(1)

    #TO DO: Display earliest, most recent, and most common year of birth
    print('    user age data:\n')
    if 'Birth Year' in df:
        min_birth = int(df['Birth Year'].min())
        max_birth = int(df['Birth Year'].max())
        mode_birth = int(df['Birth Year'].mode().iloc[0])
        print('    Birth year of oldest user: {}'.format(min_birth))
        time.sleep(1)
        print('    Birth year of youngest user: {}'.format(max_birth))
        time.sleep(1)
        print('    Most common year of birth: {}'.format(mode_birth))
        time.sleep(1)
    else:
        print('Birth Year data not available in dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    time.sleep(1)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

def display_data(df):
    """
    asks the user if they would like to see the first five rows of individual data, continues to ask until the user says 'no'

    """

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? ").lower()
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[(start_loc):(start_loc + 5)])
        start_loc += 5
        view_display = input("Do you wish to see 5 more rows of individual data?: ").lower()
        if view_display == 'no':
            break


#---------------------------------------------------------------------------------------------------------------------------------------------------------------

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

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
