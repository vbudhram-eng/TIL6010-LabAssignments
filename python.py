import pandas as pd

# Define the file path
file_path = 'C:/Users/MSI/Desktop/downloaded files from uni/Year 4/Q1/TIL6022 TIL Python Programming/New folder/dataset_full.csv'

# Read the CSV file
df_raw = pd.read_csv(file_path, delimiter=";")


def preprocessing(df):

    #Filter data, so that we weork only with Passengers and only for years above 2015 and not during 2020
    df = df.iloc[:, :43]
    df = df[ (df['Periods'].str[:4].astype(int) >= 2015) & (df['Periods'].str[:4].astype(int) != 2020)] #add only dates post 2015

    # Function to extract year, month, and quarter from the Periods column
    def extract_date(period):
        year = period[:4]  # Extract the year
        if 'MM' in period:
            month = str(period[6:])  # Extract month number for MM format
            return year, month, None  # No quarter in MM format
        elif 'KW' in period:
            quarter = str(period[6:])  # Extract quarter number for KW format
            return year, None, quarter  # No month in KW format
        return year, None, None  # Fallback if format is unrecognized

    # Create new columns for Year, Month, and Quarter
    df[['Year', 'Month_Num', 'Quarter_Num']] = df['Periods'].apply(extract_date).apply(pd.Series)

    # Map numeric month to month names
    month_names = {
        '01': 'January', '02': 'February', '03': 'March', '04': 'April', 
        '05': 'May', '06': 'June', '07': 'July', '08': 'August', 
        '09': 'September', '10': 'October', '11': 'November', '12': 'December'
    }

    # Map numeric quarters to quarter names
    quarter_names = {
        '01': 'Q1', '02': 'Q2', '03': 'Q3', '04': 'Q4'
    }

    airport_names = {
        'A043590':'Amsterdam Schiphol', 'A043596':'Rotterdam','A043591':'Eindhoven'
    }

    # Further Filtering of the data

    df['Month'] = df['Month_Num'].map(month_names)
    df['Quarter'] = df['Quarter_Num'].map(quarter_names)
    df['Airport'] = df['Airports'].map(airport_names)
    df['Month'] = df['Month'].fillna(df['Quarter'])             #For the KW part, replace it with the appropriate Quarter 
    df['Month'] = df['Month'].fillna(df['Year'])                #For the JJ part, replace it with the appropriate year  
    df = df.drop('Quarter', axis=1)         #remove the unneeded part 

    # Drop the Month_Num and Quarter_Num columns if you don't need them
    df.drop(columns=['Month_Num', 'Quarter_Num'], inplace=True)
    df.drop(columns=['Airports'], inplace=True)

    return df

df_processesd = preprocessing(df_raw)

# Display the updated DataFrame
print(df_processesd.head(20))
print(df_processesd.count())