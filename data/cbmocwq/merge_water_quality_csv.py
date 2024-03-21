import pandas as pd

# Define Path of CSVs to be Merged (2003-2024)
file_paths = [
    './Otter Point Creek Water Quality Data/cbmocwq2003.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2004.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2005.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2006.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2007.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2008.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2009.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2010.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2011.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2012.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2013.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2014.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2015.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2016.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2017.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2018.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2019.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2020.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2021.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2022.csv',
    './Otter Point Creek Water Quality Data/cbmocwq2023.csv'
    # './Otter Point Creek Water Quality Data/cbmocwq2024.csv' Ignored due to strange values 
]

# Define File Path + Name for Output File 
# Script was slightly changed for multi-year range files
output_file = './Otter Point Creek Water Quality Data/cbmocwq.csv'

# Define Merger Function
def merge_csv_files(file_paths, output_file):

    # Data Frame Temporarily Holds Files 
    dataframes = []

    # Each File Listed in 'file_paths' is Read + Added to 'dataframe' Remporary Placeholder
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        dataframes.append(df)

    # Concadentate All Dataframes
    merged_df = pd.concat(dataframes, ignore_index=True)

    # Save Final Dataframe into CSV File
    merged_df.to_csv(output_file, index=False)

    return output_file

# Run 'merge_csv_files' Script (Merging 2003-2024 Water Quality Data)
merge_csv_files(file_paths, output_file)
