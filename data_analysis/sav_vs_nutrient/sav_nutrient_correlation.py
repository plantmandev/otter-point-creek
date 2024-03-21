#                                         # 
#   SAV / NUTRIENT CORRELATION ANALYSIS   # 
#                                         # 

# These functions perform correlation analysis (Pearson correlation coefficient analysis) between SAV abundance (HV, MS, VA, CD, ZP and NM), based in surveys performed by the National Estuarine Research from 2003 - 2017. Additionally, these correlations are graphed to better understand the correlations over time. 

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

# This function calculates the correlation coefficients between MS (Myriophyllum spicatum) and nutrient values (PO4F, NH4F, NO2F, NO3F) in Otter Point Creek, from 2002 to 2017. 
def MS_nutrient_correlation(data): 
    # Convert relevant columns to numeric, coercing errors to NaN
    nutrients = ['PO4F', 'NH4F', 'NO2F', 'NO3F']
    for nutrient in nutrients:
        data[nutrient + '_numeric'] = pd.to_numeric(data[nutrient], errors = 'coerce')
    data['MS_numeric'] = pd.to_numeric(data['MS'], errors = 'coerce')
    
    # Calculate and return the correlation coefficients
    correlations = {}
    for nutrient in nutrients:
        correlations[f'MS vs {nutrient}'] = data['MS_numeric'].corr(data[nutrient + '_numeric'])
    
    return correlations

# This function calculates the correlation coefficients between VA (Vallisneria americana) and nutrient values (PO4F, NH4F, NO2F, NO3F) in Otter Point Creek, from 2002 to 2017. 
def VA_nutrient_correlation(data):
     # Convert relevant columns to numeric, coercing errors to NaN
    nutrients = ['PO4F', 'NH4F', 'NO2F', 'NO3F']
    for nutrient in nutrients:
        data[nutrient + '_numeric'] = pd.to_numeric(data[nutrient], errors = 'coerce')
    data['VA_numeric'] = pd.to_numeric(data['VA'], errors = 'coerce')
    
    # Calculate and return the correlation coefficients
    correlations = {}
    for nutrient in nutrients:
        correlations[f'VA vs {nutrient}'] = data['VA_numeric'].corr(data[nutrient + '_numeric'])
    
    return correlations

# This function calculates the correlation coefficients between CD (Ceratophyllum demersum) and nutrient values (PO4F, NH4F, NO2F, NO3F) in Otter Point Creek, from 2002 to 2017. 

def CD_nutrient_correlation(data):
     # Convert relevant columns to numeric, coercing errors to NaN
    nutrients = ['PO4F', 'NH4F', 'NO2F', 'NO3F']
    for nutrient in nutrients:
        data[nutrient + '_numeric'] = pd.to_numeric(data[nutrient], errors = 'coerce')
    data['CD_numeric'] = pd.to_numeric(data['CD'], errors = 'coerce')
    
    # Calculate and return the correlation coefficients
    correlations = {}
    for nutrient in nutrients:
        correlations[f'CD vs {nutrient}'] = data['CD_numeric'].corr(data[nutrient + '_numeric'])
    
    return correlations 

# This function calculates the correlation coefficients between ZP (Zannichellia palustris) and nutrient values (PO4F, NH4F, NO2F, NO3F) in Otter Point Creek, from 2002 to 2017. 

def ZP_nutrient_correlation(data):
     # Convert relevant columns to numeric, coercing errors to NaN
    nutrients = ['PO4F', 'NH4F', 'NO2F', 'NO3F']
    for nutrient in nutrients:
        data[nutrient + '_numeric'] = pd.to_numeric(data[nutrient], errors = 'coerce')
    data['ZP_numeric'] = pd.to_numeric(data['ZP'], errors = 'coerce')
    
    # Calculate and return the correlation coefficients
    correlations = {}
    for nutrient in nutrients:
        correlations[f'ZP vs {nutrient}'] = data['ZP_numeric'].corr(data[nutrient + '_numeric'])
    
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

    # Save Plot Locally
    plot = './resources/sav_nutrient_correlation/HV_nutrient_correlation_plot.png'
    plt.savefig(plot)

    # Show plot
    plt.show()

