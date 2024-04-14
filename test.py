import pandas as pd
import matplotlib.pyplot as plt


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
    plot = './resources/nitrogen_sediment_plot'
    plt.savefig(plot)

    # Show plot
    plt.show()


# Load data 
sediment_data_path = 'data/sediment/sediment_data.csv'


nitrogen_sediment_plot(sediment_data_path)
