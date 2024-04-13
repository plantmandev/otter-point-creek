#                                              # 
#   SAV / CHLOROPHYLL A CORRELATION ANALYSIS   # 
#                                              # 

# The following function uses Chlorophyll A and SAV (HV) data from 2007-2017 to perform a 'Pearson correlation coefficient' analysis, outputting a table with the values of this correlation analysis. This function allows us to understand the correlation between Chlorophyll A concentrations in the OPC and SAV volume (HV) observed in surveys. Additionally, a time series analysis with a linear regression between Chlorophyll A concentration and SAV (HV) volume in order further confirm if the relationship observed is consistent across analyses. The information obtained from these analyses will help us understand if higher Chlorophyll A concentrations have negative effects on SAV volume. This is important information as it will help predict if the influx of nutrients that will added to the stream post-dam removal (through the dissolution of nutrients in sediment stored behind the dam) that is expected to increase algae volume (measured as Chlorophyll A) will negatively impact SAV volume. 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# This function uses Chlorophyll A and SAV volume (HV) from 2007-2017 to perform a 'Pearson correlation coefficient matrix' results as a table. This correlation analysis allows us to understand the relationship between Chlorophyll A concentration and SAV (HV) volume observed in OPC surveys.  
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

    # Clean data
    merged_df['HV'] = pd.to_numeric(merged_df['HV'], errors = 'coerce')
    opc_data_df['Date'] = pd.to_datetime(opc_data_df['Date'], errors='coerce')
    merged_df.dropna(subset = ['HV', 'CHLA_N'], inplace = True)

    # Pearson correlation coefficient
    correlation_result = merged_df[['HV', 'CHLA_N']].corr()

    # Plot and save the correlation matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_result, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Chlorophyll Correlation Matrix')
    plt.tight_layout()

    # Save Plot Locally
    plot = './resources/sav_vs_chlorophyll/chlorophyll_correlation_matrix.png'
    plt.savefig(plot)

    # Show Plot 
    plt.show()

# # Uncomment below code to run 
# cmmocnut_path = './data/cbmocnut/cbmocnut.csv'
# opc_data_path = './data/SAV/opc_data.csv'

# sav_chlorophyll_correlation(cmmocnut_path, opc_data_path)