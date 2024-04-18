#                             # 
#   SEDIMENT VISUALIZATIONS   # 
#                             #

# The following functions plot the field-derived sediment samples (Atkisson Dam, Van Bibber Dam and Otter Point Creek) with an 'optimal range' bar for each of the items being analyzed. This 'optimal range' bar is derived from recommendations from the Environmental Protection Agency for optimizing the health of estuarine systems such as the one being analyzed in this study. 

import pandas as pd
import matplotlib.pyplot as plt

def potassium_sediment_plot(sediment_data_path):
    # Load the data
    sediment_data = pd.read_csv(sediment_data_path)

    # Process potassium data, excluding the optimal range entry
    potassium_data = sediment_data[~sediment_data['Site'].str.contains("Optimal Range", na = False)]
    potassium_data['Potassium (ppm)'] = pd.to_numeric(potassium_data['Potassium (ppm)'], errors = 'coerce')

    # Extract the optimal range from the row labeled 'Optimal Range'
    optimal_range = sediment_data[sediment_data['Site'] == 'Optimal Range']['Potassium (ppm)'].values[0]
    optimal_low, optimal_high = map(float, optimal_range.replace(' ppm', '').split(' - '))

    # Create the plot
    fig, ax = plt.subplots(figsize = (10, 6))
    bars = ax.bar(potassium_data['Site'], potassium_data['Potassium (ppm)'], color = 'blue')
    ax.axhspan(optimal_low, optimal_high, color = 'lightgreen', alpha = 0.5, label = 'Optimal Range')

    # Highlight bars within the optimal range in green
    for bar in bars:
        if optimal_low <= bar.get_height() <= optimal_high:
            bar.set_color('blue')

    # Add labels, title, and legend
    ax.set_xlabel('Site')
    ax.set_ylabel('Potassium (ppm)')
    ax.set_title('Potassium Concentration Across Sites with Optimal Range')
    ax.legend()

    plt.xticks(ha = 'center', wrap = True)
    plt.tight_layout()
    
    # Save Plot Locally
    plot = './resources/sediment_visualizations/potassium_sediment_plot'
    plt.savefig(plot)

    # Show plot
    plt.show()

def ph_sediment_plot(sediment_data_path): 
    # Load the data
    sediment_data = pd.read_csv(sediment_data_path)

    # Process ph data, excluding the optimal range entry
    ph_data = sediment_data[~sediment_data['Site'].str.contains("Optimal Range", na = False)]
    ph_data['pH'] = pd.to_numeric(ph_data['pH'], errors = 'coerce')

    # Extract the optimal range from the row labeled 'Optimal Range'
    optimal_range = sediment_data[sediment_data['Site'] == 'Optimal Range']['pH'].values[0]
    optimal_low, optimal_high = map(float, optimal_range.replace(' pH', '').split(' - '))

    # Create the plot
    fig, ax = plt.subplots(figsize = (12, 6))
    bars = ax.bar(ph_data['Site'], ph_data['pH'], color = 'blue')
    ax.axhspan(optimal_low, optimal_high, color = 'lightgreen', alpha = 0.5, label = 'Optimal Range')

    # Highlight bars within the optimal range in green
    for bar in bars:
        if optimal_low <= bar.get_height() <= optimal_high:
            bar.set_color('blue')

    # Add labels, title, and legend
    ax.set_xlabel('Site')
    ax.set_ylabel('pH')
    ax.set_title('pH Across Sites with Optimal Range')
    ax.legend

    plt.xticks(ha = 'center', wrap = True)
    plt.tight_layout
    
    # Save Plot Locally
    plot = './resources/sediment_visualizations/ph_sediment_plot'
    plt.savefig(plot)

    # Show plot
    plt.show()

