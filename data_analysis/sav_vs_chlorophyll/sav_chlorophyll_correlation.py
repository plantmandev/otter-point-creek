#                                               # 
#   SAV / CHLOROPHYLL A CORRELEATION ANALYSIS   # 
#                                               # 

# The following functions are 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def sav_chlorophyll_correlation(cbmocnut_path, opc_data_path):
     # Load the datasets
    cbmocnut_df = pd.read_csv(cbmocnut_path)
    opc_data_df = pd.read_csv(opc_data_path)

    # Prepare the data for merging
    cbmocnut_df['DateTimeStamp'] = pd.to_datetime(cbmocnut_df['DateTimeStamp'])
    cbmocnut_df['Date'] = cbmocnut_df['DateTimeStamp'].dt.date
    opc_data_df['Date'] = pd.to_datetime(opc_data_df['Date'])

    # Ensure both 'Date' columns are of the same type
    cbmocnut_df['Date'] = pd.to_datetime(cbmocnut_df['Date'])
    
    # Merge the datasets based on the date
    merged_df = pd.merge(opc_data_df, cbmocnut_df[['Date', 'CHLA_N']], on = 'Date', how = 'inner')

    # Clean the data
    merged_df['HV'] = pd.to_numeric(merged_df['HV'], errors = 'coerce')
    merged_df.dropna(subset = ['HV', 'CHLA_N'], inplace = True)

    # Pearson correlation coefficient
    correlation_result = merged_df[['HV', 'CHLA_N']].corr(method='pearson')
    print("Pearson Correlation Coefficient:")
    print(correlation_result)

def sav_chlorophyll_scatterplot(cbmocnut_path, opc_data_path):
    # Load the datasets
    cbmocnut_df = pd.read_csv(cbmocnut_path)
    opc_data_df = pd.read_csv(opc_data_path)

    # Prepare the data for merging
    cbmocnut_df['DateTimeStamp'] = pd.to_datetime(cbmocnut_df['DateTimeStamp'])
    cbmocnut_df['Date'] = cbmocnut_df['DateTimeStamp'].dt.date
    opc_data_df['Date'] = pd.to_datetime(opc_data_df['Date'])

    # Ensure both 'Date' columns are of the same type
    cbmocnut_df['Date'] = pd.to_datetime(cbmocnut_df['Date'])
    
    # Merge the datasets based on the date
    merged_df = pd.merge(opc_data_df, cbmocnut_df[['Date', 'CHLA_N']], on='Date', how='inner')

    # Clean the data
    merged_df['HV'] = pd.to_numeric(merged_df['HV'], errors='coerce')
    merged_df.dropna(subset=['HV', 'CHLA_N'], inplace=True)

    # Visualization: Scatter Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data = merged_df,
                    x='HV', 
                    y='CHLA_N')
    plt.title('Scatter Plot of HV vs CHLA_N')
    plt.xlabel('Hydrilla verticillata (HV)')
    plt.ylabel('Chlorophyll A (CHLA_N)')
    plt.show()

def sav_chlorophyll_time_series(cbmocnut_path, opc_data_path): 
    # Load the datasets
    cbmocnut_df = pd.read_csv(cbmocnut_path)
    opc_data_df = pd.read_csv(opc_data_path)

    # Prepare the data for merging
    cbmocnut_df['DateTimeStamp'] = pd.to_datetime(cbmocnut_df['DateTimeStamp'])
    cbmocnut_df['Date'] = cbmocnut_df['DateTimeStamp'].dt.date
    opc_data_df['Date'] = pd.to_datetime(opc_data_df['Date'])

    # Ensure both 'Date' columns are of the same type
    cbmocnut_df['Date'] = pd.to_datetime(cbmocnut_df['Date'])
    
    # Merge the datasets based on the date
    merged_df = pd.merge(opc_data_df, cbmocnut_df[['Date', 'CHLA_N']], on='Date', how='inner')

    # Clean the data
    merged_df['HV'] = pd.to_numeric(merged_df['HV'], errors = 'coerce')
    merged_df.dropna(subset = ['HV', 'CHLA_N'], inplace = True)

    # Visualization: Time Series Plot
    time_series_data = merged_df.groupby('Date').agg({'HV': 'mean', 'CHLA_N': 'mean'}).reset_index()
    plt.figure(figsize = (14, 7))
    plt.plot(time_series_data['Date'], time_series_data['HV'], label = 'HV')
    plt.plot(time_series_data['Date'], time_series_data['CHLA_N'], label = 'Chlorophyll-A', color = 'r')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Time Series of HV and Chlorophyll-A Over Time')
    plt.legend()
    plt.show()

# Uncomment below code to run 
cmmocnut_path = './data/cbmocnut/cbmocnut.csv'
opc_data_path = './data/SAV/opc_data.csv'

sav_chlorophyll_correlation(cmmocnut_path, opc_data_path)
sav_chlorophyll_scatterplot(cmmocnut_path, opc_data_path)
sav_chlorophyll_time_series(cmmocnut_path, opc_data_path)
