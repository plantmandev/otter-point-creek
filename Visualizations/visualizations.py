#                    # 
#   VISUALIZATIONS   # 
#                    # 

# This file contains funcions used for the creation of visualizations depicting the changes 
# in Temperature (C°), salinity, dissolved oxygen (mg/L), pH, orthophosphate (mg/L), ammonium (mg/L),# 
# nitrite (mg/L), nitrate (mg/L) and chlorophyll A (µg/L) from 2003 to 2023. 

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Setting figure sizes (all visualizations / plots)
plt.figure(figsize=(10,5))  # Height, Width

def temperature_plot(): 
    # Read master nutrient file
    cbmocwq = pd.read_csv('./Otter Point Creek Water Quality Data/cbmocwq.csv')

    # Extracts date from csv and saves data into 'Datetime' (universal)
    cbmocwq['Datetime'] = pd.to_datetime(cbmocwq['DateTimeStamp'])

    # Add axis legends + Title 
    plt.plot(cbmocwq['Datetime'], cbmocwq['Temp'], color='orange')
    plt.xlabel('Date')
    plt.ylabel('Temperature (C°)')
    plt.title(f'Otter Point Creek Temperature (2003-2023)') 
    plt.xticks(rotation=45)
    plt.legend()

    # Save Plot Locally
    plot = './Visualizations/temperature_plot.png'
    plt.savefig(plot)

    # Show Plot
    plt.show()

def salinity_plot(): 
    # Read master nutrient file
    cbmocwq = pd.read_csv('./Otter Point Creek Water Quality Data/cbmocwq.csv')

    # Extracts date from csv and saves data into 'Datetime' (universal)
    cbmocwq['Datetime'] = pd.to_datetime(cbmocwq['DateTimeStamp'])

    # Add axis legends + Title 
    plt.plot(cbmocwq['Datetime'], cbmocwq['Sal'], color='green')
    plt.xlabel('Date')
    plt.ylabel('Salinity')
    plt.title(f'Otter Point Creek Salinity (2003-2023)') 
    plt.xticks(rotation=45)
    plt.legend()

    # Save Plot Locally
    plot = './Visualizations/salinity_plot.png'
    plt.savefig(plot)

    # Show Plot
    plt.show()

def dissolved_oxygen_plot(): 
    # Read master nutrient file
    cbmocwq = pd.read_csv('./Otter Point Creek Water Quality Data/cbmocwq.csv')

    # Extracts date from csv and saves data into 'Datetime' (universal)
    cbmocwq['Datetime'] = pd.to_datetime(cbmocwq['DateTimeStamp'])

    # Add axis legends + Title 
    plt.plot(cbmocwq['Datetime'], cbmocwq['DO_mgl'], color='green')
    plt.xlabel('Date')
    plt.ylabel('Dissolved Oxygen (mg/L)')
    plt.title(f'Otter Point Creek Dissolved Oxygen (2003-2023)') 
    plt.xticks(rotation=45)
    plt.legend()

    # Save Plot Locally
    plot = './Visualizations/dissolved_oxygen_plot.png'
    plt.savefig(plot)

    # Show Plot
    plt.show()

def pH_plot(): 
    # Read master nutrient file
    cbmocwq = pd.read_csv('./Otter Point Creek Water Quality Data/cbmocwq.csv')

    # Extracts date from csv and saves data into 'Datetime' (universal)
    cbmocwq['Datetime'] = pd.to_datetime(cbmocwq['DateTimeStamp'])

    # Add axis legends + Title 
    plt.plot(cbmocwq['Datetime'], cbmocwq['pH'], color='brown')
    plt.xlabel('Date')
    plt.ylabel('pH')
    plt.title(f'Otter Point Creek pH (2003-2023)') 
    plt.xticks(rotation=45)
    plt.legend()

    # Save Plot Locally
    plot = './Visualizations/pH_plot.png'
    plt.savefig(plot)

    # Show Plot
    plt.show()

