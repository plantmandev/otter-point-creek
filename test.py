#                                         # 
#   SAV / NUTRIENT CORRELATION ANALYSIS   # 
#                                         # 

# These functions perform correlation analysis (Pearson correlation coefficient analysis) between SAV abundance (Hydrilla verticillata) based on surveys performed by the National Estuarine Research Reserve (NERR) from 2003 to 2017. Additionally, these correlations are visualized to better showcase correlations over time. 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#   PEARSON CORRELATION COEFFICIENT ANALYSIS   # 

# This function calculates the correlation coefficients between HV (Hydrilla verticillata) and nutrient values (PO4F, NH4F, NO2F, NO3F) in Otter Point Creek, from 2002 to 2017. 
def HV_nutrient_correlation(data):
    # Convert relevant columns to numeric, coercing errors to NaN
    nutrients = ['PO4F', 'NH4F', 'NO2F', 'NO3F']
    for nutrient in nutrients:
        data[nutrient + '_numeric'] = pd.to_numeric(data[nutrient], errors = 'coerce')
    data['HV_numeric'] = pd.to_numeric(data['HV'], errors = 'coerce')
    
    # Calculate and return the correlation coefficients
    correlations = {}
    for nutrient in nutrients:
        correlations[f'HV vs {nutrient}'] = data['HV_numeric'].corr(data[nutrient + '_numeric'])
    
    return correlations

#   CORRELATION VISUALIZATIONS   # 

# This function scatter plots for HV (Hydrilla verticillata) and nutrient measurements (PO4F, NH4F, NO2F, NO3F) in OPC from 2003 - 2017. 
def HV_nutrient_correlation_plot(data):
    # Formatting of plots 
    fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize = (14, 10))
    nutrients = ['PO4F', 'NH4F', 'NO2F', 'NO3F']
    
    # Iterate over nutrient type + create individual graph + merge
    for i, nutrient in enumerate(nutrients):
        ax = axes[i//2, i%2]
        sns.regplot(ax = ax,
                     data = data, #
                     x = 'HV_numeric', # 
                     y = nutrient + '_numeric', #
                     scatter_kws = {'alpha':0.5}, # 
                     line_kws = {'color':'red'}) # 
        ax.set_title(f'{nutrient} vs HV')
        ax.set_xlabel('HV')
        ax.set_ylabel(nutrient)

    plt.tight_layout()

    # # Save Plot Locally
    # plot = './resources/sav_nutrient_correlation/HV_nutrient_correlation_plot.png'
    # plt.savefig(plot)

    # Show plot
    plt.show()


# Uncomment to run code 
merged = pd.read_csv('./data/SAV/cbmocnut_sav_merged.csv') # Read csv 
data_df = pd.DataFrame(data) # Temporarily inject csv contents into data frame

HV_nutrient_correlation(data_df) # Run correlation 
HV_nutrient_correlation_plot(data_df) # Output + Save plot 