import pandas as pd

"""
YOU WILL HAVE TO CHANGE THE FILE PATH TO WORK ON THE FILE SO ON EACH COMPUTER, AS THIS IS TO FOR MY COMPUTER.

"""


# Define the file path
file_path = 'C:/Users/MSI/Desktop/downloaded files from uni/Year 4/Q1/TIL6022 TIL Python Programming/New folder/dataset_full.csv'

# Read the CSV file
df_raw = pd.read_csv(file_path, delimiter=";")

"""
Leaving some information for the rest of the project:
The data is structured so that:

Technically you can use the Periods with their code as key: 2015MM01 and 
use the Month/Year columns for the output parts and visualisation. on the X-axis for example. 

another thing for the data
    -> Each quarter already has sum over the values for the months during the quarter 
        -> i.e Q1 values = Sum(Januar,feb,March)
    -> same goes for the years, as they have summed over the quarters or months (which gives the same results)

if you want to do some quarterly values

On the other hand, you have for example:
    -> Total passengers = sheduled + Non_sheduled
        -> As well as Total passengers = Arriving + Departuring 
    -> Asia = West_Asia + East_asia + North_Asia + South_Asia

So you have a lot of breakdown and you can simply pick the columns you want to compare. 

NEWS = North + East + West + South (funny fact newspaper can be interpreted as north/east/west/south/past/and/present/event report )

For europe you only have EU and Non-Eu countries data. Why noth broken into regions idk. 
(Let's just say Europe is one big family in small island in the report, just how we can treat US as a whole)
"""

def preprocessing(df):

    #Filter data, so that we work only with Passengers and only for years above 2015(excluding) 2020
    df = df.iloc[:, :43]
    df = df[ (df['Periods'].str[:4].astype(int) >= 2015) & (df['Periods'].str[:4].astype(int) != 2020)] #add only dates post 2015

    # Function to extract year, month, and quarter from the Periods column
    def extract_date(period):
        #the function returns year, Month, Quarter and since we 
        #have eiither Month or Quarter, the missing one is set as None

        year = period[:4]               # Extract the year
        if 'MM' in period:
            month = str(period[6:])     # Extract month number for MM format
            return year, month, None    
        elif 'KW' in period:
            quarter = str(period[6:])   # Extract quarter number for KW format
            return year, None, quarter  
        return year, None, None  

    # Create new columns for Year, Month, and Quarter
    df[['Year', 'Month_Num', 'Quarter_Num']] = df['Periods'].apply(extract_date).apply(pd.Series)

    # Map months to month names
    month_names = {
        '01': 'January', '02': 'February', '03': 'March', '04': 'April', 
        '05': 'May', '06': 'June', '07': 'July', '08': 'August', 
        '09': 'September', '10': 'October', '11': 'November', '12': 'December'
    }

    # Map quarters to quarter names
    quarter_names = {
        '01': 'Q1', '02': 'Q2', '03': 'Q3', '04': 'Q4'
    }

    #Map airports to their airport quarter  
    airport_names = {
        'A043590':'Amsterdam Schiphol', 'A043596':'Rotterdam','A043591':'Eindhoven'
    }

    # Further data processing 
    df['Month'] = df['Month_Num'].map(month_names)
    df['Quarter'] = df['Quarter_Num'].map(quarter_names)
    df['Airport'] = df['Airports'].map(airport_names)

    # fill in the missing data in the column "month" with the Quarter or year 
    df['Month'] = df['Month'].fillna(df['Quarter'])             
    df['Month'] = df['Month'].fillna(df['Year']) 

    df = df.drop('Quarter', axis=1)         #Quarter is no longer needed 
    # Drop the Month_Num and Quarter_Num columns as they are not needed anymore 
    df.drop(columns=['Month_Num', 'Quarter_Num'], inplace=True)
    df.drop(columns=['Airports'], inplace=True)

    # List of columns to move and the column after which to insert them
    cols_to_move = ['Month', 'Year', 'Airport']
    insert_after = 'Periods'

    # Get the current columns and find the index of 'Period'
    cols = list(df.columns)
    insert_at = cols.index(insert_after) + 1

    # Remove the columns to move from their original positions
    for col in cols_to_move:
        cols.remove(col)

    # Insert the columns after 'Period'
    for i, col in enumerate(cols_to_move):
        cols.insert(insert_at + i, col)

    # Reorder the DataFrame
    df = df[cols]

    return df

df_processesd = preprocessing(df_raw)

# Display the updated DataFrame
print(df_processesd.head(20))
print(df_processesd.count())