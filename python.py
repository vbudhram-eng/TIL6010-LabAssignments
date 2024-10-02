import pandas as pd

# Define the file path
file_path = 'C:/Users/MSI/Desktop/downloaded files from uni/Year 4/Q1/TIL6022 TIL Python Programming/New folder/dataset_full.csv'

# Read the CSV file
df = pd.read_csv(file_path, delimiter=";")
print(df.head())