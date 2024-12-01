# Importing the relevant libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

# Loading the data
raw_data = pd.read_csv('Electric_Vehicle_Population_Data.csv')

# Reviewing the data
raw_data.info()
raw_data.head(3)
raw_data.describe().transpose()

# Creating a new data frame to avoid altering the original dataset
data = raw_data

# Renaming the columns of the new dataset
data.columns = ['VIN', 'County', 'City', 'State', 'Postal_Code', 'Model_Year', 'Make', 'Model', \
                'EV_Type', 'CAFV_Elig', 'Electric_Range', 'Base_MSRP', 'Legislative_District', \
                'DOL_Vehicle_ID', 'Vehicle_Location', 'Electric_Utility', '2020_Census_Tract']
data.head(3)

# Subsetting the data for the analysis
datasub1 = data[['County', 'City', 'State', 'Model_Year', 'Make', 'Model', 'EV_Type', 'Vehicle_Location']]

# We think Tesla could be dominant in the makes and proceed with a quick check
dfTesla = datasub1[datasub1.Make == 'TESLA']
dfTesla.info()
PercentTesla = len(dfTesla)/len(data)*100
round(PercentTesla,2)
