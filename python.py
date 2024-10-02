import pandas as pd

# Define the file path
file_path = 'C:/Users/MSI/Desktop/downloaded files from uni/Year 4/Q1/TIL6022 TIL Python Programming/New folder/dataset_full.csv'

# Read the CSV file
df = pd.read_csv(file_path, delimiter=";")
print(df.head(40))

# Function to extract year, month, and quarter from the Periods column
def extract_date(period):
    year = period[:4]  # Extract the year
    if 'MM' in period:
        month = int(period[7:])  # Extract month number for MM format
        return year, month, None  # No quarter in MM format
    elif 'KW' in period:
        quarter = int(period[7:])  # Extract quarter number for KW format
        return year, None, quarter  # No month in KW format
    return year, None, None  # Fallback if format is unrecognized

# Create new columns for Year, Month, and Quarter
df[['Year', 'Month_Num', 'Quarter_Num']] = df['Periods'].apply(extract_date).apply(pd.Series)

# Map numeric month to month names
month_names = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April', 
    5: 'May', 6: 'June', 7: 'July', 8: 'August', 
    9: 'September', 10: 'October', 11: 'November', 12: 'December'
}

# Map numeric quarters to quarter names
quarter_names = {
    1: 'Q1', 2: 'Q2', 3: 'Q3', 4: 'Q4'
}

# Add new columns for Month names and Quarter names
df['Month'] = df['Month_Num'].map(month_names)
df['Quarter'] = df['Quarter_Num'].map(quarter_names)

# Drop the Month_Num and Quarter_Num columns if you don't need them
df.drop(columns=['Month_Num', 'Quarter_Num'], inplace=True)

# Display the updated DataFrame
print(df)


# Display the updated DataFrame
print(df.head(20))