#                                       # 
#   SECCHI / SAV CORRELATION ANALYSIS   # 
#                                       # 

# This function creates a 'Pearson correlation coefficient matrix' for Secchi (m) vs SAV volume (HV). The analysis has a 10-week delay, accounting for the biology of HV and the delays in growth. The correlation is displayed in a heatmap figure. 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# This function creates a partial autocorrelation 
def secchi_sav_pacf_figure(opc_data_path): 
    # Load data
    opc_data = pd.read_csv(opc_data_path)

    # Clean data
    opc_data['HV'] = pd.to_numeric(opc_data['HV'], errors='coerce')
    opc_data['Secchi (m)'] = pd.to_numeric(opc_data['Secchi (m)'], errors='coerce')

    # Drop empty rows
    opc_data.dropna(subset=['HV'], inplace=True)  
    opc_data.dropna(subset=['Secchi (m)'], inplace=True)

    # Plot PACF 
    fig, ax = plt.subplots(figsize=(10, 6))
    plot_pacf(opc_data['HV'], ax=ax, lags=20, method='ywm')
    plt.title('PACF for SAV')
    plt.xlabel('Lags')
    plt.ylabel('Partial Autocorrelation Value')

    # Save Plot Locally
    plot = './resources/secchi_sav_pacf/secchi_sav_pacf.png'
    plt.savefig(plot)

    # Show plot 
    plt.show()

def sav_secchi_correlation(cbmocnut_path, opc_data_path):
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
    merged_df = pd.merge(opc_data_df, cbmocnut_df[['Date', 'Secchi (m)']], on = 'Date', how = 'inner')

    # Clean data
    merged_df['HV'] = pd.to_numeric(merged_df['HV'], errors = 'coerce')
    opc_data_df['Date'] = pd.to_datetime(opc_data_df['Date'], errors='coerce')
    merged_df.dropna(subset = ['HV', 'Secchi (m)'], inplace = True)

    # Pearson correlation coefficient analysis
    pearson = merged_df[['HV', 'Secchi (m)']].corr()

    # Cross-correlation analysis
    cross_correlation = smt.ccf(merged_df['HV'], merged_df['Secchi (m)'], adjusted = False)

    return pearson, cross_correlation

# ----------------------------------------------
#                 VARIABLES 
cmmocnut_path = './data/cbmocnut/cbmocnut.csv'
opc_data_path = './data/SAV/opc_data.csv'
# ----------------------------------------------

# Uncomment below code to run
sav_secchi_correlation(cbmocnut_path, opc_data_path)
secchi_sav_pacf_figure(opc_data_path)