def nitrogen_sediment_plot(sediment_data_path): 
    # Load the data
    sediment_data = pd.read_csv(sediment_data_path)

    # Process nitrogen (ppm) data, excluding the optimal range entry
    nitrogen_data = sediment_data[~sediment_data['Site'].str.contains("Optimal Range", na = False)]
    nitrogen_data['Nitrogen (ppm)'] = pd.to_numeric(nitrogen_data['Nitrogen (ppm)'], errors = 'coerce')

    # Extract the optimal range from the row labeled 'Optimal Range'
    optimal_range = sediment_data[sediment_data['Site'] == 'Optimal Range']['Nitrogen (ppm)'].values[0]
    optimal_low, optimal_high = map(float, optimal_range.replace(' Nitrogen (ppm)', '').split(' - '))

    # Create the plot
    fig, ax = plt.subplots(figsize = (12, 6))
    bars = ax.bar(nitrogen_data['Site'], nitrogen_data['Nitrogen (ppm)'], color = 'blue')
    ax.axhspan(optimal_low, optimal_high, color = 'lightgreen', alpha = 0.5, label = 'Optimal Range')

    # Highlight bars within the optimal range in green
    for bar in bars:
        if optimal_low <= bar.get_height() <= optimal_high:
            bar.set_color('blue')

    # Add labels, title, and legend
    ax.set_xlabel('Site')
    ax.set_ylabel('Nitrogen (ppm)')
    ax.set_title('Nitrogen (ppm) Across Sites with Optimal Range')
    ax.legend

    plt.xticks(ha = 'center', wrap = True)
    plt.tight_layout
    
    # Save Plot Locally
    plot = './resources/sediment_visualizations/nitrogen_sediment_plot'
    plt.savefig(plot)

    # Show plot
    plt.show()

def nitrate_sediment_plot(sediment_data_path): 
    # Load the data
    sediment_data = pd.read_csv(sediment_data_path)

    # Process ph data, excluding the optimal range entry
    nitrate_data = sediment_data[~sediment_data['Site'].str.contains("Optimal Range", na = False)]
    nitrate_data['Nitrate (ppm)'] = pd.to_numeric(nitrate_data['Nitrate (ppm)'], errors = 'coerce')

    # Extract the optimal range from the row labeled 'Optimal Range'
    optimal_range = sediment_data[sediment_data['Site'] == 'Optimal Range']['Nitrate (ppm)'].values[0]
    optimal_low, optimal_high = map(float, optimal_range.replace(' Nitrate (ppm)', '').split(' - '))

    # Create the plot
    fig, ax = plt.subplots(figsize = (12, 6))
    bars = ax.bar(nitrate_data['Site'], nitrate_data['Nitrate (ppm)'], color = 'blue')
    ax.axhspan(optimal_low, optimal_high, color = 'lightgreen', alpha = 0.5, label = 'Optimal Range')

    # Highlight bars within the optimal range in green
    for bar in bars:
        if optimal_low <= bar.get_height() <= optimal_high:
            bar.set_color('blue')

    # Add labels, title, and legend
    ax.set_xlabel('Site')
    ax.set_ylabel('Nitrate (ppm)')
    ax.set_title('Nitrate (ppm) Across Sites with Optimal Range')
    ax.legend

    plt.xticks(ha = 'center', wrap = True)
    plt.tight_layout
    
    # Save Plot Locally
    plot = './resources/sediment_visualizations/nitrate_sediment_plot'
    plt.savefig(plot)

    # Show plot
    plt.show()

def ammonium_sediment_plot(sediment_data_path): 
    # Load the data
    sediment_data = pd.read_csv(sediment_data_path)

    # Process ph data, excluding the optimal range entry
    ammonium_data = sediment_data[~sediment_data['Site'].str.contains("Optimal Range", na = False)]
    ammonium_data['Ammonium (ppm)'] = pd.to_numeric(ammonium_data['Ammonium (ppm)'], errors = 'coerce')

    # Extract the optimal range from the row labeled 'Optimal Range'
    optimal_range = sediment_data[sediment_data['Site'] == 'Optimal Range']['Ammonium (ppm)'].values[0]
    optimal_low, optimal_high = map(float, optimal_range.replace(' Ammonium (ppm)', '').split(' - '))

    # Create the plot
    fig, ax = plt.subplots(figsize = (12, 6))
    bars = ax.bar(ammonium_data['Site'], ammonium_data['Ammonium (ppm)'], color = 'blue')
    ax.axhspan(optimal_low, optimal_high, color = 'lightgreen', alpha = 0.5, label = 'Optimal Range')

    # Highlight bars within the optimal range in green
    for bar in bars:
        if optimal_low <= bar.get_height() <= optimal_high:
            bar.set_color('blue')

    # Add labels, title, and legend
    ax.set_xlabel('Site')
    ax.set_ylabel('Ammonium (ppm)')
    ax.set_title('Ammonium (ppm) Across Sites with Optimal Range')
    ax.legend

    plt.xticks(ha = 'center', wrap = True)
    plt.tight_layout
    
    # Save Plot Locally
    plot = './resources/sediment_visualizations/ammonium_sediment_plot'
    plt.savefig(plot)

    # Show plot
    plt.show()

