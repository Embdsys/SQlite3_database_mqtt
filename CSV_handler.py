import pandas as pd

def showDevices():
    filename = 'Data/devices.csv'
    df = pd.read_csv(filename)
    for index, row in df.iterrows():
        print(row)
        print("/////////////////////////")
        return df

#showDevices()