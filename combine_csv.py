import pandas as pd
import glob

# Use glob to get a list of all CSV files in a folder
path = r'/Users/bgmarketing/Desktop/dev/real_estate/combine_csv/feb_23'
all_files = glob.glob(path + "/*.csv")

# Combine all CSV files into one DataFrame
df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

# Write the combined DataFrame to a new CSV file
df.to_csv("combined.csv", index=False)

