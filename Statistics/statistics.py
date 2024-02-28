#                # 
#   STATISTICS   # 
#                #

from pandasgui import show  # This package is amazing!! 
import pandas as pd

# DATA CLEANING #

# Load dataset(s)
cbmocnut = pd.read_csv('./Otter Point Creek Nutrient Data/cbmocnut.csv')

# Drop all columns except columns of interest 
nutrient_data = cbmocnut[['StationCode', 'DateTimeStamp', 'PO4F', 'NH4F', 'NO2F', 'NO3F']]

# Drop rows with 'NaN' values in columns of interest
clean_data = nutrient_data.dropna(subset=['PO4F', 'NH4F', 'NO2F', 'NO3F'])

# Check for random rows + Make sure that data cleaning was successful
clean_sample = clean_data.sample(15)
show(clean_sample)

# If running in MacOS, inout below code into bash to temporarily utilize pandasgui (MacOS bug) 
# export APPDATA=/tmp


#   STATISTICS   # 

# Perform ANOVA? 
# Want to see if there is any relationship in the variance of PO4F, NH4F, 'NO2F, and NO3F
# Want to know if spikes in these metrics are temporally related (do they happen at the same time)
# Want to use this information to reverse engineer the source based on 
