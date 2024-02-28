import pandas as pd

# Define Path of CSVs to be Merged (2003-2024)
file_paths = [
    './Otter Point Creek Nutrient Data/cbmocnut2003.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2004.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2005.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2006.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2007.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2008.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2009.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2010.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2011.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2012.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2013.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2014.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2015.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2016.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2017.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2018.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2019.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2020.csv',
    './Otter Point Creek Nutrient Data/cbmocnut2021.csv', 
    './Otter Point Creek Nutrient Data/cbmocnut2022.csv'
]

# Define File Path + Name for Output File 
output_file = './Otter Point Creek Nutrient Data/cbmocnut2017-2022.csv'

# Define Merger Function
def merge_csv_files(file_paths, output_file):

    # Data Frame Temporarily Holds Files 
    dataframes = []

    # Each File Listed in 'file_paths' is Read + Added to 'dataframe' as Temporary Placeholder
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        dataframes.append(df)

    # Concadentate All Dataframes
    merged_df = pd.concat(dataframes, ignore_index=True)

    # Save Final Dataframe into CSV File
    merged_df.to_csv(output_file, index=False)

    return output_file

# Run 'merge_csv_files' Script (Merging 2003-2024 Nutrient Data)
merge_csv_files(file_paths, output_file)
