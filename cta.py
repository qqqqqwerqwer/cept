import pandas as pd
import matplotlib.pyplot as plt
#载入数据
Train_data = pd.read_csv('used_car_train_20200313.csv', sep=' ')
Teat_data = pd.read_csv('used_car_testA_20200313.csv', sep=' ')

print('train data shape:', Train_data.shape)
print('test data shape:', Teat_data.shape)
print(Train_data.head())
print(Train_data.info())
print(Train_data.describe())

Train_data.hist(bins=50)