def phosphorus_sediment_plot(sediment_data_path):
    # Load the data
    sediment_data = pd.read_csv(sediment_data_path)

    # Process phosphorus data, excluding the optimal range entry
    phosphorus_data = sediment_data[~sediment_data['Site'].str.contains("Optimal Range", na = False)]
    phosphorus_data['Phosphorus (ppm)'] = pd.to_numeric(phosphorus_data['Phosphorus (ppm)'], errors = 'coerce')

    # Extract the optimal range from the row labeled 'Optimal Range'
    optimal_range = sediment_data[sediment_data['Site'] == 'Optimal Range']['Phosphorus (ppm)'].values[0]
    optimal_low, optimal_high = map(float, optimal_range.replace(' Phosphorus (ppm)', '').split(' - '))

    # Create the plot
    fig, ax = plt.subplots(figsize = (10, 6))
    bars = ax.bar(phosphorus_data['Site'], phosphorus_data['Phosphorus (ppm)'], color = 'blue')
    ax.axhspan(optimal_low, optimal_high, color = 'lightgreen', alpha = 0.5, label = 'Optimal Range')

    # Highlight bars within the optimal range in green
    for bar in bars:
        if optimal_low <= bar.get_height() <= optimal_high:
            bar.set_color('blue')

    # Add labels, title, and legend
    ax.set_xlabel('Site')
    ax.set_ylabel('Phosphorus (ppm)')
    ax.set_title('Phosphorus Concentration Across Sites with Optimal Range')
    ax.legend()

    plt.xticks(ha = 'center', wrap = True)
    plt.tight_layout()
    
    # Save Plot Locally
    plot = './resources/sediment_visualizations/phosphorus_sediment_plot'
    plt.savefig(plot)

    # Show plot
    plt.show()

def potassium_sediment_plot(sediment_data_path):
    # Load the data
    sediment_data = pd.read_csv(sediment_data_path)

    # Process potassium data, excluding the optimal range entry
    potassium_data = sediment_data[~sediment_data['Site'].str.contains("Optimal Range", na = False)]
    potassium_data['Potassium (ppm)'] = pd.to_numeric(potassium_data['Potassium (ppm)'], errors = 'coerce')

    # Extract the optimal range from the row labeled 'Optimal Range'
    optimal_range = sediment_data[sediment_data['Site'] == 'Optimal Range']['Potassium (ppm)'].values[0]
    optimal_low, optimal_high = map(float, optimal_range.replace(' Potassium (ppm)', '').split(' - '))

    # Create the plot
    fig, ax = plt.subplots(figsize = (10, 6))
    bars = ax.bar(potassium_data['Site'], potassium_data['Potassium (ppm)'], color = 'blue')
    ax.axhspan(optimal_low, optimal_high, color = 'lightgreen', alpha = 0.5, label = 'Optimal Range')

    # Highlight bars within the optimal range in green
    for bar in bars:
        if optimal_low <= bar.get_height() <= optimal_high:
            bar.set_color('blue')

    # Add labels, title, and legend
    ax.set_xlabel('Site')
    ax.set_ylabel('Potassium (ppm)')
    ax.set_title('Potassium Concentration Across Sites with Optimal Range')
    ax.legend()

    plt.xticks(ha = 'center', wrap = True)
    plt.tight_layout()
    
    # Save Plot Locally
    plot = './resources/sediment_visualizations/potassium_sediment_plot'
    plt.savefig(plot)

    # Show plot
    plt.show()

def sulfur_sediment_plot(sediment_data_path):
    # Load the data
    sediment_data = pd.read_csv(sediment_data_path)

    # Process sulfur data, excluding the optimal range entry
    sulfur_data = sediment_data[~sediment_data['Site'].str.contains("Optimal Range", na = False)]
    sulfur_data['Sulfur (ppm)'] = pd.to_numeric(sulfur_data['Sulfur (ppm)'], errors = 'coerce')

    # Extract the optimal range from the row labeled 'Optimal Range'
    optimal_range = sediment_data[sediment_data['Site'] == 'Optimal Range']['Sulfur (ppm)'].values[0]
    optimal_low, optimal_high = map(float, optimal_range.replace(' Sulfur (ppm)', '').split(' - '))

    # Create the plot
    fig, ax = plt.subplots(figsize = (10, 6))
    bars = ax.bar(sulfur_data['Site'], sulfur_data['Sulfur (ppm)'], color = 'blue')
    ax.axhspan(optimal_low, optimal_high, color = 'lightgreen', alpha = 0.5, label = 'Optimal Range')

    # Highlight bars within the optimal range in green
    for bar in bars:
        if optimal_low <= bar.get_height() <= optimal_high:
            bar.set_color('blue')

    # Add labels, title, and legend
    ax.set_xlabel('Site')
    ax.set_ylabel('Sulfur (ppm)')
    ax.set_title('Sulfur Concentration Across Sites with Optimal Range')
    ax.legend()

    plt.xticks(ha = 'center', wrap = True)
    plt.tight_layout()
    
    # Save Plot Locally
    plot = './resources/sediment_visualizations/sulfur_sediment_plot'
    plt.savefig(plot)

    # Show plot
    plt.show()

