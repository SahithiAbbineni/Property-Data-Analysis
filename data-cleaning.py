import pandas as pd
import ast  # To parse corrupted JSON-like strings

# Load the combined data (after merging CSVs)
final_data = pd.read_csv('combined_property_data.csv')

# Function to extract photo count from the corrupted `photo_urls`
def extract_photo_count(url_column):
    try:
        urls = ast.literal_eval(url_column)
        return len(urls) if isinstance(urls, list) else 0
    except:
        return 0

# Clean and create a new column for photo_count
final_data['photo_count'] = final_data['photo_urls'].apply(extract_photo_count)

# Handle missing values by filling with a default value or removing them
final_data.fillna({'property_size': final_data['property_size'].mean(), 'rent': final_data['rent'].median()}, inplace=True)

# Optionally remove rows with missing critical values
final_data.dropna(subset=['property_id'], inplace=True)

# Save the cleaned data
final_data.to_csv('cleaned_property_data.csv', index=False)
