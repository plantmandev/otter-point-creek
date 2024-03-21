#                                        #
#   NUTRIENT DATA CORRELATION ANALYSIS   # 
#                                        # 

# TODO:
# Edit comments into proper description
# REASONING (For Tasha)

# If we find that variance in nutrient levels are correlated to each other, we can assume that upticks in these levels may be due to seasonal events that introduce sediment loads into the creek. We know that increased sediment loads lead to an increase of nutrient levels across the board. 

# If nutrient variance is not correlated, we may assume that a factor other than addition of new sediment loads into the creek is the cause of changes in nutrient concentrations over time, as we know that addition of sediment loads increases nutrient levels roughly proportionally. 

# We can assume that a dam removal will have a similar effect to these upticks in nutrient loads, but at a bigger scale, as a dam removal, specially an accelerated on will introduce more sediments than seasonal fluctuations do. 

# METHODOLOGY 
# Pearson correlation coefficient

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# This function looks at the statistical correlation between the variance nutrients PO4F, NH4F, NO2F, and NO3F in the Otter Point Creek (OPC) data from 2003 - 2022.

def nutrient_correlation():
    # Nutrient data
    cbmocnut = pd.read_csv('./cbmocnut/cbmocnut.csv')

    # Calculate correlation matrix 
    # .corr is pandas default Pearson correlation coefficient function
    correlation_matrix = cbmocnut[['PO4F', 'NH4F', 'NO2F', 'NO3F']].corr() 

    return correlation_matrix

# This function graphs the Pearson correlation coefficient results from the OPC nutrient data(2003 - 2022) into a heatmap, visualizing the correlation between variables 

def plot_correlation_heatmap(correlation_matrix):
    plt.figure(figsize = (8, 6))
    sns.heatmap(correlation_matrix, # Table output from Pearson correlation coefficient
                 annot = True, # Prints person correlation coefficients in heatmap boxes
                 fmt = ".2f", # Configures significant figures 
                 cmap='coolwarm', # Sets theme for heatmap
                 cbar_kws = {'label': 'Correlation Coefficient'}) # Labels heatmap
    plt.title('Correlation Matrix')  

    # Save Plot Locally
    plot = './resources/nutrient_correlation/nutrient_correlation_plot.png'
    plt.savefig(plot)

    # Show Plot
    plt.show()

# Uncomment to run code
# correlation_matrix = nutrient_correlation() 
# plot_correlation_heatmap(correlation_matrix) 