def calcium_sediment_plot(sediment_data_path):
    # Load the data
    sediment_data = pd.read_csv(sediment_data_path)

    # Process calcium data, excluding the optimal range entry
    calcium_data = sediment_data[~sediment_data['Site'].str.contains("Optimal Range", na = False)]
    calcium_data['Calcium (ppm)'] = pd.to_numeric(calcium_data['Calcium (ppm)'], errors = 'coerce')

    # Extract the optimal range from the row labeled 'Optimal Range'
    optimal_range = sediment_data[sediment_data['Site'] == 'Optimal Range']['Calcium (ppm)'].values[0]
    optimal_low, optimal_high = map(float, optimal_range.replace(' Calcium (ppm)', '').split(' - '))

    # Create the plot
    fig, ax = plt.subplots(figsize = (10, 6))
    bars = ax.bar(calcium_data['Site'], calcium_data['Calcium (ppm)'], color = 'blue')
    ax.axhspan(optimal_low, optimal_high, color = 'lightgreen', alpha = 0.5, label = 'Optimal Range')

    # Highlight bars within the optimal range in green
    for bar in bars:
        if optimal_low <= bar.get_height() <= optimal_high:
            bar.set_color('blue')

    # Add labels, title, and legend
    ax.set_xlabel('Site')
    ax.set_ylabel('Calcium (ppm)')
    ax.set_title('Calcium Concentration Across Sites with Optimal Range')
    ax.legend()

    plt.xticks(ha = 'center', wrap = True)
    plt.tight_layout()
    
    # Save Plot Locally
    plot = './resources/sediment_visualizations/calcium_sediment_plot'
    plt.savefig(plot)

    # Show plot
    plt.show()

def magnesium_sediment_plot(sediment_data_path):
    # Load the data
    sediment_data = pd.read_csv(sediment_data_path)

    # Process magnesium data, excluding the optimal range entry
    magnesium_data = sediment_data[~sediment_data['Site'].str.contains("Optimal Range", na = False)]
    magnesium_data['Magnesium (ppm)'] = pd.to_numeric(magnesium_data['Magnesium (ppm)'], errors = 'coerce')

    # Extract the optimal range from the row labeled 'Optimal Range'
    optimal_range = sediment_data[sediment_data['Site'] == 'Optimal Range']['Magnesium (ppm)'].values[0]
    optimal_low, optimal_high = map(float, optimal_range.replace(' Magnesium (ppm)', '').split(' - '))

    # Create the plot
    fig, ax = plt.subplots(figsize = (10, 6))
    bars = ax.bar(magnesium_data['Site'], magnesium_data['Magnesium (ppm)'], color = 'blue')
    ax.axhspan(optimal_low, optimal_high, color = 'lightgreen', alpha = 0.5, label = 'Optimal Range')

    # Highlight bars within the optimal range in green
    for bar in bars:
        if optimal_low <= bar.get_height() <= optimal_high:
            bar.set_color('blue')

    # Add labels, title, and legend
    ax.set_xlabel('Site')
    ax.set_ylabel('Magnesium (ppm)')
    ax.set_title('Magnesium Concentration Across Sites with Optimal Range')
    ax.legend()

    plt.xticks(ha = 'center', wrap = True)
    plt.tight_layout()
    
    # Save Plot Locally
    plot = './resources/sediment_visualizations/magnesium_sediment_plot'
    plt.savefig(plot)

    # Show plot
    plt.show()

