import os
import pandas as pd

# Path where the CSV files are stored
path = 'path_to_csv_files_directory'

# List all CSV files in the directory
files = [file for file in os.listdir(path) if file.endswith('.csv')]

# Read each CSV file into a DataFrame
dataframes = [pd.read_csv(os.path.join(path, file)) for file in files]

# Concatenate all DataFrames into one
final_data = pd.concat(dataframes, ignore_index=True)

# Check the shape of the merged DataFrame
print(final_data.shape)

# Optionally save the combined data to a new CSV file
final_data.to_csv('combined_property_data.csv', index=False)

# Check for missing values or duplicates if needed
final_data.isnull().sum()  # Identify missing values
final_data.drop_duplicates(inplace=True)  # Remove duplicates if any
