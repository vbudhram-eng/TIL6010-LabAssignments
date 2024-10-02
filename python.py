import pandas as pd

# Define the file path
file_path = 'C:/Users/MSI/Desktop/downloaded files from uni/Year 4/Q1/TIL6022 TIL Python Programming/New folder/Dataset_Passenger_data.xlsx'
file_path_2 = 'C:/Users/MSI/Desktop/downloaded files from uni/Year 4/somehting.x'


# Read the CSV file
df = pd.read_excel(file_path)
print(df.head())