def iron_sediment_plot(sediment_data_path):
    # Load the data
    sediment_data = pd.read_csv(sediment_data_path)

    # Process iron data, excluding the optimal range entry
    iron_data = sediment_data[~sediment_data['Site'].str.contains("Optimal Range", na = False)]
    iron_data['Iron (ppm)'] = pd.to_numeric(iron_data['Iron (ppm)'], errors = 'coerce')

    # Extract the optimal range from the row labeled 'Optimal Range'
    optimal_range = sediment_data[sediment_data['Site'] == 'Optimal Range']['Iron (ppm)'].values[0]
    optimal_low, optimal_high = map(float, optimal_range.replace(' Iron (ppm)', '').split(' - '))

    # Create the plot
    fig, ax = plt.subplots(figsize = (10, 6))
    bars = ax.bar(iron_data['Site'], iron_data['Iron (ppm)'], color = 'blue')
    ax.axhspan(optimal_low, optimal_high, color = 'lightgreen', alpha = 0.5, label = 'Optimal Range')

    # Highlight bars within the optimal range in green
    for bar in bars:
        if optimal_low <= bar.get_height() <= optimal_high:
            bar.set_color('blue')

    # Add labels, title, and legend
    ax.set_xlabel('Site')
    ax.set_ylabel('Iron (ppm)')
    ax.set_title('Iron Concentration Across Sites with Optimal Range')
    ax.legend()

    plt.xticks(ha = 'center', wrap = True)
    plt.tight_layout()
    
    # Save Plot Locally
    plot = './resources/sediment_visualizations/iron_sediment_plot'
    plt.savefig(plot)

    # Show plot
    plt.show()

def manganese_sediment_plot(sediment_data_path):
    # Load the data
    sediment_data = pd.read_csv(sediment_data_path)

    # Process manganese data, excluding the optimal range entry
    manganese_data = sediment_data[~sediment_data['Site'].str.contains("Optimal Range", na = False)]
    manganese_data['Manganese (ppm)'] = pd.to_numeric(manganese_data['Manganese (ppm)'], errors = 'coerce')

    # Extract the optimal range from the row labeled 'Optimal Range'
    optimal_range = sediment_data[sediment_data['Site'] == 'Optimal Range']['Manganese (ppm)'].values[0]
    optimal_low, optimal_high = map(float, optimal_range.replace(' Manganese (ppm)', '').split(' - '))

    # Create the plot
    fig, ax = plt.subplots(figsize = (10, 6))
    bars = ax.bar(manganese_data['Site'], manganese_data['Manganese (ppm)'], color = 'blue')
    ax.axhspan(optimal_low, optimal_high, color = 'lightgreen', alpha = 0.5, label = 'Optimal Range')

    # Highlight bars within the optimal range in green
    for bar in bars:
        if optimal_low <= bar.get_height() <= optimal_high:
            bar.set_color('blue')

    # Add labels, title, and legend
    ax.set_xlabel('Site')
    ax.set_ylabel('Manganese (ppm)')
    ax.set_title('Manganese Concentration Across Sites with Optimal Range')
    ax.legend()

    plt.xticks(ha = 'center', wrap = True)
    plt.tight_layout()
    
    # Save Plot Locally
    plot = './resources/sediment_visualizations/manganese_sediment_plot'
    plt.savefig(plot)

    # Show plot
    plt.show()

def zinc_sediment_plot(sediment_data_path):
    # Load the data
    sediment_data = pd.read_csv(sediment_data_path)

    # Process zinc data, excluding the optimal range entry
    zinc_data = sediment_data[~sediment_data['Site'].str.contains("Optimal Range", na = False)]
    zinc_data['Zinc (ppm)'] = pd.to_numeric(zinc_data['Zinc (ppm)'], errors = 'coerce')

    # Extract the optimal range from the row labeled 'Optimal Range'
    optimal_range = sediment_data[sediment_data['Site'] == 'Optimal Range']['Zinc (ppm)'].values[0]
    optimal_low, optimal_high = map(float, optimal_range.replace(' Zinc (ppm)', '').split(' - '))

    # Create the plot
    fig, ax = plt.subplots(figsize = (10, 6))
    bars = ax.bar(zinc_data['Site'], zinc_data['Zinc (ppm)'], color = 'blue')
    ax.axhspan(optimal_low, optimal_high, color = 'lightgreen', alpha = 0.5, label = 'Optimal Range')

    # Highlight bars within the optimal range in green
    for bar in bars:
        if optimal_low <= bar.get_height() <= optimal_high:
            bar.set_color('blue')

    # Add labels, title, and legend
    ax.set_xlabel('Site')
    ax.set_ylabel('Zinc (ppm)')
    ax.set_title('Zinc Concentration Across Sites with Optimal Range')
    ax.legend()

    plt.xticks(ha = 'center', wrap = True)
    plt.tight_layout()
    
    # Save Plot Locally
    plot = './resources/sediment_visualizations/zinc_sediment_plot'
    plt.savefig(plot)

    # Show plot
    plt.show()