def PO4F_plot():
    # Read master nutrient file
    cbmocnut = pd.read_csv('./Otter Point Creek Nutrient Data/cbmocnut.csv')

    # Extracts date from csv and saves data into 'Datetime' (universal)
    cbmocnut['Datetime'] = pd.to_datetime(cbmocnut['DateTimeStamp'])

    # Add axis legends + Title 
    plt.plot(cbmocnut['Datetime'], cbmocnut['PO4F'], color='blue')
    plt.xlabel('Date')
    plt.ylabel('PO4F (ml/L)')
    plt.title(f'Otter Point Creek Orthophosphate (2003-2023)') 
    plt.xticks(rotation=45)
    plt.legend()

    # Save Plot Locally
    plot = './Visualizations/P04F_plot.png'
    plt.savefig(plot)

    # Show Plot
    plt.show()

def NH4F_plot(): 
    # Read master nutrient file
    cbmocnut = pd.read_csv('./Otter Point Creek Nutrient Data/cbmocnut.csv')

    # Extracts date from csv and saves data into 'Datetime' (universal)
    cbmocnut['Datetime'] = pd.to_datetime(cbmocnut['DateTimeStamp'])

    # Add axis legends + Title 
    plt.plot(cbmocnut['Datetime'], cbmocnut['NH4F'], color='gray')
    plt.xlabel('Date')
    plt.ylabel('NH4F (ml/L)')
    plt.title(f'Otter Point Creek Ammonium (2003-2023)') 
    plt.xticks(rotation=45)
    plt.legend()

    # Save Plot Locally
    plot = './Visualizations/NH4F_plot.png'
    plt.savefig(plot)

    # Show Plot
    plt.show()

def NO2F_plot():
    # Read master nutrient file
    cbmocnut = pd.read_csv('./Otter Point Creek Nutrient Data/cbmocnut.csv')

    # Extracts date from csv and saves data into 'Datetime' (universal)
    cbmocnut['Datetime'] = pd.to_datetime(cbmocnut['DateTimeStamp'])

    # Add axis legends + Title 
    plt.plot(cbmocnut['Datetime'], cbmocnut['NO2F'], color='purple')
    plt.xlabel('Date')
    plt.ylabel('NO2F (ml/L)')
    plt.title(f'Otter Point Creek Nitrite (2003-2023)') 
    plt.xticks(rotation=45)
    plt.legend()

    # Save Plot Locally
    plot = './Visualizations/NO2F_plot.png'
    plt.savefig(plot)

    # Show Plot
    plt.show() 

def NO3F_plot():
    # Read master nutrient file
    cbmocnut = pd.read_csv('./Otter Point Creek Nutrient Data/cbmocnut.csv')

    # Extracts date from csv and saves data into 'Datetime' (universal)
    cbmocnut['Datetime'] = pd.to_datetime(cbmocnut['DateTimeStamp'])

    # Add axis legends + Title 
    plt.plot(cbmocnut['Datetime'], cbmocnut['NO3F'], color='pink')
    plt.xlabel('Date')
    plt.ylabel('NO3F (ml/L)')
    plt.title(f'Otter Point Creek Nitrate (2003-2023)') 
    plt.xticks(rotation=45)
    plt.legend()

    # Save Plot Locally
    plot = './Visualizations/NO3F_plot.png'
    plt.savefig(plot)

    # Show Plot
    plt.show() 

def CHLA_plot(): 
    # Read master nutrient file
    cbmocnut = pd.read_csv('./Otter Point Creek Nutrient Data/cbmocnut.csv')

    # Extracts date from csv and saves data into 'Datetime' (universal)
    cbmocnut['Datetime'] = pd.to_datetime(cbmocnut['DateTimeStamp'])

    # Add axis legends + Title 
    plt.plot(cbmocnut['Datetime'], cbmocnut['CHLA_N'], color='red')
    plt.xlabel('Date')
    plt.ylabel('CHLA (µg/L)')
    plt.title(f'Otter Point Creek Chlorophyll A (2003-2023)') 
    plt.xticks(rotation=45)
    plt.legend()

    # Save Plot Locally
    plot = './Visualizations/CHLA_plot.png'
    plt.savefig(plot)

    # Show Plot
    plt.show() 

# Uncomment + Run to generate visualizations 
# temperature_plot()
# salinity_plot()
# dissolved_oxygen_plot()
# pH_plot()
# PO4F_plot()
# NH4F_plot()
# NO2F_plot()
# NO3F_plot()
# CHLA_plot()
    
