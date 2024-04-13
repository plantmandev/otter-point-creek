

import pandas as pd
import numpy as np
from statsmodels.graphics.tsaplots import plot_pacf
import matplotlib.pyplot as plt

# Assuming you've already loaded your datasets as `cbmocnut_data` and `opc_data`
opc_data = pd.read_csv('./data/SAV/opc_data.csv')

# Clean the data by replacing 'Unable to sample' with NaN and converting to numeric
opc_data['HV'] = pd.to_numeric(opc_data['HV'], errors='coerce')  # Converts 'Unable to sample' to NaN
# If you're using Secchi depth, perform a similar cleaning step
opc_data['Secchi (m)'] = pd.to_numeric(opc_data['Secchi (m)'], errors='coerce')

# Dropping rows with NaN values if necessary or filling them with a method appropriate for your analysis
opc_data.dropna(subset=['HV'], inplace=True)  # Removes rows where 'HV' is NaN
# Similarly for Secchi depth
opc_data.dropna(subset=['Secchi (m)'], inplace=True)

# Now, plotting the PACF should work without encountering the conversion error
fig, ax = plt.subplots(figsize=(10, 6))
plot_pacf(opc_data['HV'], ax=ax, lags=20, method='ywm')
plt.title('PACF for SAV (HV)')
plt.xlabel('Lags')
plt.ylabel('Partial Autocorrelation')
plt.show()

