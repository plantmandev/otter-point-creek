#                                              # 
#   SAV / CHLOROPHYLL-A CORRELATION ANALYSIS   # 
#                                              # 

# The following function uses Chlorophyll-A and SAV (HV) data from 2007-2017 to perform an partial autocorrelation analysis in order to determine the peak lag period in terms of correlation between SAV data and Chlorophyll-a data. There is also a function performing a pearson correlation coefficient analysis. Additionally, a cross-correlation analysis was performed to understand how time lags might have an influence in the change of SAVs over time. This function allows us to understand the correlation between Chlorophyll A concentrations in the OPC and SAV volume (HV) observed in surveys. Additionally, a time series analysis with a linear regression between Chlorophyll A concentration and SAV (HV) volume in order further confirm if the relationship observed is consistent across analyses. The information obtained from these analyses will help us understand if higher Chlorophyll A concentrations have negative effects on SAV volume. This is important information as it will help predict if the influx of nutrients that will added to the stream post-dam removal (through the dissolution of nutrients in sediment stored behind the dam) that is expected to increase algae volume (measured as Chlorophyll A) will negatively impact SAV volume. 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statsmodels.tsa.stattools as smt
from statsmodels.graphics.tsaplots import plot_pacf

# This function generates a partial autocorrelation analysis for SAV and Chlorophyll-A data. Additionally, this function generates a figure for the partial autocorrelation analysis being performed. 
def chlorophyll_sav_pacf_figure(cbmocnut_data_path, opc_data_path): 
    # Load the datasets
    cbmocnut_data = pd.read_csv(cbmocnut_data_path)
    opc_data = pd.read_csv(opc_data_path)

    # Preprocess OPC Data
    opc_data['Date'] = pd.to_datetime(opc_data['Date'])
    opc_data_filtered = opc_data[['Date', 'HV']].dropna()

    # Preprocess CBMOCNUT Data
    cbmocnut_data['DateTimeStamp'] = pd.to_datetime(cbmocnut_data['DateTimeStamp'], format = '%m/%d/%Y %H:%M')
    cbmocnut_data['Date'] = cbmocnut_data['DateTimeStamp'].dt.date
    cbmocnut_data_filtered = cbmocnut_data[['Date', 'CHLA_N']].dropna()
    cbmocnut_data_filtered['Date'] = pd.to_datetime(cbmocnut_data_filtered['Date'])

    # Merge the datasets on date
    merged_data = pd.merge(opc_data_filtered, cbmocnut_data_filtered, on = 'Date', how = 'inner')

    # Set figure size 
    plt.figure(figsize = (12, 6))

    # Plot Chlorophyll A
    plt.plot(merged_data['Date'], 
             merged_data['CHLA_N'], 
             label = 'Chlorophyll A', 
             color='green')

    # Plot HV
    plt.scatter(merged_data['Date'], 
                merged_data['HV'], 
                label = 'HV', 
                color = 'blue', 
                s = 10)  # s is the marker size

    plt.title('Chlorophyll A and HV Over Time')
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.legend()
    plt.show()

    # Plotting PACF for Chlorophyll A
    fig, ax = plt.subplots(figsize=(10, 6))
    plot_pacf(merged_data['CHLA_N'], ax=ax, lags=40, method='ywm')

    plt.title('Partial Autocorrelation Function for Chlorophyll A')
    plt.xlabel('Lag')
    plt.ylabel('PACF')

     # Save Plot Locally
    plot = './resources/sav_vs_chlorophyll/pacf'
    plt.savefig(plot)

    # Show Plot 
    plt.show()

# This function uses Chlorophyll A and SAV volume (HV) from 2007-2017 to perform a pearson correlation coefficient and a cross-correlation function analysis. This correlation analysis allows us to understand the relationship between Chlorophyll-A concentration and SAV (HV) volume over time observed in OPC surveys.  
def chlorophyll_sav_correlation(cbmocnut_path, opc_data_path):
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

    # Clean data
    merged_df['HV'] = pd.to_numeric(merged_df['HV'], errors = 'coerce')
    opc_data_df['Date'] = pd.to_datetime(opc_data_df['Date'], errors='coerce')
    merged_df.dropna(subset = ['HV', 'CHLA_N'], inplace = True)

    # Pearson correlation coefficient analysis
    pearson = merged_df[['HV', 'CHLA_N']].corr()

    # Cross-correlation analysis
    cross_correlation = smt.ccf(merged_df['HV'], merged_df['CHLA_N'], adjusted = False)

    return pearson, cross_correlation

# This function generates a figure for the cross-correlation analysis.
def chlorophyll_sav_cross_correlation_figure(cross_correlation, max_lags):
    # Create figure and axis
    fig, ax = plt.subplots(figsize = (10, 5))
    
    # Plot the cross-correlation values
    lags = range(-max_lags, max_lags + 1)
    ax.stem(lags, cross_correlation, use_line_collection = True)
    
    # Highlight the zero line for reference
    ax.axhline(0, color = 'black', linewidth = 0.8, linestyle = '--')
    
    # Labeling
    ax.set_title('Cross-Correlation Function')
    ax.set_xlabel('Lags')
    ax.set_ylabel('Correlation Coefficient')
    
    # Adding grid for easier visualization
    ax.grid(True)
    
    # Save Plot Locally
    plot = './resources/chlorophyll_cross_correlation/chlorophyll_sav_cross_correlation_figure.png'
    plt.savefig(plot)

    # Show the plot
    plt.show()

# --------------------------------------------------------------------------------------
#                                         VARIABLES                                   
cmmocnut_path = './data/cbmocnut/cbmocnut.csv'
opc_data_path = './data/SAV/opc_data.csv'

pearson, cross_correlation = chlorophyll_sav_correlation(cmmocnut_path, opc_data_path)
max_lags = 1 # This uses the partial autocorrelation analysis results 

# ---------------------------------------------------------------------------------------

# Uncomment below code to run 
chlorophyll_sav_correlation(cmmocnut_path, opc_data_path) # Runs pearson + cross-correlation 
chlorophyll_sav_cross_correlation_figure(cross_correlation, max_lags) # Generates pearson correlation coefficient figure 
# chlorophyll_sav_cross_correlation_figure(cross_correlation, max_lags)(cross_correlation, max_lags) # Generates cross-correlation analysis figure
# chlorophyll_sav_pacf_figure(cmmocnut_path, opc_data_path) # Generates PACF figure