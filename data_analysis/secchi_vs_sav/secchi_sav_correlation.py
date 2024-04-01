#                                       # 
#   SECCHI / SAV CORRELATION ANALYSIS   # 
#                                       # 

# This function creates a 'Pearson correlation coefficient matrix' for Secchi (m) vs SAV volume (HV). The analysis has a 10-week delay, accounting for the biology of HV and the delays in growth. The correlation is displayed in a heatmap figure. 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def secchi_sav_correlation():
    # Secchi + SAV data
    opc_data = pd.read_csv('./data/SAV/opc_data.csv')
    
    # Convert 'Secchi (m)' and 'HV' to numeric
    opc_data['Secchi (m)'] = pd.to_numeric(opc_data['Secchi (m)'], errors='coerce')
    opc_data['HV'] = pd.to_numeric(opc_data['HV'], errors='coerce')

    # Calculate correlation matrix 
    # .corr is pandas default Pearson correlation coefficient function
    correlation_result = opc_data[['Secchi (m)', 'HV']].corr() 

    # Plot 'Pearson Correlation Matrix'
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_result, annot=True, 
                fmt=".2f", 
                cmap='coolwarm', 
                cbar=True, 
                square=True)
    plt.title("Correlation Matrix")
    plt.tight_layout()
    
     # Save Plot Locally
    plot = './resources/sav_vs_secchi/secchi_sav_correlation_plot.png'
    plt.savefig(plot)

    # Show Plot
    plt.show()

# Uncomment below code to run
secchi_sav_correlation()