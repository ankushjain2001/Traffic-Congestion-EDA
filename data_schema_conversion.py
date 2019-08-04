# =============================================================================
# === Data Pre-Processing code for AL2471 Dataset =============================
# =============================================================================

# The new data from 'http://tris.highwaysengland.co.uk/detail/trafficflowdata'
# requires additional pre-processing to convert the new schema of data to the 
# old schema that was used in the project during development in 2016-17.

# This preprocessing code will work only for the data of route AL2471.

import pandas as pd
from datetime import datetime

# --- Function for Data Preprocessing -----------------------------------------

def dataPreProcessor(year):
    path = 'data/raw/a40_'+year+'.csv'
    data = pd.read_csv(path, skiprows=3)
    # Drop specific columns
    data = data.drop(columns=[' Total Flow vehicles less than 5.2m',
               ' Total Flow vehicles 5.21m - 6.6m',
               ' Total Flow vehicles 6.61m - 11.6m',
               ' Total Flow vehicles above 11.6m'], axis=1)
    # Rename specific columns to old schema
    data = data.rename(columns={'Local Date':'Date',
                         ' Local Time': 'TimePeriod',
                         ' Day Type ID': 'DayType',
                         ' Total Carriageway Flow': 'Flow',
                         ' Speed Value': 'AverageSpeed'})
    # Add new columns with ststic values as per the old schema
    data['LinkRef'] = 'AL2471'
    data['LinkDescription'] = 'A40 between A4137 and A49 (AL2471)'
    data['LinkLength'] = 7.66 # Route distance mentioned on dataset website
    # Feature engineer the time as per the old schema
    data['AverageJT'] = round((data['LinkLength']/data['AverageSpeed'])*60*60, 2)
    # Reposition the columns as per the old schema
    cols = ['LinkRef', 'LinkDescription', 'Date', 'TimePeriod', 'AverageJT', 'AverageSpeed', 'DayType', 'LinkLength', 'Flow']
    data = data[cols]
    # Sort data by Date and Time    
    data['Date'] = data['Date'].apply(lambda x: datetime.strptime(x, '%d/%m/%Y'))
    data = data.sort_values(by=['Date', 'TimePeriod'])
    # Convert Time to str
    data['Date'] = data['Date'].apply(lambda x: datetime.strftime(x, '%m/%d/%Y'))
    # Export the processed data
    return data


# --- Initiate Data Pre-Processing --------------------------------------------

OutputDFList = []
yearList = ['2010', '2011', '2012', '2013', '2014']
for i in yearList:
    OutputDFList.append(dataPreProcessor(i))
OutputDF = pd.concat(OutputDFList)
OutputDF.reset_index(drop=True, inplace=True)
OutputDF.to_csv('data/a40_new.csv', index=False)