# This function scatter plots for HS (Myriophyllum spicatum) and nutrient measurements (PO4F, NH4F, NO2F, NO3F) in OPC from 2003 - 2017. 
def MS_nutrient_correlation_plot(data):
    # Formatting of plots 
    fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize = (14, 10))
    nutrients = ['PO4F', 'NH4F', 'NO2F', 'NO3F']
    
    # Iterate over nutrient type + create individual graph + merge
    for i, nutrient in enumerate(nutrients):
        ax = axes[i//2, i%2]
        sns.regplot(ax = ax,
                     data = data, #
                     x = 'MS_numeric', # 
                     y = nutrient + '_numeric', #
                     scatter_kws = {'alpha':0.5}, # 
                     line_kws = {'color':'red'}) # 
        ax.set_title(f'{nutrient} vs MS')
        ax.set_xlabel('MS')
        ax.set_ylabel(nutrient)

    plt.tight_layout()

    # Save Plot Locally
    plot = './resources/sav_nutrient_correlation/MS_nutrient_correlation_plot.png'
    plt.savefig(plot)

    # Show Plot 
    plt.show()

# This function scatter plots for VA (Vallisneria americana) and nutrient measurements (PO4F, NH4F, NO2F, NO3F) in OPC from 2003 - 2017. 
def VA_nutrient_correlation_plot(data):
    # Formatting of plots 
    fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize = (14, 10))
    nutrients = ['PO4F', 'NH4F', 'NO2F', 'NO3F']
    
    # Iterate over nutrient type + create individual graph + merge
    for i, nutrient in enumerate(nutrients):
        ax = axes[i//2, i%2]
        sns.regplot(ax = ax,
                     data = data, #
                     x = 'VA_numeric', # 
                     y = nutrient + '_numeric', #
                     scatter_kws = {'alpha':0.5}, # 
                     line_kws = {'color':'red'}) # 
        ax.set_title(f'{nutrient} vs VA')
        ax.set_xlabel('VA')
        ax.set_ylabel(nutrient)

    plt.tight_layout()

    # Save Plot Locally
    plot = './resources/sav_nutrient_correlation/VA_nutrient_correlation_plot.png'
    plt.savefig(plot)

    # Show Plot 
    plt.show()

# This function scatter plots for CD (Ceratophyllum demersum) and nutrient measurements (PO4F, NH4F, NO2F, NO3F) in OPC from 2003 - 2017. 
def CD_nutrient_correlation_plot(data):
    # Formatting of plots 
    fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize = (14, 10))
    nutrients = ['PO4F', 'NH4F', 'NO2F', 'NO3F']
    
    # Iterate over nutrient type + create individual graph + merge
    for i, nutrient in enumerate(nutrients):
        ax = axes[i//2, i%2]
        sns.regplot(ax = ax,
                     data = data, #
                     x = 'CD_numeric', # 
                     y = nutrient + '_numeric', #
                     scatter_kws = {'alpha':0.5}, # 
                     line_kws = {'color':'red'}) # 
        ax.set_title(f'{nutrient} vs VA')
        ax.set_xlabel('CD')
        ax.set_ylabel(nutrient)

    plt.tight_layout()

    # Save Plot Locally
    plot = './resources/sav_nutrient_correlation/CD_nutrient_correlation_plot.png'
    plt.savefig(plot)

    # Show Plot 
    plt.show()

# This function scatter plots for ZP (Zannichellia palustris) and nutrient measurements (PO4F, NH4F, NO2F, NO3F) in OPC from 2003 - 2017. 
def ZP_nutrient_correlation_plot(data):
    # Formatting of plots 
    fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize = (14, 10))
    nutrients = ['PO4F', 'NH4F', 'NO2F', 'NO3F']
    
    # Iterate over nutrient type + create individual graph + merge
    for i, nutrient in enumerate(nutrients):
        ax = axes[i//2, i%2]
        sns.regplot(ax = ax,
                     data = data, #
                     x = 'ZP_numeric', # 
                     y = nutrient + '_numeric', #
                     scatter_kws = {'alpha':0.5}, # 
                     line_kws = {'color':'red'}) # 
        ax.set_title(f'{nutrient} vs VA')
        ax.set_xlabel('ZP')
        ax.set_ylabel(nutrient)

    plt.tight_layout()

    # Save Plot Locally
    plot = './resources/sav_nutrient_correlationZP_nutrient_correlation_plot.png'
    plt.savefig(plot)

    # Show Plot 
    plt.show()

# Uncomment to run code 
data = pd.read_csv('./data/SAV/cbmocnut_sav_merged.csv') # Read csv 
data_df = pd.DataFrame(data) # Temporarily inject csv contents into data frame

HV_nutrient_correlation(data_df) # Run correlation 
HV_nutrient_correlation_plot(data_df) # Output + Save plot 

MS_nutrient_correlation(data_df) # Run correlation 
MS_nutrient_correlation_plot(data_df) # Output + Save plot 

VA_nutrient_correlation(data_df) # Run correlation 
VA_nutrient_correlation_plot(data_df) # Output + Save plot 

CD_nutrient_correlation(data_df) # Run correlation 
CD_nutrient_correlation_plot(data_df) # Output + Save plot 

VA_nutrient_correlation(data_df) # Run correlation 
VA_nutrient_correlation_plot(data_df) # Output + Save plot 