def copper_sediment_plot(sediment_data_path):
    # Load the data
    sediment_data = pd.read_csv(sediment_data_path)

    # Process copper data, excluding the optimal range entry
    copper_data = sediment_data[~sediment_data['Site'].str.contains("Optimal Range", na = False)]
    copper_data['Copper (ppm)'] = pd.to_numeric(copper_data['Copper (ppm)'], errors = 'coerce')

    # Extract the optimal range from the row labeled 'Optimal Range'
    optimal_range = sediment_data[sediment_data['Site'] == 'Optimal Range']['Copper (ppm)'].values[0]
    optimal_low, optimal_high = map(float, optimal_range.replace(' Copper (ppm)', '').split(' - '))

    # Create the plot
    fig, ax = plt.subplots(figsize = (10, 6))
    bars = ax.bar(copper_data['Site'], copper_data['Copper (ppm)'], color = 'blue')
    ax.axhspan(optimal_low, optimal_high, color = 'lightgreen', alpha = 0.5, label = 'Optimal Range')

    # Highlight bars within the optimal range in green
    for bar in bars:
        if optimal_low <= bar.get_height() <= optimal_high:
            bar.set_color('blue')

    # Add labels, title, and legend
    ax.set_xlabel('Site')
    ax.set_ylabel('Copper (ppm)')
    ax.set_title('Copper Concentration Across Sites with Optimal Range')
    ax.legend()

    plt.xticks(ha = 'center', wrap = True)
    plt.tight_layout()
    
    # Save Plot Locally
    plot = './resources/sediment_visualizations/copper_sediment_plot'
    plt.savefig(plot)

    # Show plot
    plt.show()

def boron_sediment_plot(sediment_data_path):
    # Load the data
    sediment_data = pd.read_csv(sediment_data_path)

    # Process boron data, excluding the optimal range entry
    boron_data = sediment_data[~sediment_data['Site'].str.contains("Optimal Range", na = False)]
    boron_data['Boron (ppm)'] = pd.to_numeric(boron_data['Boron (ppm)'], errors = 'coerce')

    # Extract the optimal range from the row labeled 'Optimal Range'
    optimal_range = sediment_data[sediment_data['Site'] == 'Optimal Range']['Boron (ppm)'].values[0]
    optimal_low, optimal_high = map(float, optimal_range.replace(' Boron (ppm)', '').split(' - '))

    # Create the plot
    fig, ax = plt.subplots(figsize = (10, 6))
    bars = ax.bar(boron_data['Site'], boron_data['Boron (ppm)'], color = 'blue')
    ax.axhspan(optimal_low, optimal_high, color = 'lightgreen', alpha = 0.5, label = 'Optimal Range')

    # Highlight bars within the optimal range in green
    for bar in bars:
        if optimal_low <= bar.get_height() <= optimal_high:
            bar.set_color('blue')

    # Add labels, title, and legend
    ax.set_xlabel('Site')
    ax.set_ylabel('Boron (ppm)')
    ax.set_title('Boron Concentration Across Sites with Optimal Range')
    ax.legend()

    plt.xticks(ha = 'center', wrap = True)
    plt.tight_layout()
    
    # Save Plot Locally
    plot = './resources/sediment_visualizations/boron_sediment_plot'
    plt.savefig(plot)

    # Show plot
    plt.show()

# Set data path
sediment_data_path = 'data/sediment/sediment_data.csv'

# Uncomment below code to run visualizations
# ph_sediment_plot(sediment_data_path)
# potassium_sediment_plot(sediment_data_path)
# nitrogen_sediment_plot(sediment_data_path)
# nitrate_sediment_plot(sediment_data_path)
# ammonium_sediment_plot(sediment_data_path)
# phosphorus_sediment_plot(sediment_data_path)
# potassium_sediment_plot(sediment_data_path)
# sulfur_sediment_plot(sediment_data_path)
# calcium_sediment_plot(sediment_data_path)
# magnesium_sediment_plot(sediment_data_path)
# sodium_sediment_plot(sediment_data_path)
# iron_sediment_plot(sediment_data_path)
# manganese_sediment_plot(sediment_data_path)
# zinc_sediment_plot(sediment_data_path)
# copper_sediment_plot(sediment_data_path)
# boron_sediment_plot(sediment_data_path)


