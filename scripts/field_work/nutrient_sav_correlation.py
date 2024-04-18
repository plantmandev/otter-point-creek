#                                         # 
#   SAV / NUTRIENT CORRELATION ANALYSIS   # 
#                                         # 

# These functions perform correlation analysis (Pearson correlation coefficient analysis) between SAV abundance (Hydrilla verticillata) based on surveys performed by the National Estuarine Research Reserve (NERR) from 2003 to 2017. Additionally, these correlations are visualized to better showcase correlations over time. 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# This function scatter plots for HV (Hydrilla verticillata) and nutrient measurements (PO4F, NH4F, NO2F, NO3F) in OPC from 2003 - 2017. 
def dissolved_nutrient_sav_linear_regression(merged_data):
    # Formatting of plots 
    fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize = (14, 10))
    nutrients = ['PO4F', 'NH4F', 'NO2F', 'NO3F']
    
    # Iterate over nutrient type + create individual graph + merge
    for i, nutrient in enumerate(nutrients):
        ax = axes[i//2, i%2]
        sns.regplot(ax = ax,
                     data = merged_data, #
                     x = nutrient + '_numeric', # 
                     y = 'HV_numeric', #
                     scatter_kws = {'alpha':0.5}, # 
                     line_kws = {'color':'red'}) # 
        ax.set_title('SAV')
        ax.set_xlabel(f'{nutrient}')
        ax.set_ylabel(nutrient)

    plt.tight_layout()

    # Save Plot Locally
    plot = './resources/nutrient_sav_correlation.py/dissolved_nutrient_sav_linear_regression.png'
    plt.savefig(plot)

    # Show plot
    plt.show()

# This function calculates the correlation coefficients between HV (Hydrilla verticillata) and nutrient values (PO4F, NH4F, NO2F, NO3F) in Otter Point Creek, from 2002 to 2017. 
def dissolved_nutrient_sav_pearson(merged_data):
    # Convert relevant columns to numeric, coercing errors to NaN
    nutrients = ['PO4F', 'NH4F', 'NO2F', 'NO3F']
    for nutrient in nutrients:
        merged_data[nutrient + '_numeric'] = pd.to_numeric(merged_data[nutrient], errors = 'coerce')
    merged_data['HV_numeric'] = pd.to_numeric(merged_data['HV'], errors = 'coerce')
    
    # Calculate and return the correlation coefficients
    correlations = {}
    for nutrient in nutrients:
        correlations[f'HV vs {nutrient}'] = merged_data['HV_numeric'].corr(merged_data[nutrient + '_numeric'])
    
    return correlations

# ------------------------------------------------------------------------------------------------------------
#                                                 VARIABLES
merged_data = pd.read_csv('./data/SAV/cbmocnut_sav_merged.csv') # Read csv 
# ------------------------------------------------------------------------------------------------------------

# Uncomment to run code 
dissolved_nutrient_sav_linear_regression(merged_data) # Output + Save plot
dissolved_nutrient_sav_pearson(merged_data) # Run correlation 
 