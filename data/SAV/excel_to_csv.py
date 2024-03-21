#                  # 
#   EXCEL TO CSV   # 
#                  # 

# This script is used to transformed sheets from cleaned SAV data (excel) from NERRs into individual csv files used in analysis. 

import pandas as pd
import os

def excel_to_csv(excel_file, directory):
    # Load excel file using file path
    excel = pd.ExcelFile(excel_file)

    # Iterate through all sheets in file 
    for sheet_name in excel.sheet_names:
        # Temporarily copy sheet contents into pandas data frame
        df = excel.parse(sheet_name)

        # Create new csv 
        csv = f"{sheet_name}.csv"

        # Save in correct directory
        path = os.path.join(directory, csv)

        # Inject data frame contents into csv
        df.to_csv(path, index = False)


# Uncomment below code to run
directory = "./SAV/csv_files"
excel_file = './SAV/sav_data.xlsx'
excel_to_csv(excel_file, directory)