#
#
#

#

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_pacf

def chlorophyll_sav_pacf(): 
    # Load the datasets
    cbmocnut_data = pd.read_csv('./data/cbmocnut/cbmocnut.csv')
    opc_data = pd.read_csv('./data/SAV/opc_data.csv')

    # Preprocess OPC Data
    opc_data['Date'] = pd.to_datetime(opc_data['Date'])
    opc_data_filtered = opc_data[['Date', 'HV']].dropna()

    # Preprocess CBMOCNUT Data
    cbmocnut_data['DateTimeStamp'] = pd.to_datetime(cbmocnut_data['DateTimeStamp'], format='%m/%d/%Y %H:%M')
    cbmocnut_data['Date'] = cbmocnut_data['DateTimeStamp'].dt.date
    cbmocnut_data_filtered = cbmocnut_data[['Date', 'CHLA_N']].dropna()
    cbmocnut_data_filtered['Date'] = pd.to_datetime(cbmocnut_data_filtered['Date'])

    # Merge the datasets on date
    merged_data = pd.merge(opc_data_filtered, cbmocnut_data_filtered, on='Date', how='inner')

    plt.figure(figsize=(12, 6))

    # Plot Chlorophyll A
    plt.plot(merged_data['Date'], merged_data['CHLA_N'], label='Chlorophyll A', color='green')

    # Plot HV
    plt.scatter(merged_data['Date'], merged_data['HV'], label='HV', color='blue', s=10)  # s is the marker size

    plt.title('Chlorophyll A and HV Over Time')
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.legend()
    plt.show()

    # Plotting PACF for Chlorophyll A
    fig, ax = plt.subplots(figsize=(10, 6))
    plot_pacf(merged_data['CHLA_N'], ax=ax, lags=40, method='ywm')

    plt.title('Partial Autocorrelation Function for Chlorophyll A (CHLA_N)')
    plt.xlabel('Lag')
    plt.ylabel('PACF')
    plt.show()

chlorophyll_sav_pacf()