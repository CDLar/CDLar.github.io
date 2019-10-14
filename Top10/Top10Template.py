import pandas as pd
import csv

data = pd.read_csv('C:\\Users\\Curtis\\OneDrive\\Documents\\GitHub\\BCFHL\\Top10\\test.csv')

newData = data.drop(['Rk','Opponent', 'FP/G', '% Owned', '+/-'], axis=1)
newData['Gp'] = data['FPts'].divide(data['FP/G'], fill_value=1) 
newData['Gp'] = newData['Gp'].round(0)
newData.drop(newData.index[16:], inplace=True)
newData.Gp = newData.Gp.astype(int)

print(newData)

import pandas as pd
import csv

data = pd.read_csv('2019-week1.csv')

newData = data.drop(['Rk','Opponent', 'FP/G', '% Owned', '+/-'], axis=1)
newData['Gp'] = data['FPts'].divide(data['FP/G'], fill_value=1) 
newData['Gp'] = newData['Gp'].round(0)
topData = newData.drop(newData.index[10:])

for index, row in topData.iterrows():
    x = index+1
    print(x,'. ', row['Player'],' (', row['Team'],' ',row['Position'],' - ',row['FPts'],' fpts - ','GP: ',row['Gp'], ') - Team ()',sep='')

