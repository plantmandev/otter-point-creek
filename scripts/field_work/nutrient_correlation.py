#                                        #
#   NUTRIENT DATA CORRELATION ANALYSIS   # 
#                                        # 

# The following functions create a pearson correlation coefficient analysis for PO4F, NH4F, NO2F, and NO3F and a heatmap visualization in order to better understand any relationship between these nutrients when sediments are dissolved in water. This analysis will help us determine if upticks in nutrients are related, which tells us about the way these nutrients are dissolved into the stream. This analysis will give us a better understanding of how the sediments stored behind the Atkisson dam will change the nutrient concentration in the Otter Point Creek. This analysis can further reveal information about how nutrients in sediments are dissolved into the stream and any difference in the rate of dissolution. 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# This function looks at the statistical correlation between the variance nutrients PO4F, NH4F, NO2F, and NO3F in the Otter Point Creek (OPC) data from 2003 - 2022.

def nutrient_pearson(cbmocnut_path):
    # Load data
    cbmocnut = pd.read_csv(cbmocnut_path)

    # Calculate pearson correlation matrix 
    pearson = cbmocnut[['PO4F', 'NH4F', 'NO2F', 'NO3F']].corr() 

    return pearson

# This function graphs the Pearson correlation coefficient results from the OPC nutrient data (2003 - 2022) into a heatmap, visualizing the correlation between variables 

def plot_correlation_heatmap(pearson):
    plt.figure(figsize = (8, 6))
    sns.heatmap(pearson, # Table output from Pearson correlation coefficient
                 annot = True, # Prints person correlation coefficients in heatmap boxes
                 fmt = ".2f", # Configures significant figures 
                 cmap='coolwarm', # Sets theme for heatmap
                 cbar_kws = {'label': 'Correlation Coefficient'}) # Labels heatmap
    plt.title('Nutrient Pearson Correlation Matrix')  

    # # Save Plot Locally
    # plot = './resources/resources/sav_nutrient_correlation.png'
    # plt.savefig(plot)

    # Show Plot
    plt.show()

# --------------------------------------------
#                VARIABLES                   
cbmocnut_path = './data/cbmocnut/cbmocnut.csv'
pearson = nutrient_pearson(cbmocnut_path) 
# ---------------------------------------------

# Uncomment below code to run
plot_correlation_heatmap(pearson) 