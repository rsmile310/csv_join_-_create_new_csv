import pandas as pd

# Read the CSV files
katana_df = pd.read_excel('katana.xlsx')
mrpeasy_df = pd.read_csv('mrpeasy.csv')

# Merge the two DataFrames based on 'Part No.' and 'Variant code'
merged_data = pd.merge(mrpeasy_df, katana_df, left_on='Part No.', right_on='Variant code', how='left')

# Select only the required columns
selected_data = merged_data[['Part No.', 'Default purchase price', 'Default supplier']]

# Drop duplicate rows
selected_data = selected_data.drop_duplicates()

# Save the selected data to a new CSV file
selected_data.to_csv('selected_data.csv', index=False)
