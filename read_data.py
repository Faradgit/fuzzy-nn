import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing
CREATE_TEST_SPLIT = False


if CREATE_TEST_SPLIT:
    data = pd.read_csv('data/data_3k.csv', delimiter=',', index_col = False)
    data = data.drop(np.where(data['y']==0)[0])
    indices = range(len(data))
    np.random.shuffle(indices)
    sep_index = int(0.8*len(data))
    training, test = indices[:sep_index], indices[sep_index:]
    train_data = data.iloc[training]
    test_data = data.iloc[test]
    train_data.to_csv('data/train.csv', index=False)
    test_data.to_csv('data/test.csv', index=False)


#times = [row.split()[1].split(':') for row in data.iloc[:,0]]
#times = [int(row[0])*60 + int(row[1]) for row in times]
#data.iloc[:,0] = times

train_data = pd.read_csv('data/train.csv', delimiter=',', index_col = False)
x = train_data.iloc[:,:4].values
test_data = pd.read_csv('data/test.csv', delimiter=',', index_col = False)
x_test = test_data.iloc[:,:4].values

min_max_scaler = preprocessing.MinMaxScaler()
min_max_scaler.fit(np.row_stack((x,x_test)))

x = min_max_scaler.transform(x)
x_test = min_max_scaler.transform(x_test)

y = train_data.iloc[:,4].values
y_test = test_data.iloc[:,4].values


rfc = RandomForestRegressor(n_estimators=1000)
rfc = rfc.fit(x, y)
round(sum(abs(rfc.predict(x) - y)/abs(y))/len(y),4)

round(sum(abs(rfc.predict(x_test) - y_test)/abs(y_test))/len(y_test),4)







