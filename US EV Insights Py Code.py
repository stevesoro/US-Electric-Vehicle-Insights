import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raw_data = pd.read_csv('Electric_Vehicle_Population_Data.csv')
raw_data.info()
raw_data.head(3)
raw_data.describe().transpose()
data = raw_data
data.columns = ['VIN', 'County', 'City', 'State', 'Postal_Code', 'Model_Year', 'Make', 'Model', \
                'EV_Type', 'CAFV_Elig', 'Electric_Range', 'Base_MSRP', 'Legislative_District', \
                'DOL_Vehicle_ID', 'Vehicle_Location', 'Electric_Utility', '2020_Census_Tract']
data.head(3)
datasub1 = data[['County', 'City', 'State', 'Model_Year', 'Make', 'Model', 'EV_Type', 'Vehicle_Location']]
dfTesla = datasub1[datasub1.Make == 'TESLA']
dfTesla.info()
PercentTesla = len(dfTesla)/len(data)*100
round(PercentTesla,2)
